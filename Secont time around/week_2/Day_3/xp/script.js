// Exercise 1 : Your Favorite Colors

// colors = ['blue', 'green', 'yellow', 'red'];
// suffixes = ["st", "nd", "rd", "th"];

// for (let i = 0; i < colors.length; i++) {
//     console.log(`My ${i + 1}${suffixes[i]} 's choice: ${colors[i]}`);
// }

// Exercise 2 : List Of People

// let people = ["Greg", "Mary", "Devon", "James"]
// people.shift();
// newName = "Jason";
// people.splice(2, 0, newName);
// console.log(people);
// people.push("Rony");
// console.log(people);

// for (i in people) {
//     console.log("Hi there " + people[i])
//     if (people[i] == newName) {
//         break;
//     }
// }

// let copyPeople = people.slice();
// // console.log(copyPeople)

// let ind1 = people.indexOf("Mary");
// let ind2 = people.indexOf("Foo");
// let finalAnswer = people.slice(-1)[0];
// console.log("This is the final: " + finalAnswer);

// Exercise 3 : Repeat The Question

// num = prompt("Say a number from 1 to 100, if smaller than 10 we stop asking!")

// while (num > 10) {
// 	num = prompt("Say a number from 1 to 10!");
//     console.log(typeof(num))
// }


// Exercise 4 : Attendance
// Prompt the student for their name :
// If the name is in the object, console.log the name of the student and the 
// country they come from.
// example: "Hi! I'm [name], and I'm from [country]."
// Hint: Look up the statement if ... in
// If the name is not in the object, console.log: "Hi! I'm a guest."


// let guestList = {
//     randy: "Germany",
//     karla: "France",
//     wendy: "Japan",
//     norman: "England",
//     sam: "Argentina"
//   }

//   userName = prompt("What is your name? ")

//   if (userName in guestList) {
//     console.log(`Hi! I'm ${userName} , and I'm from ${guestList[userName]}.`);
//     alert(`Hi! I'm ${userName}, and I'm from ${guestList[userName]}.`);
//     }
//     else {
//         console.log("Hi! I'm a guest.");
//         alert('Hi! you are a guest');
//     }

// Exercise 5 : Family

// let family = {
//     Father: "Papa",
//     Mother: "Mama",
//     Son: "trouble",
//     Daughter: "Sweetness",
// }

// for (people in family){
//     console.log(`This is the key ${people} , and this be the value: ${family[people]}`);
// }

// Exercise 6
// Given the object above, console.log “my name is Rudolf the raindeer”

// let details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }

// let x, str = "";
// for (x in details){
//     str += " " + x + " " + details[x];
// }
// console.log(str);

// Exercise 7 : Secret Group
// A group of friends have decided to start a secret society. 
// The society’s name will be the first letter of each of their names 
// sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society.


// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// orderedNames = names.sort();
// console.log(orderedNames)
// let firstChar = "";


// for (let index = 0; index < names.length; index++) {
//     const person = names[index];
//     // firstChar = `${firstChar}${person.charAt(0)}`; 
//     firstChar += person.charAt(0); 


    
// }
// console.log(`The name of the secret society is ${firstChar}.`)

