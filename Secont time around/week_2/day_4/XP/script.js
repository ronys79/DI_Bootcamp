// // Exercise 1 : Information
// function infoAboutMe() {
//   console.log("My name is rony, age blah blah and more blah.")
// };

// infoAboutMe()

// // Part II

// function infoAboutPerson(personName, personAge, personFavoriteColor) {
//   console.log(`Your name is ${personName} you are ${personAge} old and yout favorite color is ${personFavoriteColor}`)
// };

// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

// Part III
// function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies) {
//   console.log(`Your name is ${personName} you are ${personAge} old and yout favorite color is ${personFavoriteColor} and their hobbies are ${personHobbies}`)
// };

// infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])

// Exercise 2 : Keyless Car

// let userAge = parseInt(prompt("How old are you my lovely? "))

// function checkDriverAge(userAge) {
//   if (userAge < 18) {
//     alert("Sorry, you are too young to drive this car. Powering off")
// } else if (userAge > 18) {
//   alert("You are old enough to drive, Powering On. Enjoy the ride!")
// } else {
//   alert("Congratulations on your first year of driving. Enjoy the ride!")
// }
// }

// checkDriverAge(userAge)

// Exercise 3: Odd Or Even

// function checkNumber(){
//   for (let i = 0; i < 101; i++) {
//     if (i % 2 == 0) {
//       console.log(`the number ${i} is even`);
//     } else {
//       console.log(`the number ${i} is odd`);
//     }
//   }
// };

// checkNumber()

// Exercise 4: Find The Numbers Divisible By 23
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.
// console.log("\n****** Week02 Day 04 - XP Exercise 4: Find The Numbers Divisible By 23 ******");
// let sum = 0
// let outcome = " "
// function isDivisible() {
//   for (let i = 0; i < 501; i++) {
//     if (i %23 ==0){
//       sum += i;
//       outcome += (i + " ")
//       // console.log(`${i} divisivle by 23`);
//     } 
//   } return sum, outcome
// }

// isDivisible()
// console.log("sum:" + sum)
// console.log("outcome:" + outcome)

// Exercise 5 : Amazon Shopping
// let the user know if the item is in the basket
// Hint: Use the in keyword inside the conditional
  
// console.log("\n****** Week02 Day 04 - XP Exercise 5 : Amazon Basket ******");

// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }

// function checkBasket(){ 
//   userItem = prompt("What item would you like? ").toLowerCase()
//     if (userItem in amazonBasket) {
//       alert("item in basket")
//     } else {
//       alert("item not in basket")
//     }
// }

// checkBasket(amazonBasket)

// Exercise 6 : What’s In My Wallet ?
// Instructions
// Given a item price and an array representing the amount of change in your pocket, determine 
// whether or not you can afford the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.05
// Pennies = 0.01
// To illustrate:
// changeEnough([25, 20, 5, 0], 4.25) should return true, since having 25 quarters, 20 dimes, 
// 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

// console.log("\n****** Week02 Day 04 - XP Exercise 6 : What’s In My Wallet ******");

// let coinValue = [0.25, 0.10, 0.05, 0.01];

// // Quarters  = 0.25
// // Dimes = 0.10
// // Nickels = 0.05
// // Pennies = 0.01

// function changeEnough(pocket, price){
// let i, totalChange = 0;
// for (i=0; i<pocket.length;i++) {
//     totalChange += (pocket[i]*coinValue[i]);
// }
// if (totalChange >= price){
//     console.log("You have enough change to buy your item.");
// }
// else{console.log("You don't have enough change to buy your item.");}
// }
// changeEnough([25, 20, 5, 0], 6.25);
// changeEnough([2, 100, 0, 0], 14.11);

// console.log("\n****** Week02 Day 04 - XP Exercise 7 : Shopping List ******");

// let shoppingList = ["banana", "orange", "apple"]

// let stock = { 
//   "banana": 6, 
//   "apple": 0,
//   "pear": 12,
//   "orange": 32,
//   "blueberry":1
// }  

// let prices = {    
//   "banana": 4, 
//   "apple": 2, 
//   "pear": 1,
//   "orange": 1.5,
//   "blueberry":10
// } 

// Create a function called myBill() that takes no parameters.
// The function should return the total price of your shoppingList. 
// In order to do this you must follow these rules:
// The item must be in stock.
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1

// functio myBill()