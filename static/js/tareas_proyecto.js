function seleccionTareas(pro) {
debugger
  var pk = pro.value;
  console.log(pk);
  $.ajax({
       url: '/view_task_board/'+pk,
       type: 'get',
       success : function(data){
