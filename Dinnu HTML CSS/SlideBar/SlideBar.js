let openIdEl = document.getElementById("openId");
let dashBoardContEl = document.getElementById("dashBoardCont");
let dashboardEL = document.getElementById("dashHead");
let homeEl = document.getElementById("home");
let downloadEl = document.getElementById("download");
let favoritesEl = document.getElementById("favorites");
let settings = document.getElementById("settings");
let nameEl = document.getElementById("name");
let closeIconEl = document.getElementById("closeIcon");
let openIconEL = document.getElementById("openIcon");

openIdEl.addEventListener("click", function() {
    openIconEL.classList.toggle("hide");
    closeIconEl.classList.toggle("hide");
    dashboardEL.classList.toggle("hide");
    homeEl.classList.toggle("hide");
    downloadEl.classList.toggle("hide");
    favoritesEl.classList.toggle("hide");
    settings.classList.toggle("hide");
    nameEl.classList.toggle("hide");
});