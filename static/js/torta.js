
google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        debugger
        var valor = document.getElementById('hidden')
        var dos = parseInt(valor.value)
        var valor1 = document.getElementById('hidden1')
        var dos1 = parseInt(valor1.value)
        var valor2 = document.getElementById('hidden2')
        var dos2 =  parseInt(valor2.value)

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['Por hacer',     dos],
          ['En proceso',  dos1],
          ['Terminado', dos2],

        ]);
        console.log(data);
        var options = {
          title: 'My Daily Activities'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }