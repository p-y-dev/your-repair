(function() {

    $(document).ready(function() {
        let item = "item";

        let fa_list = "fa-list";
        let fa_times = "fa-times";
        let menu_mobile = "menu-mobile";
        let item_mobile = "item-mobile";

        let none = "none";
        let active = "active";

        $('.' + fa_list).click(function(){
            $(this).addClass(none);
            $('.' + fa_times).removeClass(none);
            $('.' + menu_mobile).removeClass(none);
        });

        $('.' + fa_times).click(function(){
            $(this).addClass(none);
            $('.' + fa_list).removeClass(none);
            $('.' + menu_mobile).addClass(none);
        });

        $('.' + item_mobile).click(function(){
            $('.' + item_mobile).removeClass(active);
            $(this).addClass(active);
            $('.' + menu_mobile).addClass(none);
            $('.' + fa_times).addClass(none);
            $('.' + fa_list).removeClass(none);
        });

        $('.' + item).click(function(){
            $('.' + item).removeClass(active);
            $(this).addClass(active);
        });
    });
})($);