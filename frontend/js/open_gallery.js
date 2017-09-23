(function () {
    $(document).ready(function(){
        $('#open-gallery').click(function() {
            $.get( "/get_galleries", function(data) {
                $(".gallery-items").html(data["gallery_html_data"])
            });
        })
    });
})($);