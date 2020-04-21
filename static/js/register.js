"use strict";

import {
    userInputStripper,
    writeInputErrorMessage,
    removeInputErrorMessage,
    isValidPhoneNumber,
    isValidEmail,
} from "../js/functions.js";

let $html = $("html"),
    $body = $("body");

$(document).ready(function () {

    $('a.register').addClass('active');

    $(".error-handler").each(function () {
        $(this).blur(function () {
            var $this = $(this);
            writeInputErrorMessage($this);
        })
        $(this).focus(function () {
            var $this = $(this);
            removeInputErrorMessage($this);
        })
    })

    let $submitBtn = $(".submit-button");
    $submitBtn.click(function (e) {
        e.preventDefault();

        var $first_name = $('.first_name'),
            $last_name = $('.last_name'),
            $email = $(".email"),
            $phoneNum = $(".phone-number");

        var clean_Fname = userInputStripper($('.first_name').val()),
            clean_Lname = userInputStripper($('.last_name').val());
        $first_name.val(clean_Fname);
        $last_name.val(clean_Lname);

        $(".error-handler").each(function () {
            var $this = $(this);
            writeInputErrorMessage($this);
        })

        var $allWarning = $(".registration-form").find(".warning");

        if (parseInt($allWarning.length) > 0) {
            $($html, $body).animate({
                scrollTop: $("fieldset:nth-of-type(1)").offset().top
            }, 1200, false);
        } else if (!isValidPhoneNumber($phoneNum.val())) {
            $phoneNum.after($("<span class='warning paragraph'>This contact number is invalid!</span> ").css("display", "inline-block"));
        } else if (!isValidEmail($email.val())) {
            $email.after($("<span class='warning paragraph'>This email is invalid!</span> ").css("display", "inline-block"));
        } else {
            $('.registration-form').unbind('submit').submit();
        }
    });

})