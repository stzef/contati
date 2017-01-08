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
              var lista = data.lista
              lis= JSON.parse(lista);
              var proy = data.proye
              pro = JSON.parse(proy);
              console.log("jsonnnnnnproyecto",pro);
              var html = ""
              var template = ""
                    for (var i = 0; i < lis.length; i++) {
                      template =
                      '<div class="table-full-width">'+
                      '<table class="table" id="id_tabla"><tbody><tr>'+
                      '<td>::HORAS::</td>'+
                      '<td>::PROYECTO::</td>'+
                      '</td></tr></div></tbody></table>'+
                      '</div>'
                      template = template.replace("::HORAS::",pro[i]).replace("::PROYECTO::",lis[i])
                      //.replace(/\:\:idTarea\:\:/g,fields.pk)
                      html += template
                    $("#tabla_repo").html(html)
                    }
              }
          }
        );

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
