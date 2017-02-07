function rango_fecha(inicio, fin){
  var ini = inicio;
  var fi = fin;
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
                    console.info(data)
                    drawMaterial(eval(data.todos))
              }
          }
        );

}

function rango_fecha_actividad(inicio, fin){
  var ini = inicio;
  var fi = fin;
  console.log(ini);
  console.log(fi);
      $.ajax({
          type: 'POST',
          url: '/actividad_reporte/',
          data : { inicio : ini, fin : fi },
          success: function(data) {
              var activity = data.activity
              acti= JSON.parse(activity);
              var proyectos = data.proyectos
              proye = JSON.parse(proyectos);
              var horas = data.horas
              hor = JSON.parse(horas);
              //pro = JSON.parse(proy);
              var html1 = ""
              var template1 = ""
                    for (var i = 0; i < acti.length; i++) {
                      template1 =
                      '<div class="table-full-width">'+
                      '<table class="table" id="id_tabla"><tbody><tr>'+
                      '<td>::PROYECTO::</td>'+
                      '<td>::ACTIVIDADES::</td>'+
                      '<td>::HORAS::</td>'+
                      '</td></tr></div></tbody></table>'+
                      '</div>'
                      template1 = template1.replace("::HORAS::",hor[i]).replace("::PROYECTO::",proye[i]).replace("::ACTIVIDADES::",acti[i])
                      //.replace(/\:\:idTarea\:\:/g,fields.pk)
                      html1 += template1
                    $("#tabla_activiti").html(html1)

                    }
                    console.info(data)
                    drawBasic(eval(data.totalh))
              }
          }
        );

}

google.charts.load('current', {packages: ['corechart', 'bar']});
/*google.charts.setOnLoadCallback(drawMaterial);*/

function drawMaterial(rows) {
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Proyecto');
      data.addColumn('number', 'Horas');

      data.addRows(rows);

      var options = {
        title: 'Motivation and Energy Level Throughout the Day',
        hAxis: {
          title: 'Time of Day',
          format: 'number',
          viewWindow: {
            min: [7, 30, 0],
            max: [17, 30, 0]
          }
        },
        vAxis: {
          title: 'Rating (scale of 1-10)'
        }
      };

      var material = new google.charts.Bar(document.getElementById('barchart_values'));
      material.draw(data, options);
    }

    google.charts.load('current', {packages: ['corechart', 'bar']});
    /*google.charts.setOnLoadCallback(drawBasic);*/
    function drawBasic(rows) {

          var data = new google.visualization.DataTable();
          data.addColumn('string', 'Actividad');
          data.addColumn('number', 'Horas');

          data.addRows(rows);

          var options = {
            title: 'Actividades por programa',
            chartArea: {width: '50%'},
            hAxis: {
              title: 'Total horas',
              minValue: 0
            },
            vAxis: {
              title: 'actividades'
            }
          };

          var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

          chart.draw(data, options);
        }
