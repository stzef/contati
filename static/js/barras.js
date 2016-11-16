
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var valor = document.getElementById('hidden')
  var cap = parseInt(valor.value)
  console.log(valor);
  var valor1 = document.getElementById('hidden1')
  var pend = parseInt(valor1.value)
  var valor2 = document.getElementById('hidden2')
  var perm =  parseInt(valor2.value)
  var admin =3
  var com =4
  var sdes =5
  var ssop =6
  var ides =7
  var isop =8
  var pagw =9
  var odes =10
  var pla =11
  var mequ =12
  var psof =13

  var ptic =14
  var sapp =15
  var pers =16

  var data = google.visualization.arrayToDataTable([
    ['Task', 'Horas por mes'],
    ['Capacitacion',     cap],
    ['Pendiente',  pend],
    ['Permiso',  perm],
    ['Administrativo', admin],
    ['comercial', com],
    ['Siacol Web Desarrollo',     sdes],
    ['Siacol Web Soporte',  ssop],
    ['Infa++ Desarrollo', ides],
    ['Infa++ Soporte', isop],
    ['Paginas Web',  pagw],
    ['Oportunidadapp Desarrollo', odes],

    ['Placea', pla],
    ['Mtto Equipos',     mequ],
    ['Proyectos software',  psof],
    ['Pruebas Tics', ptic],
    ['Siacolapp', sapp],
    ['Personal', pers],

  ]);
  var options = {
    title: 'My Daily Activities'
  };

  var chart = new google.visualization.BarChart(document.getElementById('Barchart'));

  chart.draw(data, options);
}
