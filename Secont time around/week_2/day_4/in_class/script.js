// Exercise 1
// 1. Create a structured html file linked to a js file
// 2. Write a JS function that takes a parameter: myAge
// 3. Console.log the age of my mum and my dad 
// (my mum is twice my age, and my dad is 1.2 the age of my mum)
// 4. Call the function

// function parentsAge(myAge) {
//   let momAge = myAge * 2;
//   let dadAge = myAge * 1.2;
//   console.log(`My fathers is ${Math.round(dadAge)} and my mother is ${momAge}`);
// }

// parentsAge(41)

// 1. Create a structured html file linked to a js file
// 2. Write a JS function that takes a parameter: myAge
// 3. Return the age of my mum (my mum is twice my age)
// 4. Call the function
// 5. Console.log the age of my mum


function parentsAge(myAge) {
  let momAge = myAge * 2;
  let dadAge = Math.round(myAge * 1.2);
  let answer = `My fathers is ${dadAge} and my mother is ${momAge}`
  return answer;
}

console.log(parentsAge(41))
