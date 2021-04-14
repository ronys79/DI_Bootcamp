/* Exercise 1 : Your Favorite Colors
Instructions
Create an array called colors where the value is a list of your favorite colors.
Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
Hint : create an array of suffixes to do the Bonus

----------------------------------
let colors = ['green', 'blue', 'red']

for (i in colors) {
    console.log(`My ${parseInt(i) + 1} color is ${colors[i]}`)
}

or

let counter = 1
for (color of colors) {
    console.log(`My ${counter} color is {color}`);
    counter++
}

for (let i = 0; i < 200; i++) {
    console.log(i);
}
----------------------------------
*/

/* Exercise 2 : List Of People
Instructions
Write code to remove “Greg” from the people array.
Write code to replace “James” to “Jason”.
Write code to add your name to the end of the people array.
Using a loop, iterate through the people array and console.log each person.
Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
Write code that console.logs Mary’s index. take a look at indexOf on google.
Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
Create a variable called last which value is the last element of the array.
Hint: What is the relationship between the index of the last element in the array and the length of the array?

----------------------------------------------------------------
let newName = ("Jason")
let people = ["Greg", "Mary", "Devon", "James"];
people.shift();

people.splice(2, 1, newName);

people.push("Rony");
console.log(people);
for (i in people) {
    console.log(`your name is ${people[i]}`);
    if (people[i] == newName) {
        break;
    }
}
for(let i =1; i< people.length; i++){
    if(i > 2){
        break;
    }
    console.log(people[i]);
}
people.splice(2, 1,);
let ind1 = people.indexOf("Mary");

let ind2 = people.indexOf("Foo");

let last = people.slice(-1)[0];
console.log(last);
------------------------------------
*/
/*
Exercise 3 : Repeat The Question
Instructions
Prompt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
Tip : Which while loop is more relevant for this situation?
Hint : Check the data type you receive from the prompt (ie. typeof method)

--------------------------------
let userResponse = 0;

while (userResponse < 10) {
    userResponse = prompt("If input <= 10 it stops");
}
--------------------------------
*/
/*

Exercise 4 : Attendance
Instructions
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}
Given the object above where the key is the students name and the value is the country they are from.

Prompt the student for their name :
If the name is in the object, console.log the name of the student and the country they come from.
example: "Hi! I'm [name], and I'm from [country]."
Hint: Look up the statement if ... in
If the name is not in the object, console.log: "Hi! I'm a guest."
*/

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}
let userName = prompt("Tell us your name?")

if (userName in guestList) {
console.log(`Hi! I'm ${userName} , and I'm from ${guestList[userName]}.`);
alert(`Hi! I'm ${userName}, and I'm from ${guestList[userName]}.`);
}
else {
    console.log("Hi! I'm a guest.");
    alert('Hi! you are a guest');
}
// Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Console.log the keys. (using a for loop).
// Console.log the values. (using a for loop).


// Exercise 6
// Instructions
// let details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }
// Given the object above, console.log “my name is Rudolf the raindeer”


// Exercise 7 : Secret Group
// Instructions
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society.
