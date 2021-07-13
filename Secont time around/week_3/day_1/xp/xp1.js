// Excersive 1
// In the <div> above, change the value of the id attribute from navBar to 
// socialNetworkNavigation, using the setAttribute method.
document.getElementById("navBar").setAttribute("id","socialNetworkNavigation");
// We are going to add a new <li> to the <ul>.

// Create element
let ul = document.getElementsByTagName("ul")[0];
let li = document.createElement("li");

li.innerHTML = '<a href="#">Logout</a>';
ul.appendChild(li);
// Show text element content
let firstChild = ul.firstElementChild.textContent;
let lastChild = ul.lastElementChild.textContent;
console.log("Text of first line item = " + firstChild);
console.log("Text of last line item = " + lastChild);



