(function () {
    $(document).ready(function(){
        $('#open-gallery').click(function() {
            $.get( "/gallery/", function(data) {
                $(".gallery-items").html(data["gallery_html_data"])
            });
        })
    });
})($);