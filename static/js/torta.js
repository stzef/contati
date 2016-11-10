
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
  var valor = document.getElementById('hidden')
  var dos = parseInt(valor.value)
  console.log(valor);
  var valor1 = document.getElementById('hidden1')
  var dos1 = parseInt(valor1.value)
  var valor2 = document.getElementById('hidden2')
  var dos2 =  parseInt(valor2.value)
  console.log(dos, dos1, dos2);
  var data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'],
    ['Por hacer',     dos],
    ['En proceso',  dos1],
    ['Terminado', dos2],

  ]);
  var options = {
    title: 'My Daily Activities'
  };

  var chart = new google.visualization.PieChart(document.getElementById('piechart'));

  chart.draw(data, options);
}
