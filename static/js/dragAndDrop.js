

function star(ev) {
  console.log(ev.target)
ev.dataTransfer.effectAllowed = 'move';
ev.dataTransfer.setData("text",ev.target.id);
ev.dataTransfer.setDragImage(ev.target,80,80);
}
debugger
var x
function myFunction() {
    x = document.getElementById("usr1");
    //console.log(x);
    //document.body.style.backgroundColor = "red";
}


function enter(ev) {
  return true;
}

function over(ev) {
  ev.preventDefault();
}

function drop(ev) {
  ev.preventDefault();
  var datos=ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById( datos));
  ev.stopPropagation();
}

function end(ev) {
ev.dataTransfer.clearData("text");
}
