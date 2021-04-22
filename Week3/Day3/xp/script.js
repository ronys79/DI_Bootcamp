// exercise 1
let clickme = document.getElementsByTagName("button")[0];

clickme.onclick = function () {
    let start = Date.now();
    let timer = setInterval(function () {
        let timePassed = Date.now() - start;
        animate.style.left = timePassed / 5 + 'px';
        if (timePassed > 1746) clearInterval(timer);
    }, );
}

// // exercise 2
