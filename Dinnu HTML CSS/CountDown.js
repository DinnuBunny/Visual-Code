let year = document.getElementById("year");
let month = document.getElementById("month");
let day = document.getElementById("day");
let hour = document.getElementById("hour");
let startButtonEl = document.getElementById("startButton");

let y = "2000"
let m = "Feb"
let d = "28"
let h = "15"




// Set the date we're counting down to
let countDownDate = new Date("3 1, 2022 00:00:00").getTime();
console.log(countDownDate);
//console.log(dd);

function convertCountdownDate() {
    let yearValue = year.value;
    let monthValue = month.value;
    let dayValue = day.value;
    let hourValue = hour.value;

    let inputDate = `${monthValue} ${dayValue}, ${yearValue} ${hourValue}:00:00`;
    console.log(inputDate);
    var countDownDate = new Date(inputDate).getTime();

    startTheCountDown(countDownDate);


}





// Update the count down every 1 second
let timerId = "";

function startTheCountDown(countDownDate) {
    function printTheConutTime() {

        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        days = days + " days ";
        hours = hours + " hours ";
        minutes = minutes + " minutes ";
        seconds = seconds + " seconds";

        let countDownArray = [days, hours, minutes, seconds];
        let print = "";
        for (let value of countDownArray) {
            if (value[0] !== "0") {
                print += value;
            }
        }
        // Output the result in an element with id="demo"
        document.getElementById("demo").innerHTML = print; //days + "days " + hours + "h " + minutes + "m " + seconds + "s ";

        // If the count down is over, write some text 
        if (distance < 0) {
            clearInterval(timerId);
            document.getElementById("demo").innerHTML = "EXPIRED";
        }
    }
    timerId = setInterval(printTheConutTime, 1000);
    console.log("x", timerId);
}

//startTheCountDown(countDownDate);