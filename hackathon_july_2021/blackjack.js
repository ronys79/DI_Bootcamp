// these values are link to unicode to display respectice icons on html
const suits = ["spades", "hearts", "clubs", "diams"];
const numb = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
var output = document.getElementById("output");

//  capture dealer + player cards
var cards = [];
var cardCount = 0;
var playerCard = [];
var dealerCard = [];
var dealerHolder = document.getElementById("dealerHolder");
var playerHolder = document.getElementById("playerHolder");

var moneyAvailable = 100;

var message = document.getElementById("message");

for (s in suits) {
    // get value of card suit
    var suit = suits[s][0].toUpperCase();
    // set background color for different cards
    var bgcolor = (suit == "S" || suit == "C") ? "black" : "red";
    for (n in numb) {
    //if card value is higher than 9 it is valued at 10 if lower then numeric value +1
    var cardValue = (n > 9) ? 10 : parseInt(n) + 1
    // capture card value that has been randomly generated
    var card = {
        suit: suit,
        icon: suits[s],
        bgcolor: bgcolor,
        cardnum: numb[n],
        cardvalue: cardValue
    }
        cards.push(card); 
  }
}

// function ranCard() {
//   var randomNum = Math.floor((Math.random() * 52));
//   output.innerHTML += "<span style='color:" + cards[randomNum].bgcolor + "'>&" + cards[randomNum].icon + ";" + cards[randomNum].cardnum + "</span>  ";
// }
// ranCard();

function Start() {
shuffleDeck(cards);
dealNew();
// start button not shown after click play
document.getElementById("start").style.display = "none";
// display total monetary value
document.getElementById("money").innerHTML = moneyAvailable;
}

function dealNew() {
    // clear out arrays+html holders when new deal
playerCard = [];
dealerCard = [];
dealerHolder.innerHTML = "";
playerHolder.innerHTML = "";

// bets and money amount
var betValue = document.getElementById("mybet").value;

// changesvalue of moneyAvailable on Html
moneyAvailable = moneyAvailable-betValue;
document.getElementById("money").innerHTML = moneyAvailable;

// enable on new deal
document.getElementById("myactions").style.display = "block";

// display to user current bet
message.innerHTML = "Reach 21 to win Blackjack or beat the dealer to take the pot!<br>Current bet is $"+betValue;

// disable on new deal
document.getElementById("mybet").disabled = true;
document.getElementById("maxbet").disabled = true;
deal()
}

function deal(){
    // loop to get 2 cards each per player
for (dealtCard = 0; dealtCard < 2; dealtCard++) {
    // dealers/players cards - capturing cards from array
    dealerCard.push(cards[cardCount]);
    dealerHolder.innerHTML += cardOutput(cardCount, dealtCard);
    // hide dealers first cards
    if (dealtCard == 0) {
        dealerHolder.innerHTML += '<div id="cover" style="left:100px;"></div>';
    }
    cardCount++
    playerCard.push(cards[cardCount]);
    playerHolder.innerHTML += cardOutput(cardCount, dealtCard);
    cardCount++
    }

}

//  returns cardCount value in generated html/css output depending on what the value is from (var card)
function cardOutput(n, dealtCard) {
    // position adjustable of first/second card
    var pos1stcard = 100;
    var pos2ndcard = 165;
    // var to change postion of card if not the first card(dealtCard=0)
    var hpos = (dealtCard > 0) ? dealtCard * pos2ndcard : pos1stcard;
    return '<div class="icard ' + cards[n].icon + '" style="left:' + hpos + 'px;">  <div class="top-card suit">' + cards[n].cardnum + '<br></div>  <div class="content-card suit"></div>  <div class="bottom-card suit">' + cards[n].cardnum +
    '<br></div> </div>';
}

function cardAction(userAction) {
    switch (userAction){
        case 'hit':
            addPlayerCard();
            break;
        case 'hold':
            playend(); // calculate and payout
            break;
        case 'double':
            // double current bet and remove value from moneyAvailable
            addPlayerCard();
            playend(); // calculate and payout
        default:
            console.log("default end game")
            playend(); // calculate and payout
    }
}

function addPlayerCard(){
    playerCard.push(cards[cardCount]);
    playerHolder.innerHTML += cardOutput(cardCount, (playerCard.lenght -1));
    cardCount++
}


function shuffleDeck(array) {
    // loop through deck of cards iin reverse order till none left 
    // - shuffle start
    for (var i = array.length - 1; i > 0; i--) {
        // resort order of array randomly, every loop changes
        var j = Math.floor(Math.random() * (i + 1));
        // temp array value holder
        var temp = array[i];
        // recreate value of [i] so after starting loop a random value is assing every ++loop to [j]
        array[i] = array[j];
        // pick up value of [j] and assing temp value above of [i] 
        array[j] = temp;
        // -shuffle end
    }
    // return value of array/cards to be used with function start(shuffleDeck(cards))
    return array;
}

function outputCard() {
    // pick up and return first cards value to html using (var cardCount)
    output.innerHTML += "<span style='color:" + cards[cardCount].bgcolor + "'>" + cards[cardCount].cardnum + "&" + cards[cardCount].icon + ";</span>  ";
}