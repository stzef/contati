var contador =0
function myFunction() {
    debugger
      var padre = document.getElementById('States_kanban1');
      var hijo = document.createElement("input");
      padre.appendChild(hijo);
      hijo.setAttribute("type", "hidden");
      hijo.setAttribute("name","states_kanban" );
      hijo.setAttribute("value",3);

      console.log(padre);
    }
function mi_funcion() {
  debugger
  var tarea = document.getElementsByName("pintar");
  console.log(tarea);

  //var padre = document.getElementById('pru');
  //var hijo = document.createElement("input");
  //padre.appendChild(hijo);
}

function star(ev) {
  ev.dataTransfer.effectAllowed = 'move';
  ev.dataTransfer.setData("text",ev.target.id);
  ev.dataTransfer.setDragImage(ev.target,80,80);
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
  var destino = ev.target.id
  console.log("destino: "+destino);
  console.log("objeto: "+datos);
  ev.stopPropagation();
}

function end(ev) {
ev.dataTransfer.clearData("text");
}
