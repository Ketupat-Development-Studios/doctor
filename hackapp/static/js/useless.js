;useless = {

    name: 'useless',

	nyan: function(){
		$("#nyan").css("top",-$("#nyan").height());
      	$("#nyan").css("left",-$("#nyan").width());
		for(tgx=0;tgx<=5;tgx++){
			if(tgx == 0){
			  $("#nyan").animate({left:tgx/5*$(window).width(), top:tgx%2 == 0 ? 0:($(window).height()-$("#nyan").height())},500,"linear", function(){$(this).removeClass("flip");});
			} else {
			  $("#nyan").animate({left:tgx/5*$(window).width(), top:tgx%2 == 0 ? 0:($(window).height()-$("#nyan").height())},500,"linear");
			}
		}
		for(tgx=5;tgx>=0;tgx--){
			if(tgx == 5){
			  $("#nyan").animate({left:tgx/5*$(window).width(), top:tgx%2 == 0 ? 0:($(window).height()-$("#nyan").height())},500,"linear", function(){$(this).addClass("flip");});
			} else if (tgx == 0){
			  $("#nyan").animate({left:tgx/5*$(window).width() - $("#nyan").width(), top:tgx%2 == 0 ? 0:($(window).height()-$("#nyan").height())},500,"linear", function(){$(this).removeClass("flip");});
			} else {
			  $("#nyan").animate({left:tgx/5*$(window).width() - $("#nyan").width(), top:tgx%2 == 0 ? 0:($(window).height()-$("#nyan").height())},500,"linear");
			}
		}
	},
	
	dalekPatrol: function(direction){
	    if(direction == 'left'){
	        $("#dalek").animate({left:0},10000,"linear",function(){
	            $(this).addClass("flip");
    	        useless.dalekPatrol('right');
    	    });
	    } else {
    	    $("#dalek").animate({left:$(window).width()-$("#dalek").width()},10000,"linear",function(){
    	        $(this).removeClass("flip");
    	        useless.dalekPatrol('left');
    	    });
	    }
	},

	iwantGIFs: function(){
		var gifs = [];
		$.getJSON('http://whateverorigin.org/get?url=' + encodeURIComponent('http://www.reddit.com/r/gifs/hot/.json') + '&callback=?', function(herehavepie){
			$.each($.parseJSON(herehavepie.contents).data.children,function(index,value){
				gifs.push(value.data.url);
				console.log(gifs);
			});
			return gifs;
		});
	},

	lolfunny: function(){
		var funnyStuff = [];
		$.getJSON('http://whateverorigin.org/get?url=' + encodeURIComponent('http://www.reddit.com/r/funny/hot/.json') + '&callback=?', function(roflmaos){
			$.each($.parseJSON(roflmaos.contents).data.children,function(index,value){				
				funnyStuff.push(value.data.url);
				console.log(funnyStuff);
			});
			return funnyStuff;
		});
	},
	
	
}

;card = {
	create: function(contents){
		/*
			{
				image: "url", (optional)
				stuff: "card title here",
				actons: "urls at bottom" (optional)
			}
		*/
		var aceOfSpades = $("<div class='col s12'>").append($("<div class='card'>"));
		if(typeof contents.image !== 'undefined' && contents.image.length > 0){
			aceOfSpades.children("div.card").append($("<div class='card-image'>")
				.append($("<img src='"+contents.image+"'>"))
			);
		}

		aceOfSpades.children("div.card").append($("<div class='card-contents'>").append(
				$("<p>").text(contents.stuff)
			)
		);

		if(typeof contents.actions !== 'undefined' && contents.actions.length > 0){
			var links = "";
			$.each(contents.actions,function(index,value){
				links += value;
			});
			aceOfSpades.children("div.card").append($("<div class='card-action'>").html(links));
		}
		return aceOfSpades;
	},
	youtube: function(video_url){ ////www.youtube.com/embed/OK5f1xkk3hU?autoplay=1&controls=0
		var rickroll = $('<div class="card col s12">')
				.append($('<div class="card-content">')
					.append($('<iframe width="100%" src="'+video_url+'" frameborder="0" allowfullscreen></iframe>')));
		return rickroll;
	}
}

$.fn.entertimevortex = function() {
    var time_to_jump = null;
    var i = 0;
    var thingy = $(this);
    clearInterval(time_to_jump);
    time_to_jump = setInterval(function(){
        if (i != -360) {
            i -= 1;
            thingy.css({
                MozTransform: 'rotate(-' + -i + 'deg)',
                WebkitTransform: 'rotate(' + -i + 'deg)',
                transform: 'rotate(' + -i + 'deg)'
            }).animate({left: '+=' + i + 'px'}, 40);
        }
    }, 10);    
}

