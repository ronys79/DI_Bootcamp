// Excersice 1

let lastp = document.getElementsByTagName('p')[3];
lastp.parentElement.removeChild(lastp);

// Add an event listener which will change the background color of the h2 tag from the DOM when clicked on.

let firstH2 = document.getElementsByTagName('h2')[0];

function pain() {
    firstH2.style.backgroundColor = "magenta";
    
  } 
    firstH2.addEventListener("click", pain);

  // Set the font size of the h1 tag to a random pixel size between 0 to 100.(Check out this documentation)

  let firstH1 = document.getElementsByTagName('h1')[0];

  function dolores() {
      firstH1.style.fontSize = `${Math.floor(Math.random() * 101)}px`;
  }
  firstH1.addEventListener("click", dolores);

 // Add an event listener which will hide the h3 when it’s clicked on (use the display property).

 let firstH3 = document.getElementsByTagName('h3')[0];
 function hide() {
    firstH3.style.display = "none";
 }

 firstH3.addEventListener("click", hide);

 // Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
function getBold_items() {
  let bold = document.getElementById('strong');
  return bold
}

function paintIt() {
  let arr = getBold_items();
  for (let i of arr){
    i.style.color = color;
  }
}
function highlight() {
  paintIt("blue");
}

function return_normal() {
  paintIt("black");
}

 let p = document.querySelectorAll('p');
 p.addEventListener('mouseover', highlight);
 p.addEventListener('mouseout', return_normal);
// ----------   

//-----------------

// When the “Submit” button of the form is clicked:
// get the values of the input tags
// make sure that they are not empty,
// then append them to a HTML table, in the div, below the form.
// When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

// Excersice 2

// Create a function called highlight() that changes the color of all the bold text to blue.
// Create a function called return_normal() that changes the color of all the bold text back to black.
// Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), 
// and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

// function getBold_items() {
//   let bold = document.getElementsByTagName('strong');
//   return bold
// }

// function paintIt(color){
//   let arr = getBold_items();
//     for (let i of arr) {
//     i.style.color = color;
//   }
// }


// function highlight() {
//   paintIt("blue");
// }

// function return_normal() {
//   paintIt("black");
// }

//  let ps = document.querySelector('p');
 
//  ps.addEventListener('mouseover', highlight);
//  ps.addEventListener('mouseout', return_normal);

// ----------------------------------------------------------------
// Exercice 3 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:

// function volume_spr() {
//   let volume;
//   let radius = document.getElementById("radius").value;
//   radius = Math.abs(radius);
//   volume = (4/3)*Math.PI*Math.pow(radius, 3);
//   volume = volume.toFixed(4);
//   document.getElementById("volume").value = volume;
//   return false;
// }
 
// window.onload=document.getElementById("MyForm").onsubmit=volume_spr;

// function volume_sphere(){
//   let volume;
//   let radius = document.getElementById('radius').value;
//   radius = Math.abs(radius);
//   volume = (4/3)*Math.PI * Math.pow(radius, 3);
//   volume = volume.toFixed(4);
//   document.getElementById('volume').value = volume;
//   return false;
// }
// window.onload=document.getElementById('MyForm').onsubmit=volume_sphere;


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
storyDiv.innerHTML =("i dont know "+ noun + " what the hell " + adjective + " im doing " + person + " get me " 
+ verb + " out of here " + place);
};
libButton.addEventListener('click', libIt);