/* Exercise 1
Create a structured HTML file linked to a JS file

1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, and display a message to the screen.

Sample Output: //"0 is even" //"1 is odd" //"2 is even"

for ( let x = 0; x<=15; x++ ){
    if ( x === 0 ) {
        console.log(x + 'is even')
    }
    else if (x % 2 === 0) {
        console.log (x + 'is even')
    }
    else {
        console.log (x + ' is odd')
    }
}
*/ 

/* Exercise 2

let names= ["john", "sarah", 23, "Rudolf",34]
1. Write a JavaScript for loop that will go through the variable names.

if the item is not a string, pass.
if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.
2. Write a JavaScript for loop that will go through the variable names

if the item is not a string, go out of the loop.
if the item is a string, display it.
*/

let names= ["john", "sarah", 23, "Rudolf",34]
for (x in names)
    
        if (typeof(names[x]) === 'string'){
            continue;
        }
         if (typeof names[x] === 'string'){
             if (names[x][0].toUpperCase)
            console.log(names[x]);
            // firstLetter = firstLetter.toUpperCase();
            names = names.charAt(0).toUpperCase() + names.slice(1);
            console.log(newname);
        }
        const capitalized = names.charAt(0).toUpperCase() + names.slice(1);
        
// for (x in names) {
//     if (typeof(names[x]) capitalizeFirstLetter {
//         console.log(names[x])

//         function initialIsCapital(names[x]){
//             return word[0] !== word[0].toLowerCase();
//           }
//     }

//     // converting first letter to uppercase
//     const capitalized = names.charAt(0).toUpperCase() + names.slice(1);

//     return capitalized;
