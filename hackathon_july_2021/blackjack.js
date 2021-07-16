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





// console.log(cards);

// function ranCard() {
//   var randomNum = Math.floor((Math.random() * 52));
//   output.innerHTML += "<span style='color:" + cards[randomNum].bgcolor + "'>&" + cards[randomNum].icon + ";" + cards[randomNum].cardnum + "</span>  ";
// }
// ranCard();

function Start() {
shuffleDeck(cards);
dealNew();

}

function dealNew() {
    // clear out arrays+html holders when new deal
playerCard = [];
dealerCard = [];
dealerHolder.innerHTML = "";
playerHolder.innerHTML = "";
// loop to get 2 cards each per player
for (x = 0; x < 2; x++) {
    // dealers/players cards - capturing cards from array
    dealerCard.push(cards[cardCount]);
    dealerHolder.innerHTML += cardOutput(cardCount);
    cardCount++
    playerCard.push(cards[cardCount]);
    playerHolder.innerHTML += cardOutput(cardCount);
    cardCount++
}
console.log(dealerCard);
console.log(playerCard);

}

//  returns cardCount value in generated html/css output deping on what the card is
function cardOutput(n) {
    return "<span style='color:" + cards[cardCount].bgcolor + "'>" + cards[cardCount].cardnum + "&" + cards[cardCount].icon + ";</span>  "
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