"use strict";

$(document).ready(function () {

    let days = document.querySelector("#days"),
        hours = document.querySelector("#hours"),
        minutes = document.querySelector("#minutes"),
        seconds = document.querySelector("#seconds");

    let countDownDate = new Date(2019, 10, 13, 0, 0, 0);
    let millisecsPerDay = 86400000,
        millisecsPerHour = 3600000,
        millisecsPerMin = 60000;


    function changeCountDown() {

        let currentDate = new Date(),
            timeDifference = countDownDate - currentDate;

        let daysLeft = Math.floor(timeDifference / millisecsPerDay),
            hoursLeft = Math.floor((timeDifference - (daysLeft * millisecsPerDay)) / millisecsPerHour),
            minsLeft = Math.floor((timeDifference - (daysLeft * millisecsPerDay) - (hoursLeft * millisecsPerHour)) / millisecsPerMin),
            secsLeft = Math.floor((timeDifference - (daysLeft * millisecsPerDay) - (hoursLeft * millisecsPerHour) - (minsLeft * millisecsPerMin)) / 1000);
        days.textContent = String(daysLeft).padStart(2, "0");
        hours.textContent = String(hoursLeft).padStart(2, "0");
        minutes.textContent = String(minsLeft).padStart(2, "0");
        seconds.textContent = String(secsLeft).padStart(2, "0");
    };

    setInterval(changeCountDown, 1000);
})