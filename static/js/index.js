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

    $('a.home').addClass('active');

    const $slideShow = $("#slideshow");

    const slideMessages = [

        `<div class="slideTextChild">
                    <h1 class=" text-white">
                        <span class="course-intro">COURSES IN</span><br>
                        <span id="course-name">CG ANIMATION</span>
                    </h1>
                    <p class="pb-3 pt-1 text-white paragraph" id="course-content">
                    This is just NOT the same old Animation industry that your older brother may have told you
                    about. The most advanced Software tools are now fully utilising the quantum leap in Computer 
                    Processing Power to...
                    </p>
                    <a href="courses/cg-animation" class="blue" id="course-link">
                        MORE DETAILS
                        <span class="pl-2">
                            <i class="fas fa-angle-double-right"></i>
                        </span>
                    </a>
        </div>`,

        `<div class="slideTextChild">
                    <h1 class=" text-white">
                        <span class="course-intro">COURSES IN</span><br>
                        <span id="course-name">FILM MAKING</span>
                    </h1>
                    <p class="pb-3 pt-1 text-white paragraph" id="course-content">
                    The Foundation module in VFX Academy gives student a thorough understanding the basics
                     of Film Making, Virtual Effects and Animation. This then advances into...
                    </p>
                    <a href="courses/film-making" class="blue" id="course-link">
                        MORE DETAILS
                        <span class="pl-2">
                            <i class="fas fa-angle-double-right"></i>
                        </span>
                    </a>
        </div>`,

        `<div class="slideTextChild">
                    <h1 class=" text-white">
                        <span class="course-intro">COURSES IN</span><br>
                        <span id="course-name">VISUAL EFFECTS</span>
                    </h1>
                    <p class="pb-3 pt-1 text-white paragraph" id="course-content">
                    This module focuses on teaching fundamental Compositing Techniques as well as Motion Graphics, using After
                    Effects. Down the lane, students are exposed to advanced Composting Skills in...
                    </p>
                    <a href="courses/visual-effects" class="blue" id="course-link">
                        MORE DETAILS
                        <span class="pl-2">
                            <i class="fas fa-angle-double-right"></i>
                        </span>
                    </a>
        </div>`,
    ];

    $slideShow.vegas({
        delay: 8000,
        preload: true,
        timer: false,
        shuffle: false,
        cover: true,
        firstTransition: "fade",
        firstTransitionDuration: 20,
        transition: "fade",
        transitionDuration: 4000,
        slides: [{
                src: "/static/img/get-the-best-of-cg-animation-from-vfx-academy.webp"
            },
            {
                src: "/static/img/best-film-making-school-in-nigeria.webp"
            },
            {
                src: "/static/img/visual-effect-ghost-rider.webp"
            },
        ],
        overlay: "/static/img/01.png",

        walk: function (index) {

            // $('#slideText').fadeOut(1500, function () {
            //     $('.slideTextChild').replaceWith(
            //         slideMessages[index]
            //     )
            // }).fadeIn(1500);

            $('.slideTextChild').replaceWith(
                slideMessages[index]
            );
        },
    });

    $('input, textarea').each(function () {
        $(this).focus(function () {
            $(this).prev().addClass("in-focus");
        });
    });

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

        var $full_name = $('.full-name'),
            $email = $(".email"),
            $phoneNum = $(".phone-number"),
            $message = $(".message");

        var clean_Fullname = userInputStripper($('.full-name').val()),
            clean_message = userInputStripper($('.message').val());
        $full_name.val(clean_Fullname);
        $message.val(clean_message);

        $(".error-handler").each(function () {
            var $this = $(this);
            writeInputErrorMessage($this);
        })

        var $allWarning = $(".inquiry-form").find(".warning");

        if (parseInt($allWarning.length) > 0) {
            $($html, $body).animate({
                scrollTop: $("fieldset:nth-of-type(1)").offset().top
            }, 1200, false);
        } else if (!isValidPhoneNumber($phoneNum.val())) {
            $phoneNum.after($("<span class='warning paragraph'>This contact number is invalid!</span> ").css("display", "inline-block"));
        } else if (!isValidEmail($email.val())) {
            $email.after($("<span class='warning paragraph'>This email is invalid!</span> ").css("display", "inline-block"));
        } else {
            $('.inquiry-form').unbind('submit').submit();
        }
    });
})