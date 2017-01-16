function myFunction(entra) {
  debugger
  var w = document.getElementById("proyecto").selectedIndex;
  if (w==0) {
    $('#id_error1').empty();   //limpio id_error *seleccione proyecto
    $("#id_error1").append("<p>*Selecione un proyecto</p>");
    modal = document.getElementById("ocultar");
          modal.style.display = "none";


  }else {
    ActividesProducto()
    modal1 = document.getElementById("ocultar");
    modal1.style.display = "";
    if (entra==1){
      var pa = document.getElementById("id_kanban")
      var hijo = document.createElement("input");
      hijo.setAttribute("type", "hidden");
      hijo.setAttribute("name","states_kanban" );
      hijo.setAttribute("value",1);
      pa.appendChild(hijo);
      }
    if (entra==2){
      var pa = document.getElementById("id_kanban")
      var hijo = document.createElement("input");
      hijo.setAttribute("type", "hidden");
      hijo.setAttribute("name","states_kanban" );
      hijo.setAttribute("value",2);
      pa.appendChild(hijo);
      }

    if (entra==3){
      var pa = document.getElementById("id_kanban")
      var hijo = document.createElement("input");
      hijo.setAttribute("type", "hidden");
      hijo.setAttribute("name","states_kanban" );
      hijo.setAttribute("value",3);
      pa.appendChild(hijo);
      }
}
}

//funcion cambia en la base de datos el estado kamban cuando la tarea cambia de sitio en el tablero
function edit_Kanban(des, pk) {

  states_kanban = des;
  id = pk;
  console.log("states_kanban"+states_kanban);
  console.log("id"+id);
  //document.location.href = url;
  debugger
        $.ajax({
            type: 'POST',
            url: 'board/'+pk+'/kanban/',
            data : { pos : des },
            success: function() {
              window.location = 'edit_board_task.html'
            }
          });
}

function edit_table(tarea){
  // debugger
  var pk = tarea;
  console.log(pk);
  // $('#edit_tablero').empty();
    $.ajax({
      type: 'GET',
            url: 'board/'+pk+'/edit/',
            dataType: 'json',
            success: function(data) {
              var name = data.tas.fields.name_task
              console.log(name)
              var des1 = '<input class="form-control" name="name_task" value="::name::" />'
              des1 = des1.replace("::name::", name)
              $("#nam").html(des1)

              var descrip = data.tas.fields.description
              console.log(descrip)
              var des = '::descrip::'
              des = des.replace("::descrip::", descrip)
              $("#di").html(des)

              var estime = data.tas.fields.estimated_time
              console.log(estime)
              var des2 = '<input class="form-control" name="name_task" value="::estime::" />'
              des2 = des2.replace("::estime::", estime)
              $("#estimate").html(des2)

              var totalt = data.tas.fields.total_time
              console.log(totalt)
              var des3 = '<input class="form-control" name="name_task" value="::totalt::" />'
              des3 = des3.replace("::totalt::", totalt)
              $("#totaltime").html(des3)

            //   var user = "<h1> user </h1>";
            //     // recorremos cada usuario
            //     $.forEach(data.tas.fields.responsible, function(key, value) {
            //         user += "<h2>Detalles del usuario " + value['ID'] + "</h2>";
            //         // recorremos los valores de cada usuario
            //         $.forEach(value, function(userkey, uservalue) {
            //             user += '<ul>';
            //             user += '<li>' + userkey + ': ' + uservalue + "</li>";
            //             user += '</ul>';
            //         })
            //     // Actualizamos el HTML del elemento con id="#respon"
            //     $("#respon").html(user);
            //
            // })
          }
    })

};

function answer_table(tarea){
  // debugger
  var pk = tarea;
  console.log(pk);
  $('#answer_tablero').submit(function() {
    $.ajax({
            url: 'board/'+pk+'/comment/add',
            data: $(this).serialize(),
            type: $(this).attr('method'),
            success: function() {
              alert("guardo respuesta")

          }
    })
    return false;
 })
};


// funcion para objetos arrastrables
function star(ev) {
  ev.dataTransfer.effectAllowed = 'move';
  ev.dataTransfer.setData("text",ev.target.id);
  ev.dataTransfer.setDragImage(ev.target,80,80);
}
// funcion para objetos arrastrables
function enter(ev) {
  return true;
}
// funcion para objetos arrastrables
function over(ev) {
  ev.preventDefault();
}
// funcion para objetos arrastrables
function drop(ev) {
  ev.preventDefault();
  var datos=ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById( datos));E
  var destino = ev.target.id
  console.log("destino: "+destino);
  console.log("objeto: "+datos);
  edit_Kanban(destino, datos)
  ev.stopPropagation();
}
// funcion para objetos arrastrables
function end(ev) {
ev.dataTransfer.clearData("text");
}
// funcion pinta solo las tareas del proyecto seleccionado
function actividad1(pro) {
  $('#id_error1').empty();   //limpio id_error *seleccione proyecto
  var pk = pro.value;       //id proyecto seleccionado guardo en pk
  $.ajax({                                        //ajax pintar tareas del proyecto seleccionado
       url: '/view_task_board/'+pk,
       type: 'get',
       success : function(data){
         var html = ""
         var template = ""
         var color = data.col.fields.hexadecimal
         var avatar = data.imagen.fields.image_2
         data.por_hacer.forEach(task => {
         	template = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)" style="background-color: #::hexadecimal::">'+
         	    '<img class="avatar border-gray" src="/media/::fotoImagen:: " width="7%" height="7%  alt="foto"> ' +
         	    '::descripcionTarea::'+
              '<a onclick="answer_table(::idTareas::)" class="pull-right" data-toggle="modal" href="#" data-target="#MyModalAnswer" title="respuesta" data-tooltip>'+
              '&nbsp;<i class="fa fa-commenting-o" aria-hidden="true"></i> '+
              '</a>'+
              '<a onclick="edit_table(::idTareas::)" class="pull-right" data-toggle="modal" href="#" data-target="#MyModalEdit" title="edit tarea" data-tooltip>'+
              '<i class="fa fa-pencil" aria-hidden="true"></i> '+
              '</a>'+
         	'</div>'

         	template = template.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.name_task).replace("::fotoImagen::",avatar).replace("::hexadecimal::",color)
         	html += template
         })
         $("#1").html(html)
         var html1 = ""
         var template1 = ""
         data.en_proceso.forEach(task => {
           template1 = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)" style="background-color: #::hexadecimal::">'+
               '<img class="avatar border-gray" src="/media/::fotoImagen::" width="7%" height="7% alt="foto"> '+
               '::descripcionTarea::'+
               '<a onclick="answer_table(::idTareas::)" class="pull-right" data-toggle="modal" href="#" data-target="#MyModalAnswer" title="respuesta" data-tooltip>'+
               '&nbsp;<i class="fa fa-commenting-o" aria-hidden="true"></i> '+
               '</a>'+
               '<a onclick="edit_table(::idTareas::)" class="pull-right" data-toggle="modal" href="#" data-target="#MyModalEdit" title="edit tarea" data-tooltip>'+
               '<i class="fa fa-pencil" aria-hidden="true"></i> '+
               '</a>'+
           '</div>'

           template1 = template1.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.name_task).replace("::fotoImagen::",avatar).replace("::hexadecimal::",color)
           html1 += template1
         })
         $("#2").html(html1)
         var html2 = ""
         var template2 = ""
         data.terminado.forEach(task => {
           template2 = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)"  style="background-color: #::hexadecimal::">'+
               '<img class="avatar border-gray" src="/media/::fotoImagen::" width="7%" height="7% alt="foto"> '+
               '::descripcionTarea::'+
               '<a onclick="answer_table(::idTareas::)" class="pull-right" data-toggle="modal" href="#" data-target="#MyModalAnswer" title="respuesta" data-tooltip>'+
               '&nbsp;<i class="fa fa-commenting-o" aria-hidden="true"></i> '+
               '</a>'+
               '<a onclick="edit_table(::idTareas::)" class="pull-right" data-toggle="modal" href="#" data-target="#MyModalEdit" title="edit tarea" data-tooltip>'+
               '<i class="fa fa-pencil" aria-hidden="true"></i> '+
               '</a>'+
           '</div>'

           template2 = template2.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.name_task).replace("::fotoImagen::",avatar).replace("::hexadecimal::",color)
           html2 += template2
         })
         $("#3").html(html2)
       }
});
};
//funcion valida si es seleccionada una actividad antes de guardar una tarea
function validacion() {
  activi = document.getElementById('id_actividad').selectedIndex;
  console.log('activi',activi);
  if (activi==" ") {
    // Si no se cumple la condicion...
    $('#id_sinactivi').empty();   //limpio id_error *seleccione actividad
    $("#id_sinactivi").append("<p>*Debe selecionar una actividad</p>");
    return false;

  }else {

    $(document).ready(function() {
     $('#form_task').submit(function() { // toma el formulario para enviarlo por ajax
         $.ajax({ // create an AJAX call...
             data: $(this).serialize(), // serializa el formulario
             type: $(this).attr('method'), // toma el metodo que tiene el formulario en add_board
             url: $(this).attr(action), // toma la url que tiene el formulario en add_board en action
             success: function() {
                alert("guardo tarea")
             }
         });
         return false;
     });
 });
  };
}
function aviso_valida(){
  $('#id_sinactivi').empty();   //limpio id_error *seleccione actividad
}

//funcion deriva de mifuntion aqui pinta las actividades dependiendo del producto seleccionado
function ActividesProducto() {
  $('#id_actividad').empty();     //limpio select actividades para que no se sumen con las nuevas
  $('#id_actividad').append('<option value="0">-- Seleccina una actividad --</option>')
  var pk = document.getElementById("proyecto").value;
  $.ajax({
       url: '/generaActividad/'+pk,
       type: 'GET',
       success : function(data){
                    $("#id_actividad").append("option value='0'>-- Indica actividad --</option>");
                    for ( var i =0; i < data.length; i++){
                      $("#id_actividad").append("<option value='"+ data[i].pk +"'>"+data[i].fields.activity+"</option>");
                    }
       }
});
};
