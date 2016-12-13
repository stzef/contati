

function tareasPorProyecto(pro) {
  var pk = pro.value;
  console.log(pk);
  $.ajax({
       url: '/tareas_index/'+pk,
       type: 'get',
       success : function(data){
         var html = ""
         var template = ""
         var color = data.col.fields.hexadecimal
         var error = true
         console.log(avatar);
         data.por_hacer.forEach(task => {
         	template = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)" >'
         	    '::descripcionTarea::'+
         	'</div>'

         	template = template.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.description)
         	html += template
         })
         $("#1").html(html)
         var html1 = ""
         var template1 = ""
         data.en_proceso.forEach(task => {
           template1 = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)">'+
           		'::descripcionTarea::'+
           '</div>'

           template1 = template1.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.description)

           html1 += template1
         })
         $("#2").html(html1)
         var html2 = ""
         var template2 = ""
         data.terminado.forEach(task => {
           template2 = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)">'+

              '::descripcionTarea::'+
           '</div>'

           template2 = template2.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.description)
           html2 += template2
         })
         $("#3").html(html2)
       }
});
  return error;
};
