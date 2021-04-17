// Create a structured HTML file linked to a JS file

// 1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, 
// and display a message to the screen.

// Sample Output: //"0 is even" //"1 is odd" //"2 is even"


// for (let i = 0; i < 16; i++) 
//     if ( i % 2 == 0) {
//     console.log(`${i} number is even`);
// } else {
//     console.log(`${i} number is odd`);
// }

// Exercise 2

1. Write a JavaScript for loop that will go through the variable names.

if the item is not a string, pass.
if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.
2. Write a JavaScript for loop that will go through the variable names

if the item is not a string, go out of the loop.
if the item is a string, display it.

let names = ["john", "sarah", 23, "Rudolf", 34];
for (let i of names) {
    if (Number.isInteger(i) == true) {
        continue;
    } else {
        let q = i[0];
        if (q === q.toUpperCase()) {
            console.log(i);
            continue
        } else {
            i = i.charAt(0).toUpperCase() + i.slice(1);
            console.log(i);
        }
    }
}