
function seleccionTareas(seleccion) {
  //debugger
  var pk = seleccion.value;
  console.log(pk);
  $.ajax({
       url: '/tareas_index/'+pk,
       type: 'get',
       success : function(data){
		var html = ""
        var template = ""
        data.por_hacer.forEach(fields =>{
        	template =
          '<div class="table-full-width">'+
          '<table class="table" id="id_tabla"><tbody><tr>'+
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

        var html3 = ""
        var template3 = ""
        data.en_proceso.forEach(fields =>{
          template3 =
          '<div class="table-full-width">'+
          '<table class="table" id="tabla"><tbody><tr><td>'+
          '<label class="checkbox"><span class="icons"><span class="first-icon fa fa-square-o"></span><span class="second-icon fa fa-check-square-o"></span></span>'+
          '<input type="checkbox" value="" data-toggle="checkbox"><label>'+
          '</td>'+
          '<td>::nombreTareas::</td><td class="td-actions text-right">'+
          '<a href="/tasks/::idTarea::/edit/" class="btn btn-info btn-simple btn-xs"> <i class="fa fa-edit"></i></a>'+
          '<a href="/tasks/::idTarea::/delete/" class="btn btn-danger btn-simple btn-xs"> <i class="fa fa-times"></i></a>'+
          '</td></tr></div></tbody></table>'+
          '</div>'

          template3 = template3.replace("::nombreTareas::",fields.fields.name_task)
          .replace(/\:\:idTarea\:\:/g,fields.pk)
          html3 += template3
          })
        $("#tabla").html(html3)

        var html1 = ""
        var template1 = ""
        var template = '<table class="table table-bordered table-hover table-striped"><thead><th>LISTA DE TAREAS</th><th>FUNCIONES</th><th>HECHO</th></thead>'
        data.tareas.forEach(fields =>{

          template1 =
          '<td>::nombreTarea::</td>'+
          '<td><a class="btn btn-primary" href="/tasks/::idTareas::/edit/">Editar</a>'+
          '<a class="btn btn-danger" href="/tasks/::idTareas::/delete/">Borrar</a>'+
          '<a class="btn btn-success" href="/tasks/::idTareas::/comment/">Respuestas</a></td>'+
          '<td>'+'<p class="text-center" style="font-size: 21px;"> <i class="fa fa-check" aria-hidden="true"></i> </p></td>'+
          '</table>'+
          '</tr>'+'</tbody>'


          template1 = template1.replace("::nombreTarea::",fields.fields.name_task)
          .replace(/\:\:idTareas\:\:/g,fields.pk)
          html1 += template1

          })

        $("#tarea").html(template + html1)

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
        })
        $("#activity").html(template + html2)


}
});
};

function seleccionresponsable(seleccion) {
  //var user = document.getElementById('usuario');
  debugger
  var pk = seleccion.value;
  console.log(pk);
  $.ajax({
       url: '/tasks_responsible/'+pk,
       type: 'get',
       success : function(data){
        var html = ""
        var template = ""
        data.tareas.forEach(fields =>{
          template =
          '<div class="table-full-width">'+
          '<table class="table" id="users"><tbody><tr><td>'+
          '<label class="checkbox"><span class="icons"><span class="first-icon fa fa-square-o"></span><span class="second-icon fa fa-check-square-o"></span></span>'+
          '<input type="checkbox" value="" data-toggle="checkbox"><label>'+
          '</td>'+
          '<td>::usuarioTareas::</td><td class="td-actions text-right">'+
          '<a href="/tasks/::idTarea::/edit/" class="btn btn-info btn-simple btn-xs"> <i class="fa fa-edit"></i></a>'+
          '<a href="/tasks/::idTarea::/delete/" class="btn btn-danger btn-simple btn-xs"> <i class="fa fa-times"></i></a>'+
          '</td></tr></div></tbody></table>'+
          '</div>'


          template = template.replace("::usuarioTareas::",fields.fields.name_task)
          .replace(/\:\:idTarea\:\:/g,fields.pk)
          html += template
          })
        $("#users").html(html)


}
});
};
