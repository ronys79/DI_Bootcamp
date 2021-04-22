// SetTimeout()

// function sayHi(phrase, who) {
//     alert( phrase + ', ' + who );
//   }
  
//   setTimeout(sayHi, 5000, "Hello", "John"); //  calls sayHi() after one second --> Hello, John



// Exercise 1
// Create a new HTML file

// Create a banner saying "The sales end in 10min ! " . Style the banner and make it visible to the user after 5 sec.

// setTimeout(function(){ alert("The sales end in 10min ! "); }, 5000);
// setInterval(function() { }, 5000);

// Exercise 2

  // Step 1. What element do we want to animate?
  var countdown = document.getElementById("countdown");
  // Step 2. What function will change it each time?
  var countItDown = function() {
    var currentTime = parseFloat(countdown.textContent);
    if (currentTime > 0) {
       countdown.textContent = currentTime - 1;   
    } else {
        window.clearInterval(timer);
        alert("You missed it!");
    }
    
  };
  // Step 3: Call that on an interval
  var timer = window.setInterval(countItDown, 1000);