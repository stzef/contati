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
      var w = document.getElementById("proyecto").selectedIndex;
      console.log(w);
      if (w==0) {
        $("#id_error1").append("<p>*Selecione un proyecto</p>");
        var error = false
        return error;

      }else {
        ActividesProducto()
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
}
function edit_Kanban(des, pk) {
  states_kanban = des;
  id = pk;
  //url = '/projects/'+id;
  console.log("states_kanban"+states_kanban);
  console.log("id"+id);
  //document.location.href = url;
        $.ajax({
            type: 'POST',
            url: 'board/'+pk+'/edit/',
            data : { pos : des },
            success: function() {

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

function actividad1(pro) {
  var pk = pro.value;
  console.log(pk);
  $.ajax({
       url: '/view_task_board/'+pk,
       type: 'get',
       success : function(data){
         var html = ""
         var template = ""
         var color = data.col.fields.hexadecimal
         var avatar = data.imagen.fields.image_2
         var error = true
         console.log(avatar);
         data.por_hacer.forEach(task => {
         	template = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)" style="background-color: #::hexadecimal::">'+
         	    '<img class="avatar border-gray" src="/media/::fotoImagen::" width="7%" height="7% alt="foto">'+
         	    '<a class="pull-right" data-toggle="modal" href="#MyModalEdit"><i class="fa fa-pencil" aria-hidden="true"></i></a>'+
         	    '::descripcionTarea::'+
         	'</div>'

         	template = template.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.description).replace("::fotoImagen::",avatar).replace("::hexadecimal::",color)
         	html += template
         })
         $("#1").html(html)
         var html1 = ""
         var template1 = ""
         data.en_proceso.forEach(task => {
           template1 = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)" style="background-color: #::hexadecimal::">'+
               '<img class="avatar border-gray" src="/media/::fotoImagen::" width="7%" height="7% alt="foto">'+
               '<a class="pull-right" data-toggle="modal" href="#MyModalEdit"><i class="fa fa-pencil" aria-hidden="true"></i></a>'+
               '::descripcionTarea::'+
           '</div>'

           template1 = template1.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.description).replace("::fotoImagen::",avatar).replace("::hexadecimal::",color)
           html1 += template1
         })
         $("#2").html(html1)
         var html2 = ""
         var template2 = ""
         data.terminado.forEach(task => {
           template2 = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)"  style="background-color: #::hexadecimal::">'+
               '<img class="avatar border-gray" src="/media/::fotoImagen::" width="7%" height="7% alt="foto">'+
               '<a class="pull-right" data-toggle="modal" href="#MyModalEdit"><i class="fa fa-pencil" aria-hidden="true"></i></a>'+
               '::descripcionTarea::'+
           '</div>'

           template2 = template2.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.description).replace("::fotoImagen::",avatar).replace("::hexadecimal::",color)
           html2 += template2
         })
         $("#3").html(html2)
       }
});
  return error;
};
function ActividesProducto() {

  var pk = document.getElementById("proyecto").value;
  //var pk1 = pk.value
  console.log(pk);
  $.ajax({
       url: '/generaActividad/'+pk,
       type: 'GET',
       success : function(data){
                    console.info(data)
                    $("#id_actividad").append("option value='0'>-- Indica actividad --</option>");
                    for ( var i =0; i < data.length; i++){
                      $("#id_actividad").append("<option value='"+ data[i].pk +"'>"+data[i].fields.activity+"</option>");
                    }
       }
});
};

function validacion() {
  activi = document.getElementById('id_actividad').selectedIndex;
  console.log('activi',activi);
  if (activi==" ") {
    // Si no se cumple la condicion...
    $("#id_error").append("<p>*Debe selecionar una actividad</p>");
    return false;

  }
};
