let timerEl = document.getElementById("timer");
let startTimerEl = document.getElementById("startTimer");
let stopTimerEl = document.getElementById("stopTimer");
let milliSecondsEl = document.getElementById("milliSeconds");
let resetTimer = document.getElementById("resetTimer");


let UniqueId = null;
let UniqueId2 = null;
let counter = 0;
let counter1 = 0;
startTimerEl.onclick = function() {
    clearInterval(UniqueId);
    milliSecondsEl.textContent = "";
    timerEl.textContent = "";

    UniqueId = setInterval(function() {
        console.log(counter);
        counter = counter + 1;
        timerEl.textContent = counter;
    }, 60000);

    UniqueId2 = setInterval(function() {
        console.log(counter1);
        counter1 = counter1 + 1;
        milliSecondsEl.textContent = counter1;
        if (counter1 === 59) {
            counter1 = 0
        }
    }, 1000);
    startTimerEl.classList.add("d-none");
};

stopTimerEl.onclick = function() {
    clearInterval(UniqueId);
    clearInterval(UniqueId2);
    startTimerEl.classList.remove("d-none")
};

resetTimer.onclick = function() {
    counter1 = 0
    counter = 0
    milliSecondsEl.textContent = "";
    timerEl.textContent = "";



};