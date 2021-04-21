// Exercise 1
// let divE = document.getElementsByTagName('div')[0]
// divE.setAttribute('id', 'socialNetworkNavigation');
// var node = document.createElement("li");                 // Create a <li> node
// var textnode = document.createTextNode('<a href="#">Logout</a>');         // Create a text node
// node.appendChild(textnode);                              // Append the text to <li>
// let ul = document.getElementsByTagName("ul")[0]
// ul.appendChild(node);    

// var bonus1 = document.getElementById("navBar").lastChild.innerHTML;
// var bonus2 = document.getElementById("navBAr").firstChild.innerHTML;

// Exercise 2 : Users
// Instructions

// Change each first name of the two <ul>'s to your name.
// At the end of each <ul> add a <li> that says “Hey students”.
// Delete the name Sarah from the second <ul>.
// Bonus
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

// var lis = document.getElementsByTagName('li')


// document.getElementsByClassName('list')[0].lastElementChild.innerText = "Richard";
// let uls = document.getElementsByClassName('list');
// let addli = document.createElement('li');
// addli.innerText = "Hey Students";

// for (i = 0; i < uls.length; i++) {
// uls[i].firstElementChild.innerText = "Rony";
// let addli = document.createElement('li');
// addli.innerText = "Hey Students"
// };

// Exercise 3 : Users And Style
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” 
// (x and y are the users in the div).

document.getElementsByTagName('div')[0].style.backgroundColor = 'lightblue';
document.getElementsByTagName('div')[0].style.padding = "50px 10px 20px 30px";
document.getElementsByTagName('li')[0].style.display = "none"
document.getElementsByTagName('li')[1].style.border ="10px solid"
document.body.style.fontSize = "x-large";