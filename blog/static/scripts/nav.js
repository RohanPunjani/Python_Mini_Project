$('document').ready(function(){
    $('.burger').click(function(){
        if($('.burger').attr("state") == "ham")
        {
            $('.burger').attr("state","cross");
            $('.black_nav').fadeIn()
            $('.bar').css(
                "background", "white"
            )
            $('outer_nav').css("background","#029e74")
            $('.outer_nav li a').css(
                "color", "white"
            )
            $('.floating_btn_container').fadeOut()
        }
        else if($('.burger').attr("state") == "cross")
        {
            $('.burger').attr("state","ham");
            $('.black_nav').fadeOut()
            $('.bar').css({
                "background": "#029e74",
            })
            $('outer_nav').css("background","white")
            $('.outer_nav li a').css(
                "color", "black"
            )
            $('.floating_btn_container').fadeIn()
        }
    })
    $('.black_nav').click(function(){
        $('.burger').attr("state","ham");
        $('.black_nav').fadeOut()
        $('.bar').css({
            "background": "#029e74",
        })
        $('outer_nav').css("background","white")
        $('.outer_nav li a').css(
            "color", "black"
        )
        $('.floating_btn_container').fadeIn()
    })
})

function confirm_delete(url){
    res = confirm("Are you sure you want to delete?")
    if (res){
        window.location.href = url;
    }
}