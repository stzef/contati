
function seleccionTareas(seleccion) {
  var pk = seleccion.value;
  console.log(pk);
  $.ajax({
       url: '/tareas_index/'+pk,
       type: 'get',
       success : function(data){
		var html = ""
        var template = ""
        data.tareas.forEach(fields =>{
        	template =
          '<div class="table-full-width">'+
          '<table class="table" id="id_tabla"><tbody><tr><td>'+
          '<label class="checkbox"><span class="icons"><span class="first-icon fa fa-square-o"></span><span class="second-icon fa fa-check-square-o"></span></span>'+
          '<input type="checkbox" value="" data-toggle="checkbox"><label>'+
          '</td>'+
          '<td>::nombreTareas::</td><td class="td-actions text-right">'+
          '<a href="/tasks/::idTarea::/edit/" class="btn btn-info btn-simple btn-xs"> <i class="fa fa-edit"></i></a>'+
          '<a href="/tasks/::idTarea::/delete/" class="btn btn-danger btn-simple btn-xs"> <i class="fa fa-times"></i></a>'+
          '</td></tr></div></tbody></table>'+
          '</div>'

          template = template.replace("::nombreTareas::",fields.fields.name_task)
          .replace(/\:\:idTarea\:\:/g,fields.pk)
         	html += template
          })
       	$("#id_tabla").html(html)

        var html1 = ""
        var template1 = ""
        var template = '<table class="table table-bordered table-hover table-striped"><thead><th>LISTA DE TAREAS</th><th>FUNCIONES</th></thead>'
        data.tareas.forEach(fields =>{
<<<<<<< HEAD
          template1 =


          '<table class="table table-bordered table-hover table-striped">'+
          '<thead>'+
          '<th>LISTA DE TAREAS</th><th>FUNCIONES</th>'+
          '</thead>'+
=======
          template1 = 
>>>>>>> eedef8dab9eca3f7dd71fcfb89f6ae10d4868c85
          '<td>::nombreTarea::</td>'+
          '<td><a class="btn btn-primary" href="/tasks/::idTareas::/edit/">Editar</a>'+
          '<a class="btn btn-danger" href="/tasks/::idTareas::/delete/">Borrar</a>'+
          '<a class="btn btn-success" href="/tasks/::idTareas::/comment/">Respuestas</a></td>'+
          '</table>'
<<<<<<< HEAD


=======
             
>>>>>>> eedef8dab9eca3f7dd71fcfb89f6ae10d4868c85
          template1 = template1.replace("::nombreTarea::",fields.fields.name_task)
          .replace(/\:\:idTareas\:\:/g,fields.pk)
          html1 += template1

          })

        $("#tarea").html(template + html1)

<<<<<<< HEAD
// function seleccionresponsable(seleccion) {
//   var pk = seleccion.value;
//   console.log(pk);
//   $.ajax({
//        url: '//'+pk,
//        type: 'get',
//        success : function(data){
//     var html = ""
//         var template = ""
//         data.tareas.forEach(fields =>{
//           template = 
//           '<table type="text" name="seleccion" onchange="seleccionresponsable(seleccion)" class="table" id="table">'+
//           '<tbody>'+
//           '<h3>tareas</h3>'+'<td><label class="checkbox"><input type="checkbox" value="" data-toggle="checkbox"></label>'+
//           '</td>'+
//           '<td>::Tareas::</td>'+
//           '<td class="td-actions text-right">'+
//           '<a href="/tasks/::idTarea::/edit/" class="btn btn-info btn-simple btn-xs"><i class="fa fa-edit"></i></a>'+
//           '<a href="/tasks/::idTarea::/delete/" class="btn btn-danger btn-simple btn-xs"><i class="fa fa-times"></i></a>'+
//           '</td>'+
//           '</tr>'+
//           '</tbody>'+
//           '</table>'
       
//           template = template.replace("::Tareas::",fields.fields.name_task)
//           .replace(/\:\:idTarea\:\:/g,fields.pk)
//           console.warn(template)
//           html += template

=======
        var html2 = ""
        var template2 = ""
        var template = '<table class="table table-bordered table-hover table-striped"><thead><th>LISTA DE TAREAS</th><th>FUNCIONES</th></thead>'
        data.actividades.forEach(fields =>{
          template2 = 
          '<tr>'+
          '<td>::nombreactividad::</td>'+
          '<td><a class="btn btn-primary" href="/tasks/::idTareas::/edit/">Editar</a>'+
          '<a class="btn btn-danger" href="/tasks/::idTareas::/delete/">Borrar</a>'+
          '</tr>'+
          '</table>'
             
          template2 = template2.replace("::nombreactividad::",fields.fields.activity)
          .replace(/\:\:idTareas\:\:/g,fields.pk)
          html2 += template2
>>>>>>> 10b37c7217b6613bb28b5f1ff10a85f0f29e76a7

//           })

<<<<<<< HEAD
//         $("#tabla").html(html)
// }
// });
// };  
=======
        $("#activity").html(template + html2)

}
});
<<<<<<< HEAD
};
=======
};  
>>>>>>> 10b37c7217b6613bb28b5f1ff10a85f0f29e76a7
>>>>>>> eedef8dab9eca3f7dd71fcfb89f6ae10d4868c85




// function seleccionresponsable(seleccion) {
//   var pk = seleccion.value;
//   console.log(pk);
//   $.ajax({
//        url: '/tasks_ad/'+pk,
//        type: 'get',
//        success : function(data){
//     var html = ""
//         var template = ""
//         data.tareas.forEach(fields =>{
//           template =
//           '<table type="text" name="seleccion" onchange="seleccionresponsable(seleccion)" class="table" id="table">'+
//           '<tbody>'+
//           '<h3>tareas</h3>'+'<td><label class="checkbox"><input type="checkbox" value="" data-toggle="checkbox"></label>'+
//           '</td>'+
//           '<td>::Tareas::</td>'+
//           '<td class="td-actions text-right">'+
//           '<a href="/tasks/::idTarea::/edit/" class="btn btn-info btn-simple btn-xs"><i class="fa fa-edit"></i></a>'+
//           '<a href="/tasks/::idTarea::/delete/" class="btn btn-danger btn-simple btn-xs"><i class="fa fa-times"></i></a>'+
//           '</td>'+
//           '</tr>'+
//           '</tbody>'+
//           '</table>'

//           template = template.replace("::Tareas::",fields.fields.name_task)
//           .replace(/\:\:idTarea\:\:/g,fields.pk)
//           console.warn(template)
//           html += template


//           })

//         $("#tabla").html(html)
// }
// });
// };
