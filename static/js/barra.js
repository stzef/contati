 google.charts.load("current", {packages:["corechart"]});
 google.charts.setOnLoadCallback(drawChart);
 function drawChart() {
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
