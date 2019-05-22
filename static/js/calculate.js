"use strict";


$("#calculate").on("click", function(){
    let num = $("#number").val()
    let factorial = 1;
    let i = num;

    while(i > 0){
        factorial *= i
        i -= 1
    }

    $("#result").html(factorial)
})