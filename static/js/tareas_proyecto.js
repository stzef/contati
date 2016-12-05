function seleccionTareas(pro) {
  var pk = pro.value;
  console.log(pk);
  $.ajax({
       url: '/tareas_index/'+pk,
       type: 'get',
       success : function(data){
         var tar = data.tareas.fields
         console.log("-----------",tar);
         data,tareas.forEach(fields => {
          template = '<div type="text" name="pintar" id="::idTareas::" class="formasCss" draggable="true" ondragstart="star(event)" ondragend="end(event)" style="background-color: #::hexadecimal::">'+
              '<img class="avatar border-gray" src="/media/::fotoImagen::" width="7%" height="7% alt="foto">'+
              '<a class="pull-right" data-toggle="modal" href="#MyModalEdit"><i class="fa fa-pencil" aria-hidden="true"></i></a>'+
              '::descripcionTarea::'+
          '</div>'

          template = template.replace("::idTareas::",task.pk).replace("::descripcionTarea::",task.fields.description).replace("::fotoImagen::",avatar).replace("::hexadecimal::",color)
          html += template
       })
       $("#3").html(html2)
     }
   });
 }
