$('document').ready(function(){
    $('.burger').click(function(){
        if($('.burger').attr("state") == "ham")
        {
            $('.burger').attr("state","cross");
            $('.black_nav').fadeIn()
            $('.bar').css(
                "background", "white"
            )
            $('.outer_nav li a').css(
                "color", "white"
            )
        }
        else if($('.burger').attr("state") == "cross")
        {
            $('.burger').attr("state","ham");
            $('.black_nav').fadeOut()
            $('.bar').css({
                "background": "#c51263",
            })
            $('.outer_nav li a').css(
                "color", "black"
            )
        }
    })
    $('.black_nav').click(function(){
        $('.burger').attr("state","ham");
        $('.black_nav').fadeOut()
    })
})