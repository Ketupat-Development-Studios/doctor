from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from hackapp.models import Essay
import datetime, random, json, subprocess

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            User.objects.create_user(username, username, password)
            return HttpResponse("OK.")
        else:
            match_user = authenticate(username = username, password = password)
            if match_user is not None:
                login(request, match_user)
                return HttpResponse("OK.")
            else:
                return HttpResponse("Wrong.")
    else:
        return HttpResponseNotFound()

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required
def get_markdown(request, url):
    try:
        match_essay = Essay.objects.get(user = request.user, url = url)
    except Essay.DoesNotExist:
        return HttpResponseNotFound()
    return HttpResponse(match_essay.markdown)

def lcs(a, b):
    max_len = min(len(a), len(b))
    mx_match = 0
    for i in range(1, max_len + 1):
        for j in range(1, len(a) - i + 1):
            for k in range(1, len(b) - i + 1):
                if a[j:(j+i)] == b[k:(k+i)]:
                    mx_match = max(mx_match, i)
    return mx_match

def get_links(title, markdown):
   in_tag = 0
   new_md = ""
   for char in markdown:
       if char == '<':
           in_tag = 1
       elif char == '>':
           in_tag = 0
       elif in_tag == 0:
           new_md += char
   import urllib2, urllib
   api_call = urllib2.Request('http://textalytics.com/core/topics-1.2', urllib.urlencode({
       'of': 'json',
       'lang': 'en',
       'txt': title + " " + new_md,
       'key': '139aca45c4319083bbbe86835f0b7f5f',
       'tt': 'c'
   }))
   api_result = urllib2.urlopen(api_call)
   api_result = api_result.read()
   api_res = json.loads(api_result)
   print(api_res)
   for form in api_res.concept_list:
       print(form.form)
       
   scholar = subprocess.Popen(['python', '/home/pwypeanut/hacknroll/hackapp/scholar.py', "-c", "5", "--phrase", query, "--citation", "bt"], stdout=subprocess.PIPE)
   (stdout, stderr) = scholar.communicate()
   import bibtexparser
   bib_db = bibtexparser.loads(stdout)
   ans = []
   for journal in bib_db.entries:
       ans.append([journal["title"], "scholar.google.com"])
   return ans

@login_required
def edit_markdown(request, url):
    new_title = request.POST.get('title')
    new_markdown = request.POST.get('markdown')
    try:
        match_essay = Essay.objects.get(user = request.user, url = url)
    except Essay.DoesNotExist:
        return HttpResponseNotFound()
    match_essay.title = new_title
    match_essay.markdown = new_markdown
    match_essay.save()
    return HttpResponse(json.dumps(get_links(new_title, new_markdown)))

def rand_url():
    url = ""
    sel = "abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(6):
        url += sel[random.randint(0, 36)]
    return url

@login_required
def create_essay(request):
    new_title = request.POST.get('title')
    new_markdown = request.POST.get('markdown')
    new_essay = Essay.objects.create(user = request.user, title = new_title, url = rand_url(), markdown = new_markdown, last_update = datetime.datetime.now())
    new_essay.save()
    return HttpResponse(new_essay.url)

@login_required
def delete_essay(request, url):
    try:
        essay = Essay.objects.get(user = request.user, url = url)
    except Essay.DoesNotExist:
        return HttpResponseNotFound()
    essay.delete()
    return HttpResponse()

def login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/main/")
    return render(request, "login.html", {})
    
@login_required
def main_page(request):
    user_files = Essay.objects.filter(user = request.user)
    query_file = []
    for userfile in user_files:
        url = userfile.url
        if len(userfile.title) > 10:
            tit = userfile.title[:10] + "..."
        else:
            tit = userfile.title
        query_file.append([url, tit])
    return render(request, "index.html", {
        'files': query_file,
        'username': request.user.username,
        'title': "",
        'markdown': "",
        'url': "",
    })

@login_required
def main_essay(request, url):
    try:
        essay = Essay.objects.get(user = request.user, url = url)
    except Essay.DoesNotExist:
        return HttpResponseNotFound()
    user_files = Essay.objects.filter(user = request.user)
    query_file = []
    for userfile in user_files:
        url = userfile.url
        if len(userfile.title) > 10:
            tit = userfile.title[:10] + "..."
        else:
            tit = userfile.title
        query_file.append([url, tit])
    return render(request, "index.html", {
        'files': query_file,
        'username': request.user.username,
        'title': essay.title,
        'markdown': essay.markdown,
        'url': essay.url,
    })