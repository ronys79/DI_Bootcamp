
// --------------- JAVASCRIPT ANIMATION --------------------

function allowDrop(event) {
    event.preventDefault(); // Necessary. Allows us to drop.
  }
  
  //add dashes
  function allowEnter(event) {
    event.target.classList.add('over');
  }
  
  //remove dashes
  function allowLeave(event) {
    event.target.classList.remove('over');
  }
  
  function dragStart(event) {
  //set the data to be dragged
  console.log("target:",  event.target)
  console.log("id: ",  event.target.id ) // id: square1
  event.dataTransfer.setData("text", event.target.id);
  }
  
  function dragDrop(event) {
  // console.log("event.target:",event.target) 
  // "event.target:" "<div id='square3' ondrop='dragDrop(event)' ondragover='allowDrop(event)'>square3</div>"
  event.preventDefault();
  // retrieve the data dragged
    
  let data = event.dataTransfer.getData("text");
  console.log("data: ",  data) //data: square1 
    
  let box = document.getElementById(data)
  event.target.appendChild(box);
  }
  
  // Only JS
  
  // let square1 = document.getElementById("square1")
  // let square3 = document.getElementById("square3")
  
  // square1.addEventListener("dragstart", dragStart)
  
  // function dragStart(event){
  //   event.dataTransfer.setData("text", event.target.id);
  // }
  
  // ///END OF SQUARE 1////
  
  // ///BEGINNING OF SQUARE 1///
  // square3.addEventListener("dragover", dragOver)
  // square3.addEventListener("drop", drop)
  // square3.addEventListener("dragenter", dragEnter)
  // square3.addEventListener("dragleave", dragLeave)
  
  // //1st step of drop target
  // function dragOver(event){
  //   event.preventDefault();
  // }
  
  // function drop(event) {
  //   event.preventDefault();
  //   let dataSquare = event.dataTransfer.getData("text");
  //   let box = document.getElementById(dataSquare)
  //   event.target.appendChild(box);
  // }
  
  // function dragEnter(event){
  //   // event.target.style.backgroundColor = "green"
  //    event.target.classList.add('over');
  // }
  
  // function dragLeave(event){
  //   // event.target.style.backgroundColor = "lightblue"
  //   event.target.classList.remove('over');
  // }