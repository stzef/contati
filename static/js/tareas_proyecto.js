

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
          console.warn(template)
         	html += template


          })

       	$("#id_tabla").html(html)
}
});
};  

function seleccionresponsable(seleccion) {
  var pk = seleccion.value;
  console.log(pk);
  $.ajax({
       url: '/tasks_ad/'+pk,
       type: 'get',
       success : function(data){
    var html = ""
        var template = ""
        data.tareas.forEach(fields =>{
          template = 
          '<table class="table" id="table">'+
          '<tbody>'+
          '<h3>tareas</h3>'+'<td><label class="checkbox"><input type="checkbox" value="" data-toggle="checkbox"></label>'+
          '</td>'+
          '<td>::Tareas::</td>'+
          '<td class="td-actions text-right">'+
          '<a href="/tasks/::idTarea::/edit/" class="btn btn-info btn-simple btn-xs"><i class="fa fa-edit"></i></a>'+
          '<a href="/tasks/::idTarea::/delete/" class="btn btn-danger btn-simple btn-xs"><i class="fa fa-times"></i></a>'+
          '</td>'+
          '</tr>'+
          '</tbody>'+
          '</table>'
       
          template = template.replace("::Tareas::",fields.fields.name_task)
          .replace(/\:\:idTarea\:\:/g,fields.pk)
          console.warn(template)
          html += template


          })

        $("#table").html(html)
}
});
};  


