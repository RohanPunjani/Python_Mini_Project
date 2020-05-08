
$('document').ready(function(){
    $('.add_btn').click(function(){
        if($('.add_btn').attr("state") == "plus")
        {
            $('.add_btn').attr("state","cross");
            $('.white_layer').fadeIn()
            $('.floating_btn_container').css("transform","rotateZ(135deg)")
        }
        else if($('.add_btn').attr("state") == "cross")
        {
            $('.add_btn').attr("state","plus");
            $('.white_layer').fadeOut()
            $('.floating_btn_container').css("transform","rotateZ(0deg)")
        }
    })
    
    $('.white_layer').click(function(){
        $('.add_btn').attr("state","ham");
        $('.white_layer').fadeOut()
        $('.floating_btn_container').css("transform","rotateZ(0deg)")
    })
})