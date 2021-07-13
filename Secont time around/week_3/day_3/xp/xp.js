const container = document.getElementById('container');
const box = document.getElementById('box');
let position = 1;
let test = true;
let id;
// XP1 Excersive
function move() {
    clearInterval(id)
    id = setInterval(function () {
        box.style.left = position + 'px';
        box.style.top = position + 'px';
        if (test)
            position++;
        else
            position--;

        if (position >= 150)
            test = false
        else if (position <= 0)
            test = true;
    }, 10)
}

function stop() {
    clearInterval(id)
}

// XP2 : Drag & Drop

const fill = document.querySelector('.fill');
const empty = document.querySelector('.empty');


// Fill listeners
fill.addEventListener('dragstart', dragStart);
fill.addEventListener('dragend', dragEnd);
empty.addEventListener('dragover', dragOver);
empty.addEventListener('drop', dragDrop);


function dragStart(){
    this.className += ' hold';
    setTimeout(() => (this.className = 'invisible'), 0);
};

function dragOver(e) {
    e.preventDefault();
}

function dragEnd() {
    this.className = 'fill';
}

function dragDrop() {
    this.className = 'empty';
    this.append(fill);
  }

