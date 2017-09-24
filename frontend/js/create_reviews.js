(function () {
    $(document).ready(function(){
        let status_data_class = ".status-initials-reviews";
        let initials_id = "#initials-reviews";
        let review_id = "#review";

        $("#reviews-form").submit(function(event) {
            event.preventDefault();

            let initials = $(initials_id).val();
            let review = $(review_id).val();

            $(status_data_class).removeClass("red-text");
            $(status_data_class).removeClass("green-text");
            $(status_data_class).text("");

            if(initials === "" || review === "" ) {
                $(status_data_class).addClass("red-text");
                $(status_data_class).text("Пожалуйста, заполните все поля");
                return
            }

            $(status_data_class).addClass("green-text");
            $(status_data_class).html("<i class='fa fa-refresh fa-spin fa-fw'></i>" + "&nbsp;Отзыв отправляется");

            let get_data = "initials=" + initials + "&review=" + review;

            $.get({
                url: "/reviews/create?" + get_data,
                success: function(data) {
                    $(status_data_class).html("Спасибо за Ваш отзыв, он будет опубликован после проверки модератором!");
                    $(initials_id).val("");
                    $(review_id).val("");
                },

                error: function () {
                    $(status_data_class).removeClass("green-text");
                    $(status_data_class).addClass("red-text");
                    $(status_data_class).html("Ошибка при отправке");
                },
            });
        });

        $(".modal-close-reviews").click(function() {
            $(initials_id).val("");
            $(review_id).val("");
            $(status_data_class).removeClass("red-text");
            $(status_data_class).removeClass("green-text");
            $(status_data_class).text("");
        })
    });
})($);