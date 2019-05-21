"use static";

function getRandomAdjective(response){

    $("#random-adjective").text(response)
}

$.get("/adjective", getRandomAdjective)