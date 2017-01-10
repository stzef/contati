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

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  debugger
  var proyec = document.getElementById("id_proye")
  console.log(proyec);
  var lista = document.getElementById("id_lista")
  console.log(lista);
  encabezado =  ["Element", "Horas por mes", { role: "style" } ]
  lista = [


  ]
  var data = google.visualization.arrayToDataTable(
    lista
  );

  var view = new google.visualization.DataView(data);
  view.setColumns([0, 1,
                   { calc: "stringify",
                     sourceColumn: 1,
                     type: "string",
                     role: "annotation" },
                   2]);

  var options = {
    title: "Informe de gestion",
    width: 400,
    height: 300,
    bar: {groupWidth: "95%"},
    legend: { position: "none" },
  };
  var chart = new google.visualization.BarChart(document.getElementById("barchart_values"));
  chart.draw(view, options);
}
