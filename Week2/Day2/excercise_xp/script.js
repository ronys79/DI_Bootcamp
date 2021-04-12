/* Exercise 1: Simple If/Else Statement

Instructions:
Create 2 variables, x and y. Each of them should have a different numeric value.
Write an if/else statement that checks which number is bigger.

--------------------------------------------------------------------------- 
let x = 5;
let y = 2;

if (x > y) {
    console.log("x is bigger")
} 

else {
    console.log("x is not bigger")
}
----------------------------------------------------------------------------------------------
*/

/*
Exercise 2: Chihuahua

Instructions: 

1. Create a variable called newDog where it’s value is “Chihuahua”. - Done
2. Check and display how many letters are in newDog. - Done
3. Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
4. Check if the variable newDog is equal to “Chihuahua”
     - if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
     - else, console.log ‘I dont care, I prefer cats’

--------------------------------------------------------------------------- 

let newDog = 'Chihuahua';
console.log(newDog, 'has', newDog.length, 'letters!');
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog === 'Chihuahua') {
console.log('I love Chihuahuas, it’s my favorite dog breed')
}

else {
    console.log("I dont care, I prefer cats")
}

----------------------------------------------------------------------------------------------
*/

/* Exercise 3: Even Or Odd
Instructions:
1. Prompt the user for a number and save it to a variable.
2. Check whether the variable is even or odd.
        - If it is even, display: “x is an even number”. Where x is the actual number the user chose.
        - If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
        
----------------------------------------------------------------------------------------------

let userNumber = +prompt("Enter a numer below:");
if (input % 2 === 0) {
    console.log(input + " is even");
} else if (input % 2 === 1) {
    console.log(input + " is odd");
} else {
    console.log("This is not a number!")
};
----------------------------------------------------------------------------------------------

*/

/* Exercise 4 : Switch Case - Guess the answers to the questions!

let whatHappens;
let direction = (fo);
direction = forward;

switch (direction) {
    case "forward":
        break;
        whatHappens = "you encounter a monster";
    case "back":
        whatHappens = "you arrived home";
        break;
        break;
    case "right":
        whatHappens = "you found a river";
        break;
    case "left":
        break;
        whatHappens = "you run into a troll";
        break;
    default:
        whatHappens = "please enter a valid direction";
}

----------------------------------------------------------------------------------------------
Q1: What is the value of the whatHappens variable, when the value of the direction variable is “forward”
    A1: undefined
Q2: What is the value of the whatHappens variable, when the value of the direction variable is “back”
    A2: you arrived home
Q3: What is the value of the whatHappens variable, when the value of the direction variable is “right”
    A3: you found a river
Q4: What is the value of the whatHappens variable, when the value of the direction variable is “left”
    A4: you run into a troll
----------------------------------------------------------------------------------------------

*/

/* Exercise 5: Group Chat - I am not sure about this one, worked with shy and Yair to solve it, without them I am not 100% on this

1. Using the array above, console.log the number of users in a group chat based on the following rules:
    - If there is no users (the users array is empty), console.log “no one is online”.
    - If there is 1 user, console.log “<name_user> is online”.
    - If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
    - If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
For example, if there are 5 users, it should display: name_user1, name_user2 and 3 more are online
s
*/
/*
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

let NoUsers = users.length;

switch (NoUsers) {
    case 0:
        console.log("no one is online");
        break;
    case 1:
        console.log(users[0] + " is online");
        break;
    case 2:
        console.log(users[0] + " and " + users[1] + " are online");
        break
    default:
        console.log(users[0] + ", " + users[1] + "and " + (NoUsers - 2) + " are online");
}
*/
