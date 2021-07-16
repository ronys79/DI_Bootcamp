var cards = [];
// these values are link to unicode to display respectice icons on html
const suits = ["spades", "hearts", "clubs", "diams"];
const numb = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
var output = document.getElementById("output");

for (s in suits) {
    // get value of card suit
    var suit = suits[s][0].toUpperCase();
    // set background color for different cards
    var bgcolor = (suit == "S" || suit == "C") ? "black" : "red";
    for (n in numb) {
    //if card value is higher than 9 it is valued at 10 if lower then numeric value +1
    var cardValue = (n > 9) ? 10 : parseInt(n) + 1
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

console.log(cards);

function ranCard() {
  var randomNum = Math.floor((Math.random() * 52));
  output.innerHTML += "<span style='color:" + cards[randomNum].bgcolor + "'>&" + cards[randomNum].icon + ";" + cards[randomNum].cardnum + "</span>  ";
}
ranCard();