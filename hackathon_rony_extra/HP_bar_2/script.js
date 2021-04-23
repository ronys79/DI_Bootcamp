health = document.getElementById('health'); 

// var for loosing health
const loseHp = document.getElementById('loseHp');

// var if we want to give and extra life that adds health
// const addHp = document.getElementById('addHp'); 

// This is the event listener, it is setup to link event from html by clicking button - we switch the eventL once we have it 
// set to get wrong question
loseHp.addEventListener('click', () => { health.value -= 1; va()});
// addHp.addEventListener('click', () => { health.value += 1; va()});

//update value div when this function called

// function va() {
// document.getElementById('val').innerHTML = health.value;
// }

// //show value div when page loaded

// va()