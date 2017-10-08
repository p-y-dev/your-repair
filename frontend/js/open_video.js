(function () {
    $(document).ready(function(){
        $('#open-video').click(function() {
            $.get( "/video/", function(data) {
                $(".video-items").html(data["video_html_data"])
            });
        });

        $('#close-video').click(function() {
           $(".video-items").html("<i class='fa fa-cog fa-spin fa-fw'></i>")
        });
    });
})($);