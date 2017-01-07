function rango_fecha(inicio, fin){
  var ini = inicio;
  var fi = fin;
  console.log(ini);
  console.log(fi);
      $.ajax({
          type: 'POST',
          url: '/reportes/',
          data : { inicio : ini, fin : fi },
          success: function(data) {
              console.log(data);
          }
        });

}

function edit_Kanban(des, pk) {

  states_kanban = des;
  id = pk;
  console.log("states_kanban"+states_kanban);
  console.log("id"+id);
  //document.location.href = url;
        $.ajax({
            type: 'POST',
            url: 'board/'+pk+'/kanban/',
            data : { pos : des },
            success: function() {

            }
          });
}
