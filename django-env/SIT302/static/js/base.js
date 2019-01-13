window.onload=function(){
$(".footer_right_icon").hover(function(){
    $(this).addClass("match");
    //console.log('2');

    //I use is() function to judge which child of the parent element this object is
    if($(this).is($($('#footer_right').children().get(1))))
    	console.log(1);
        $(this).addClass("background1");
        //console.log(2);

    if($(this).is($($('#footer_right').children().get(2))))
    	//console.log(2);
    	$(this).addClass("background2");

    if($(this).is($($('#footer_right').children().get(3))))
    	$(this).addClass("background3");

    if($(this).is($($('#footer_right').children().get(4))))
    	$(this).addClass("background4");

    if($(this).is($($('#footer_right').children().get(5))))
    	$(this).addClass("background5");


});

$(".footer_right_icon").mouseleave(function() {
	$(".footer_right_icon").removeClass("match");
	$(".footer_right_icon").removeClass("background1");
	$(".footer_right_icon").removeClass("background2");
	$(".footer_right_icon").removeClass("background3");
	$(".footer_right_icon").removeClass("background4");
	$(".footer_right_icon").removeClass("background5");

});
}