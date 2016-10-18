

function star(ev) {
  console.log(ev.target)
ev.dataTransfer.effectAllowed = 'move';
ev.dataTransfer.setData("text",ev.target.id);
ev.dataTransfer.setDragImage(ev.target,80,80);
}
var ids =0
function myFunction() {
    debugger
    var demos = $("#demos").val();
    ids += 1
    //console.log(ids);
    if (ids == 1) {
      var micapa = document.getElementById('pru');
      micapa.innerHTML= '<input type="text" class="form-control" id="ids" draggable="true" ondragstart="star(event)" ondragend="end(event)">';
      var mi = document.getElementById('ids');
      console.log(ids);
      document.getElementById("ids").value = demos;
    }
    if (ids == 2) {
      var micapa = document.getElementById('pru1');
      micapa.innerHTML= '<input type="text" class="form-control" id="2" draggable="true" ondragstart="star(event)" ondragend="end(event)">';
      var mi = document.getElementById('2');
      console.log("pruebas2"+ids);
      document.getElementById("2").value = demos;
    }

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
