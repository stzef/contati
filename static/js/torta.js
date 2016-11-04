google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart(a,b,c) {
    //debugger
    var pa = document.getElementById("hidden")
    console.log(pa);
    var por = 2
    var en = 11
    var ter = 4
  var data = google.visualization.arrayToDataTable([

    ['Task', 'Hours per Day'],
    ['Por hacer',   por],
    ['En proceso',   en],
    ['Terminado',  ter]
  ]);

  var options = {
    title: 'GRAFICO TAREAS DURANTE EL MES'
  };

  var chart = new google.visualization.PieChart(document.getElementById('piechart'));

  chart.draw(data, options);
}
