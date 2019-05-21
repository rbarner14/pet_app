"use strict";

let daytimeButton = document.querySelector("#daytime-button");
let nightimeButton = document.querySelector("#nightime-button");

$(daytimeButton).on("click", function(){
    $(".colorChange").css("background-color", "#FFFF99");
})

$(nightimeButton).on("click", function(){
    $(".colorChange").css("background-color", "#2F4F4F")
})

