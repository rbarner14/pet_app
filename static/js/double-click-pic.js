"use static";


function swapPic(){
    $("#double-click-pic").attr("src", "https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F38670528%2F108919755319%2F1%2Foriginal.jpg?auto=compress&s=32c728ebfab7bb7cab9cf42307962b37")
}

$("#double-click-pic").on('dblclick', swapPic)