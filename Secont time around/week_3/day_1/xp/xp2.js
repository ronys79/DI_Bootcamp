// In the HTML above change the name “Pete” to “Richard”.
let arr_list = document.querySelectorAll('.list');
console.log(arr_list[0])
arr_list[0].lastElementChild.innerText = "Richard";

// // Change each first name of the two <ul>'s to your name.
// // At the end of each <ul> add a <li> that says “Hey students”.

let listNames = document.getElementsByClassName('list');
let addMe = document.createElement("li");
addMe.innerText = "Hey students";

for (i = 0; i < listNames.length; i++) {
    listNames[i].firstElementChild.innerText ="Rony";
    let addMe = document.createElement("li");
    addMe.innerText = "Hey students";
    listNames[i].appendChild(addMe);
};

// // Delete the name Sarah from the second <ul>.

arr_list[1].firstElementChild.nextElementSibling.remove()

// Bonus
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.
let ul1 = document.querySelector("ul");
ul1.setAttribute('class','student_list university attendance');


