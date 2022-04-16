let fullPage = document.getElementById("fullPage");
let toogleEl = document.getElementById("toogleEl");
let onId = document.getElementById("onIdEl");
let offId = document.getElementById("offIdEl");

toogleEl.addEventListener("click", function() {
    onId.classList.toggle("hide");
    offId.classList.toggle("hide");
    toogleEl.classList.toggle("offf");
    fullPage.classList.toggle("off");
});