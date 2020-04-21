"use strict";

$(document).ready(function () {
    let $mainNav = $("#mainNav"),
        $navTriggerBtn = $("#navTriggerBtn"),
        $mainNavWrapper = $(".mainNav-wrapper");

    $navTriggerBtn.click(function () {
        $mainNav.toggleClass("active");
        $mainNavWrapper.toggleClass("active");
    });
})