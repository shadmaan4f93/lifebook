(function($) {
    "use strict";
    $('input').addClass('input100');

    $('.input100').each(function() {
        $(this).on('blur', function() {
            if ($(this).val().trim() != "") {
                $(this).addClass('has-val');
            } else {
                $(this).removeClass('has-val');
            }
        })
    })
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit', function() {
        var check = true;

        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) == false) {
                showValidate(input[i]);
                check = false;
            }
        }
        return check;
    });
})(jQuery);

$('document').ready(function() {
    jQuery.validator.addMethod("password_check", function(value, element) {
        debugger
        if (/^[0-9]{8}$/.test(value)) {
            return false;
        } else {
            return true;
        };
    }, "Password must be length of 8 numbers and letters");

    $(".vaalidte-form").validate({

        rules: {
            first_name: {
                required: true
            },
            last_name: {
                required: true
            },
            password1: {
                required: true,
                minlength: 8,
                password_check: true
            },
            password2: {
                required: true,
                equalTo: "#id_password1"
            },
            username: {
                required: true,
                remote: {
                    url: "/api/get-username/",
                    type: "GET",
                    dataFilter: function(data) {
                        data = JSON.parse(data)
                        if (data.username[0]) {
                            return false
                        } else {
                            return true;
                        }
                    }
                }
            },
        },
        messages: {
            username: {
                remote: "the user is exist"
            },
        },
    });
});