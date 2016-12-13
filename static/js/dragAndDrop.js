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
      var w = document.getElementById("proyecto").selectedIndex;
<<<<<<< HEAD
      console.log(w);
=======
      var x = document.getElementById("id_error1");
>>>>>>> a99ba8e3e119aef2abebeab05a4705536217c025
      if (w==0) {
        $("#id_error1").append("<p>*Selecione un proyecto</p>");
        var error = false
        return error;

      }else {
        ActividesProducto()
        var error = true
        if (entra==1){
          var pa = document.getElementById("id_kanban")
          var hijo = document.createElement("input");
          hijo.setAttribute("type", "hidden");
          hijo.setAttribute("name","states_kanban" );
          hijo.setAttribute("value",1);
          pa.appendChild(hijo);
<<<<<<< HEAD
          console.log(pa);
          return error;}
=======
          }
>>>>>>> a99ba8e3e119aef2abebeab05a4705536217c025
        if (entra==2){
          var pa = document.getElementById("id_kanban")
          var hijo = document.createElement("input");
          hijo.setAttribute("type", "hidden");
          hijo.setAttribute("name","states_kanban" );
          hijo.setAttribute("value",2);
          pa.appendChild(hijo);
<<<<<<< HEAD
          console.log(pa);
          return error;}
=======
          }
>>>>>>> a99ba8e3e119aef2abebeab05a4705536217c025
        if (entra==3){
          var pa = document.getElementById("id_kanban")
          var hijo = document.createElement("input");
          hijo.setAttribute("type", "hidden");
          hijo.setAttribute("name","states_kanban" );
          hijo.setAttribute("value",3);
          pa.appendChild(hijo);
<<<<<<< HEAD
          console.log(pa);
          return error;}
=======
          }
>>>>>>> a99ba8e3e119aef2abebeab05a4705536217c025
      }
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
//funcion cambia en la base de datos el estado kamban cuando la tarea cambia de sitio en el tablero
function edit_Kanban(des, pk) {
  states_kanban = des;
  id = pk;
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
  ev.target.appendChild(document.getElementById( datos));
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
// funcion
function actividad1(pro) {
<<<<<<< HEAD
  var pk = pro.value;
  console.log(pk);
  $.ajax({
=======
  $('#id_error1').empty();   //limpio id_error *seleccione proyecto
  var pk = pro.value;       //id proyecto seleccionado guardo en pk
  $.ajax({                                        //ajax pintar tareas del proyecto seleccionado
>>>>>>> a99ba8e3e119aef2abebeab05a4705536217c025
       url: '/view_task_board/'+pk,
       type: 'get',
       success : function(data){
         var html = ""
         var template = ""
         var color = data.col.fields.hexadecimal
         var avatar = data.imagen.fields.image_2
         data.por_hacer.forEach(task => {
         	template = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)" style="background-color: #::hexadecimal::">'+
         	    '<img class="avatar border-gray" src="/media/::fotoImagen::" width="7%" height="7% alt="foto">'+
         	    '<a class="pull-right" data-toggle="modal" href="#MyModalEdit"><i class="fa fa-pencil" aria-hidden="true"></i></a>'+
         	    '::descripcionTarea::'+
         	'</div>'

         	template = template.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.name_task).replace("::fotoImagen::",avatar).replace("::hexadecimal::",color)
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

           template1 = template1.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.name_task).replace("::fotoImagen::",avatar).replace("::hexadecimal::",color)
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
    $("#id_error").append("<p>*Debe selecionar una actividad</p>");
    return false;

  }else {
<<<<<<< HEAD
    $('#form_task').submit(function() {
     // Enviamos el formulario usando AJAX
     debugger
           $.ajax({
               type: 'POST',
               url: $(this).attr('action'),
               data: $(this).serialize(),
               // Mostramos un mensaje con la respuesta de PHP
               success: function(data) {
                   alert("guardo tarea")
               }
           })
           return false;
       });

  }
};
=======
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
>>>>>>> a99ba8e3e119aef2abebeab05a4705536217c025
