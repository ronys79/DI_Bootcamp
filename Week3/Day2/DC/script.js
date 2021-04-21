// 1. Get the value of each of the inputs in the HTML file when the button is clicked.
// 2. Make sure the values are not empty
// 3. Write a story that uses each of the values.
// 4. Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently 
// displayed (but keep the values entered by the user). The user could click the button at least three times and 
// get a new story. Display the stories randomly.

var libButton = document.getElementById('lib-button');
var libIt = function() {
var storyDiv = document.getElementById("story");
var noun = document.getElementById('noun').value;
var adjective = document.getElementById('adjective').value;
var person = document.getElementById('person').value;
var verb = document.getElementById('verb').value;
var place = document.getElementById('place').value;

let abort = false;
for (item of document.getElementsByTagName('input')) {
    if (item.value.length === 0) {
        item.style.borderColor = "tomato";
        abort = true;
    } else {
        item.style.borderColor = "fuchsia"
    };
};
if (abort) { return; };
storyDiv.innerHTML =("i dont know "+ noun + " what the hell " + adjective + " im doing " + person + " get me " 
+ verb + " out of here " + place);
};
libButton.addEventListener('click', libIt);