//function myFunction() {
  //  debugger
    //  var padre = document.getElementById('date.states_kanban1');
      //var hijo = document.createElement("input");
//      padre.appendChild(hijo);
  //    hijo.setAttribute("type", "hidden");
    //  hijo.setAttribute("name","states_kanban" );
      //hijo.setAttribute("value",3);

  //    console.log(padre);
  //  }
    function myFunction(entra) {
        debugger
        if (entra==1){
          var pa = document.getElementById("states_kanban1")
          var hijo = document.createElement("input");
          hijo.setAttribute("type", "hidden");
          hijo.setAttribute("name","states_kanban" );
          hijo.setAttribute("value",1);
          pa.appendChild(hijo);
          console.log(pa);}
        if (entra==2){
          var pa = document.getElementById("states_kanban1")
          var hijo = document.createElement("input");
          hijo.setAttribute("type", "hidden");
          hijo.setAttribute("name","states_kanban" );
          hijo.setAttribute("value",2);
          pa.appendChild(hijo);
          console.log(pa);}
        if (entra==3){
          var pa = document.getElementById("states_kanban1")
          var hijo = document.createElement("input");
          hijo.setAttribute("type", "hidden");
          hijo.setAttribute("name","states_kanban" );
          hijo.setAttribute("value",3);
          pa.appendChild(hijo);
          console.log(pa);}
}
function edit_Kanban(des, pk) {
  debugger
  states_kanban = des;
  id = pk;
  //url = '/projects/'+id;
  console.log("states_kanban"+states_kanban);
  console.log("id"+id);
  //document.location.href = url;
        $.ajax({
            type: 'POST',
            url: '/board/'+pk/edit,
            success: function() {
                alert('Object deleted!')
            }
          });
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
  edit_Kanban(destino, datos)
  ev.stopPropagation();
}

function end(ev) {
ev.dataTransfer.clearData("text");
}
