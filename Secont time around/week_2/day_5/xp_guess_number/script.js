function playTheGame() {
    if (confirm("Would you like to play a fun game! ")){
        let userNumber = +prompt("Enter a between 0-10: ")
        if (userNumber >=0 && userNumber <= 10){
            let randomNumber = Math.floor(Math.random() * 11) 
            numberCompare(userNumber,randomNumber);
        }else if (userNumber <= 0 || userNumber > 10){
            alert("Sorry it's not a good number.");
            playTheGame();
        }else{
            alert("Input a number only!!"); 
            playTheGame();
        }
    } else{
        alert("Why like this? dont want to play?");
        playTheGame();
    }
}

function numberCompare(userNumber, randomNumber){
    console.log(randomNumber)
    for (let i = 0; i <3 ; i++){
        if(userNumber == randomNumber){
            alert("Wow you are amazing at guessing, you won!")
            return;
        }else if(userNumber < randomNumber){
            alert("Your number is smaller then the computer's, guess again.");
        }else {
            alert("Your number is larger then the computer’s, guess again.");
        }
        if (i<2){
            userNumber = +prompt("Enter a new number: ");
        }
    }
    alert("Out of chances.");
    return;
}

