
$('document').ready(function(){
    $('.add_btn').click(function(){
        if($('.add_btn').attr("state") == "plus")
        {
            $('.floating_btn_container').css("transform","rotateZ(225deg)")
            $('.white_layer').fadeIn()
            $('.add_btn').attr("state","cross");
            $('.form_container').fadeIn()
        }
        else if($('.add_btn').attr("state") == "cross")
        {
            $('.form_container').fadeOut()
            $('.add_btn').attr("state","plus");
            $('.floating_btn_container').css("transform","rotateZ(0deg)")
            $('.white_layer').fadeOut()
        }
    })
    
    $('.white_layer').click(function(){
        $('.form_container').fadeOut()
        $('.add_btn').attr("state","plus");
        $('.white_layer').fadeOut()
        $('.floating_btn_container').css("transform","rotateZ(0deg)")
    })

    $("#upload_trigger").click(function(){
        $("#upload_image").click();
     });
})