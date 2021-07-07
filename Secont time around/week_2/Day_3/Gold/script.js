// Exercise 1 : Building Management
// let building = {
//     numberLevels : 4,
//     numberOfAptByLevel : {
//         "1": 3,
//         "2": 4,
//         "3": 9,
//         "4": 2,
//     },
//     nameOfTenants : ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         "Sarah": [3, 990],
//         "Dan":  [4, 1000],
//         "David": [1, 500],
//     },
// }
// // Console.log the number of levels in the building.
// console.log(`Number of levels: ${building.numberLevels}`);
// // Console.log how many apartments are on levels 1 and 3.
// console.log(`How many apartments are on levels 1: ${building.numberOfAptByLevel[1]} and 3: ${building.numberOfAptByLevel[3] }`);
// // Console.log the name of the second tenant and the number of rooms he has in his apartment.
// console.log(`Name of tenant: ${building.nameOfTenants[1]}, Number of rooms: ${building.numberOfRoomsAndRent.Dan[0]}`);
// // Check if the sum of Sarah and David’s rent is bigger than Dan’s rent.
// // If it is than increase Dan’s rent.
// if ((building.numberOfRoomsAndRent.Sarah[1] + building.numberOfRoomsAndRent.David[1]) > building.numberOfRoomsAndRent.Dan[1]){
//     building.numberOfRoomsAndRent.Dan[1] += 100;
// }

// if (building.numberOfRoomsAndRent.Dan[1] > 1000) {
//     console.log(`Dan's new rent is: ${building.numberOfRoomsAndRent.Dan[1]}`)
// }

// Exercise 2 : Divisible By Three
// Loop through the array above and determine whether or not each 
// number is divisible by three.
// Each time you loop console.log “true” or “false”.

// let numbers = [123, 8409, 100053, 333333333, 7];
// divisible = [];
// nonDivisible = [];

// console.log(typeof(numbers))
// for (let index = 0; index < numbers.length; index++) {
//     if (numbers[index] % 3 == 0){
//         divisible.push(numbers[index])
//     } else {
//         nonDivisible.push(numbers[index])
//     }
// }

// console.log(`These numbers: (${divisible}) are divisible by 3`)
// console.log(`These numbers: (${nonDivisible}) are NOT divisible by 3`)

// Exercise 3 : Playing With Numbers
// 1. Console.log the sum of all the numbers in the age array.
// 2. Console.log the largest age in the array.

let age = [20,5,12,43,98,55];
let sum = 0
let largest = 0
for (x in age){
    sum += age[x]
}

for (x in age){
    if (age[x] > largest){
    largest = age[x];
}}
console.log(`Thw total sum is: ${sum}`)
console.log(`The largest age is: ${largest}`)