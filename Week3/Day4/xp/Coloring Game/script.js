
let mainContainer= document.getElementById("mainContainer");

for(i=0; i<=3059; i++){
    let square = document.createElement("div");
    square.setAttribute("class","square");
    mainContainer.appendChild(square);
}

// How does a user choose a color?
// How does drawing work? How can you tell when the user is clicking and dragging?
// Hint, look at the JS events mousedown, mouseup, and mouseover.

let colorCurrent = "pink";
let area = document.getElementsByClassName('area');
for (col of area) {
    col.addEventListener("click", function(){
        colorCurrent =this.style.backgroundColor;
    })
};

let pixels = document.getElementsByClassName('square')
for (paint of pixels) {
    paint.addEventListener("mouseover", function(){
        this.style.backgroundColor = colorCurrent;
    })
};

let clear_button = document.getElementsByTagName("button")[0];
clear_button.addEventListener("mousedown", function(){
    for (clear_block of pixels){
        clear_block.style.backgroundColor = "white";
    }
});



// ------------------------------ Element: 
//// src= mousedown event https://developer.mozilla.org/en-US/docs/Web/API/Element/mousedown_event

// // When true, moving the mouse draws on the canvas
// let isDrawing = false;
// let x = 0;
// let y = 0;

// const myPics = document.getElementById('myPics');
// const context = myPics.getContext('2d');

// // event.offsetX, event.offsetY gives the (x,y) offset from the edge of the canvas.

// // Add the event listeners for mousedown, mousemove, and mouseup
// myPics.addEventListener('mousedown', e => {
//   x = e.offsetX;
//   y = e.offsetY;
//   isDrawing = true;
// });

// myPics.addEventListener('mousemove', e => {
//   if (isDrawing === true) {
//     drawLine(context, x, y, e.offsetX, e.offsetY);
//     x = e.offsetX;
//     y = e.offsetY;
//   }
// });

// window.addEventListener('mouseup', e => {
//   if (isDrawing === true) {
//     drawLine(context, x, y, e.offsetX, e.offsetY);
//     x = 0;
//     y = 0;
//     isDrawing = false;
//   }
// });

// function drawLine(context, x1, y1, x2, y2) {
//   context.beginPath();
//   context.strokeStyle = 'black';
//   context.lineWidth = 1;
//   context.moveTo(x1, y1);
//   context.lineTo(x2, y2);
//   context.stroke();
//   context.closePath();
// }

// -------------------------------- chaim's code --------------------------------

// let color = null;
// let mousedown = false;

// let body = document.getElementsByTagName("body")[0];
// let color_blocks = document.querySelectorAll("#sidebar > *");
// let fill_blocks = document.querySelectorAll("#main > *");
// let clear_button = document.getElementsByTagName("button")[0];

// clear_button.addEventListener("click", function(){
//     for (fill_block of fill_blocks){
//         fill_block.style.backgroundColor = "white";
//     }
// });

// body.addEventListener("mousedown", function(){
//     mousedown = true;
// })

// body.addEventListener("mouseup", function(){
//     mousedown = false;
// })


// for (color_block of color_blocks){
//     color_block.addEventListener("click", function(event){
//         color = event.target.style.backgroundColor;
//     });
// }

// for (fill_block of fill_blocks){
//     fill_block.addEventListener("mousedown", function(event){
//         if (color != null) event.target.style.backgroundColor = color;
//     });
//     fill_block.addEventListener("mouseover", function(event){
//         if (mousedown && color != null) event.target.style.backgroundColor = color;
//     });
// }
