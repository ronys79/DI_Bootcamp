// // 1. The div node
let divnodes = document.getElementsByTagName('div');
console.log(divnodes);
// 1 alternative
let divnodes2 = document.querySelector('#container');

// 2. The ul nodes, and render all of it's children one by one
let ulnodes = document.getElementsByTagName('ul');
console.table([ulnodes[0].children[0].innerText, ulnodes[0].children[1].innerText, ulnodes[1].children[0].innerText, ulnodes[1].children[1].innerText])

for (i = 0; i < ulnodes.length; i++) {
    console.log("ulnodes[" + i + "] = ", ulnodes[i]);
    for (j = 0; j < ulnodes[i].children.length; j++) {
        console.log(i, j);
        console.log(ulnodes[i].children[j].innerText);
    };
};
// 3. The first li of each ul
let list0 = document.getElementsByClassName('list')[0];
let list1 = document.getElementsByClassName('list')[1];
console.table([list0.textContent, list1.textContent]);