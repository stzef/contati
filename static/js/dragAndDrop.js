

function star(ev) {
  //console.log(ev.target)
ev.dataTransfer.effectAllowed = 'move';
ev.dataTransfer.setData("text",ev.target.id);
ev.dataTransfer.setDragImage(ev.target,80,80);
}
var contador =0
/*function myFunction() {
    //debugger
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

}*/
function myFunction() {
    //debugger
    var demos = $("#demos").val();
    contador += 1
    //console.log(ids);
      var padre = document.getElementById('pru');
      var hijo = document.createElement("input");
      padre.appendChild(hijo);
      hijo.id ='ID'+contador;
      hijo.setAttribute("type", "text");
      hijo.setAttribute("class","form-control");
      hijo.setAttribute("draggable","true" );
      hijo.setAttribute( "ondragstart","star(event)");
      hijo.setAttribute("ondragend","end(event)");
      hijo.setAttribute("value",demos);
      //hijo.class= "form-control", hijo.id = 'id'+contador, hijo.type = 'text',  hijo. draggable="true", hijo.ondragstart="star(event)" ;
      //hijo.ondragend="end(event)";

      //console.log(padre2);
      //hijo.innerHTML= 'type="text" class="form-control" draggable="true" ondragstart="star(event)" ondragend="end(event)"';
      console.log(padre);

      /*nodoHijo.innerHTML= '<input type="text" class="form-control" id="ids" draggable="true" ondragstart="star(event)" ondragend="end(event)">';
      console.log(nodoHijo);
      nodoHijo.innerHTML = document.createElement("div");
      nodoHijo.id ='ID'+contador;
      console.log(nodoHijo);
      console.log(nodoHijo.id);
      id = nodoHijo.id
      console.log(id);
      nodoHijo.innerHTML= '<input type="text" class="form-control" id="ids" draggable="true" ondragstart="star(event)" ondragend="end(event)">';
      //var mi = document.getElementById('ids');
      var input = document.getElementById("this.id");
      console.log(input);*/
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
