/* Exercise 1
1. Create a structured html file linked to a js file
2. Write a JS function that takes a parameter: myAge
3. Console.log the age of my mum and my dad (my mum is twice my age, and my dad is 1.2 the age of my mum)
4. Call the function
*/


// let sonAge = +prompt("How old are you?");
// function prAge(myAge){
    
//     let ageMam = sonAge*2;
//     let agePap = ageMam*1.2;
//     console.log('my mum is twice my age' +  ageMam + ', and my dad is 1.2 the age of my mum' + agePap);
//   }

// console.log(prAge)


// Exercise 2
// 1. Create a structured html file linked to a js file
// 2. Write a JS function that takes a parameter: myAge
// 3. Return the age of my mum (my mum is twice my age)
// 4. Call the function
// 5. Console.log the age of my mum

let sonAge = +prompt('How old are you?');
function prAge(myAge) {
    let ageMam = sonAge * 2;
    var agePap = Math.round(ageMam * 1.2);
    return('my mum is twice my age' +  ageMam + ', and my dad is 1.2 the age of my mum' + agePap);
  }

console.log(prAge)