"use strict";

function alertUser(response){
    alert(response.msg)
}

function handleRegistrationSubmit(evt){
    evt.preventDefault();

    let url = "/register.json"
    let formData = $("#registration-form").serialize()

    $.post(url, formData, alertUser)
}

$("#registration-form").on("submit", handleRegistrationSubmit);