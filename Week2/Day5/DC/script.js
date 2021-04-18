// Instructions
// Have you heard the infamous song “99 Bottles of Beer?”
// In ths exercise you need to console.log the lyrics to the song 99 Bottles of Beer as an output.

// Prompt the user for a number to begin counting down bottles.
// In the song everytime a bottle falls we subtract the bottles by 1.
// What your code should do is:
// instead of subtracting by 1, everytime a bottle drops the subtracted number should go up by 1
// For example the first time a bottle drops we subtract by 1, the second time we subtract by 2 and so on.

var bottleCount = 0;
var bottlesLeft = +prompt("How many bottles left on the wall?");

function beersWall() {  
    for (i = bottlesLeft; bottlesLeft>=1; bottlesLeft-=bottleCount) {
        console.log(bottlesLeft + " bottles of beer on the wall")
        console.log(bottlesLeft + " bottles of beer")
        bottleCount++;
    } if (bottleCount>1) {
        console.log("Take" + bottleCount + "down, and pass THEM around")
        console.log(bottlesLeft + "bottles of beer on the wall")
} else if ( bottleCount === 1) {
        console.log("Take" + bottleCount + "down, and pass IT around")
        console.log(bottlesLeft + "bottles of beer on the wall")}
}
beersWall()


// var bottleCount = 0;
// var bottlesLeft = +prompt("How many bottles left on the wall?");

// function beersWall() {  
//     for (i = bottlesLeft; bottlesLeft>=1; bottlesLeft-=bottleCount) {
//         console.log(bottlesLeft + " bottles of beer on the wall")
//         bottleCount++;
//         if (bottleCount>1) {
//             console.log("Take" + bottleCount + "down, and pass THEM around")
//             console.log(bottlesLeft + "bottles of beer on the wall")
//     } else if ( bottleCount === 1) {
//     console.log("Take" + bottleCount + "down, and pass IT around")
//     console.log(bottlesLeft + "bottles of beer on the wall")}
// }
// }

// beersWall()