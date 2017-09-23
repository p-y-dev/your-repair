(function () {
    $(document).ready(function(){
        let status_data_class = ".status-data";
        let phone_reg = /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/;
        let initials_id = "#initials";
        let phone_id = "#phone";

        $("#application-form").submit(function(event) {
            event.preventDefault();

            let initials = $(initials_id).val();
            let phone = $(phone_id).val();

            $(status_data_class).removeClass("red-text");
            $(status_data_class).removeClass("green-text");
            $(status_data_class).text("");

            if(initials === "" || phone === "" ) {
                $(status_data_class).addClass("red-text");
                $(status_data_class).text("Пожалуйста, заполните все поля");
                return
            }

            if(!phone_reg.test(phone)) {
                $(status_data_class).addClass("red-text");
                $(status_data_class).text("Введите корректный номер телефон");
                return
            }

            $(status_data_class).addClass("green-text");
            $(status_data_class).html("<i class='fa fa-refresh fa-spin fa-fw'></i>" + "&nbsp;Заявка отправляется");

            let get_data = "initials=" + initials + "&phone=" + phone;

            $.get({
                url: "/send_application?" + get_data,
                success: function (data) {
                    $(status_data_class).html("Заявка успешно отправлена, мы вам перезвоним");
                    $(initials_id).val("");
                    $(phone_id).val("");
                    console.log(data);
                },

                error: function () {
                    $(status_data_class).removeClass("green-text");
                    $(status_data_class).addClass("red-text");
                    $(status_data_class).html("Ошибка при отправке");
                },
            });
        });

        $(".modal-close-application").click(function() {
            $(initials_id).val("");
            $(phone_id).val("");
            $(status_data_class).removeClass("red-text");
            $(status_data_class).removeClass("green-text");
            $(status_data_class).text("");
        })
    });
})($);