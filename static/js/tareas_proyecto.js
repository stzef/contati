

function seleccionTareas(seleccion) {
  var pk = seleccion.value;
  console.log(pk);
  $.ajax({
       url: '/tareas_index/'+pk,
       type: 'get',
       success : function(data){
          var tare = data.tareas
          console.log(tare);
         alert("retorna json")
}
});
};
