let computerNumber = (Math.floor(Math.random() * 11))
let userNumber =(null)
let runCount = (4)
function numberInput (){var tnum = prompt("Enter a number between 1 and 10")
if (runCount==0){
    alert("out of chances")
}
else {
        if (isNaN(tnum)===true)
        {alert("Sorry Not a number")
        numberInput();}
        else if (tnum <0 || tnum>10)
        {alert("Sorry it's not a good number")
        numberInput();}
        else {var userNumber = tnum;
            runCount--
            console.log("runcount"+runCount)
        test(userNumber,computerNumber)}
        }
}
function playTheGame() {
  var confirmation = confirm("Are you sure you want to play the game?");
  if (confirmation === false) {
    alert("No problem, Goodbye");
  }
  else {numberInput();}
    }
  console.log(computerNumber)
  console.log(userNumber)
function test(userNumber,computerNumber) {
if (userNumber == computerNumber){
    alert("WINNER")
}
else if (userNumber > computerNumber){
   var userNumber= alert ("Your number is bigger then the computer's, guess again")
   numberInput();
}
else if (userNumber < computerNumber){
    var userNumber= alert ("Your number is smaller then the computer's, guess again")
    numberInput()
 }
}

// ----


// let computerNumber = (Math.floor(Math.random() * 11))
// let userNumber =(null)
// let runCount = (4)
// ​
// function numberInput (){var tnum = prompt("Enter a number between 1 and 10")
// ​
// if (runCount==0){
//     alert("out of chances")
// }
// else {
//         if (isNaN(tnum)===true)
//         {alert("Sorry Not a number, Goodbye")}
//         else if (tnum <0 || tnum>10)
//         {alert("Sorry it’s not a good number, Goodbye")}
//         else {var userNumber = tnum;
//             runCount++
//         test(userNumber,computerNumber)}
//         }
//         console.log("runcount"+runCount)
        
// }
// ​
// function playTheGame() {
//   var confirmation = confirm("Are you sure you want to play the game?");
//   if (confirmation === false) {
//     alert("No problem, Goodbye");
//   }
//   else {numberInput();}
// ​
//     }
//   console.log(computerNumber)
//   console.log(userNumber)
// ​
// ​
// function test(userNumber,computerNumber) {
// if (userNumber == computerNumber){
//     alert("WINNER")
// }
// else if (userNumber > computerNumber){
//    var userNumber= alert ("Your number is bigger then the computer’s, guess again")
//    numberInput();
// }
// else if (userNumber < computerNumber){
//     var userNumber= alert ("Your number is smaller then the computer’s, guess again")
//     numberInput()
//  }
// ​
// }