// these values are link to unicode to display respectice icons on html
const suits = ["spades", "hearts", "clubs", "diams"];
const numb = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];


//  capture dealer + player cards
var cards = [];
var playerCard = [];
var dealerCard = [];

var cardCount = 0;
var myMoney = 100;
var endplay = false;

var message = document.getElementById('message');
var output = document.getElementById('output');
var dealerHolder = document.getElementById('dealerHolder');
var playerHolder = document.getElementById('playerHolder');
var pValue = document.getElementById('pValue');
var dValue = document.getElementById('dValue');
var dollarValue = document.getElementById('money');

document.getElementById('mybet').onchange = function() {
    if (this.value < 0) {
    this.value = 0;
    }
    if (this.value > myMoney) {
    this.value = myMoney;
    }
    blink(message.innerHTML = "Bet changed to $" + this.value)
}

for (s in suits) {
    // get value of card suit
    var suit = suits[s][0].toUpperCase();
    // set background color for different cards
    var bgcolor = (suit == "S" || suit == "C") ? "black" : "red";
    for (n in numb) {
    //if card value is higher than 9 it is valued at 10 if lower then numeric value +1
    var cardValue = (n > 9) ? 10 : parseInt(n) + 1;
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
    document.getElementById('start').style.display = 'none';
    // display total monetary value
    dollarValue.innerHTML = myMoney;
}

function dealNew() {
    dValue.innerHTML = " ";
    message.innerHTML = " "
    // clear out arrays+html holders when new deal
    playerCard = [];
    dealerCard = [];
    dealerHolder.innerHTML = "";
    playerHolder.innerHTML = "";

    // bets and money amount
    var betvalue = document.getElementById('mybet').value;
    
    // changesvalue of moneyAvailable on Html
    myMoney = myMoney - betvalue;
    document.getElementById('money').innerHTML = myMoney;
    
    // enable on new deal
    document.getElementById('output').style.visibility = 'visible';
    document.getElementById('myactions').style.visibility = 'visible';
    
    // disable on new deal
    document.getElementById('mybet').disabled = true;
    document.getElementById('maxbet').disabled = true;
    document.getElementById('btndeal').style.visibility = 'hidden';
    document.getElementById('maxbet').style.visibility = 'hidden';
    deal();
    
}

// if (myMoney <= 0){
//     alert("You are out of money")
//     // document.title = +prompt('Black Jack Game', document.title);
//     // myMoney = +prompt("Would you like to add more funds to play? ")
// }

function redeal() {
    cardCount++;
    if (cardCount > 40) {
        shuffleDeck(cards);
        cardCount = 0;
        blink(message.innerHTML = "New Shuffle!")
    }
}

function deal() {
    // card count reshuffle: loop to get 2 cards each per player
    for (dealtCard = 0; dealtCard < 2; dealtCard++) {
        dealerCard.push(cards[cardCount]);
        dealerHolder.innerHTML += cardOutput(cardCount, dealtCard);
        // hide dealers first cards
        if (dealtCard == 0) {
        dealerHolder.innerHTML += '<div id="cover" style="left:100px;"></div>';
        }
        redeal();
        playerCard.push(cards[cardCount]);
        playerHolder.innerHTML += cardOutput(cardCount, dealtCard);
        redeal();
    }
    var playervalue = checktotal(playerCard);
    if (playervalue == 21 && playerCard.length == 2) {
        endGame();
        document.getElementById('btndeal').style.visibility = 'visible';
    }
    pValue.innerHTML = playervalue;
}

//  returns cardCount value in generated html/css output depending on what the value is from (var card)
function cardOutput(n, dealtCard) {
    // position adjustable of first/second card
    var pos1stcard = 100;
    var pos2ndcard = 60;
    // var to change postion of card if not the first card(dealtCard=0)
    var hpos = (dealtCard > 0) ? dealtCard * pos2ndcard + pos1stcard : pos1stcard;
    return '<div class="icard ' + cards[n].icon + '" style="left:' + hpos + 'px;">  <div class="top-card suit">' + cards[n].cardnum + '<br></div>  <div class="content-card suit"></div>  <div class="bottom-card suit">' + cards[n].cardnum +
    '<br></div> </div>';
}

function maxbet() {
  document.getElementById('mybet').value = myMoney;
  alert("Max Bet: Bet changed to $" + myMoney)
}

function cardAction(userAction) {
    switch (userAction) {
      case 'hit':
        addPlayerCard(); // add new card to players hand
        break;
      case 'hold':
        endGame(); // playout and calculate
        break;
      case 'double':
        var betvalue = parseInt(document.getElementById('mybet').value);
        if ((myMoney - betvalue) < 0) {
          betvalue = betvalue + myMoney;
          myMoney = 0;
        } else {
          myMoney = myMoney - betvalue;
          betvalue = betvalue * 2;
        }
        document.getElementById('money').innerHTML = myMoney;
        document.getElementById('mybet').value = betvalue;
        addPlayerCard(); // add new card to players hand
        endGame(); // playout and calculate
        break;
      default:
        endGame(); // playout and calculate
    }
  }

function addPlayerCard() {
    playerCard.push(cards[cardCount]);
    playerHolder.innerHTML += cardOutput(cardCount, (playerCard.length - 1));
    redeal();
    var currentValue = checktotal(playerCard);
    pValue.innerHTML = currentValue;
    if (currentValue > 21) {
      alert("Busted! Dealer Wins!!")
      endGame();
    }
}

function endGame() {
    endplay = true;
    // shows dealers first card
    document.getElementById('cover').style.display = 'none';
    
    // hide/display option changes
    document.getElementById('myactions').style.visibility = 'hidden';
    document.getElementById('btndeal').style.visibility = 'visible';
    document.getElementById('mybet').disabled = false;
    document.getElementById('maxbet').disabled = false;
    document.getElementById('maxbet').style.visibility = 'visible';
    // show dealerCard
    var payoutJack = 1;
    var dealervalue = checktotal(dealerCard);
    dValue.innerHTML = dealervalue;
    
    // dealer plays till 17 or bust
    while (dealervalue < 17) {
        dealerCard.push(cards[cardCount]);
        dealerHolder.innerHTML += cardOutput(cardCount, (dealerCard.length - 1));
        redeal();
        dealervalue = checktotal(dealerCard);
        dValue.innerHTML = dealervalue;
    }

    //WHo won???
    var playervalue = checktotal(playerCard);
    if (playervalue == 21 && playerCard.length == 2) {
        document.getElementById('btndeal').style.visibility = 'visible'
        alert("Player Blackjack")
        payoutJack = 1.5;
    }

    var betvalue = parseInt(document.getElementById('mybet').value) * payoutJack;
    if ((playervalue < 22 && dealervalue < playervalue) || (dealervalue > 21 && playervalue < 22)) {
        alert('You WIN! You won $' + betvalue);
        myMoney = myMoney + (betvalue * 2);
    } else if (playervalue > 21) {
        alert('Dealer Wins! You lost $' + betvalue)
        broke()
    } else if (playervalue == dealervalue) {
        alert('PUSH:         Same Value as Dealer!');
        myMoney = myMoney + betvalue;
    } else {
        alert('Dealer Wins! You lost $' + betvalue);
        broke()
    }
    pValue.innerHTML = playervalue;
    dollarValue.innerHTML = myMoney;
}

function broke() {
    if (myMoney <= 0){
        myMoney= +prompt("You have NO money, add more funds below by typing in a number!")
    }
}


function checktotal(aceCheckerIndex) {
    var currentValue = 0;
    var aceAdjust = false;
    for (var i in aceCheckerIndex) {
        if (aceCheckerIndex[i].cardnum == 'A' && !aceAdjust) {
            aceAdjust = true;
            currentValue = currentValue + 10;
        }
        currentValue = currentValue + aceCheckerIndex[i].cardvalue;
    }
    
    if (aceAdjust && currentValue > 21) {
        currentValue = currentValue - 10;
    }
    return currentValue;
}

function shuffleDeck(cardDeck) {
    // loop through deck of cards iin reverse order till none left 
    // - shuffle start
    for (var i = cardDeck.length - 1; i > 0; i--) {
        // resort order of array randomly, every loop changes
        var j = Math.floor(Math.random() * (i + 1));
        // temp array value holder
        var temp = cardDeck[i];
        // recreate value of [i] so after starting loop a random value is assing every ++loop to [j]
        cardDeck[i] = cardDeck[j];
        // pick up value of [j] and assing temp value above of [i] 
        cardDeck[j] = temp;
        // -shuffle end
    }
    return cardDeck;
}

function outputCard() {
    // pick up and return first cards value to html using (var cardCount)
    output.innerHTML += "<span style='color:" + cards[cardCount].bgcolor + "'>" + cards[cardCount].cardnum + "&" + cards[cardCount].icon + ";</span>  ";
}

var ALERT_TITLE = "JavaScript Black Jack Game";
var ALERT_BUTTON_TEXT = "Ok";

if(document.getElementById) {
	window.alert = function(txt) {
		createCustomAlert(txt);
	}
}

function createCustomAlert(txt) {
	d = document;

	if(d.getElementById("modalContainer")) return;

	mObj = d.getElementsByTagName("body")[0].appendChild(d.createElement("div"));
	mObj.id = "modalContainer";
	mObj.style.height = d.documentElement.scrollHeight + "px";
	
	alertObj = mObj.appendChild(d.createElement("div"));
	alertObj.id = "alertBox";
	if(d.all && !window.opera) alertObj.style.top = document.documentElement.scrollTop + "px";
	alertObj.style.left = (d.documentElement.scrollWidth - alertObj.offsetWidth)/2 + "px";
	alertObj.style.visiblity="visible";

	h1 = alertObj.appendChild(d.createElement("h1"));
	h1.appendChild(d.createTextNode(ALERT_TITLE));

	msg = alertObj.appendChild(d.createElement("p"));
	//msg.appendChild(d.createTextNode(txt));
	msg.innerHTML = txt;

	btn = alertObj.appendChild(d.createElement("a"));
	btn.id = "closeBtn";
	btn.appendChild(d.createTextNode(ALERT_BUTTON_TEXT));
	btn.href = "#";
	btn.focus();
	btn.onclick = function() { removeCustomAlert();return false; }

	alertObj.style.display = "block";
	
}

function removeCustomAlert() {
	document.getElementsByTagName("body")[0].removeChild(document.getElementById("modalContainer"));
}
function ful(){
    alert('Alert this pages');
}

function blink() {
    var f = document.getElementById('message');
    setTimeout(function() {
       f.style.display = (f.style.display == 'none' ? '' : 'none');
        setTimeout(function() {
           f.style.display = (f.style.display == 'none' ? '' : 'none');
        }, 500);
    }, 500);
 }
