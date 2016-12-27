function imprime_pdf(){
  debugger
  var doc = new jsPDF();
  var elementHandler = {
    '#content': function (element, renderer) {
      return true;
    }
  };
  var source = window.document.getElementsByTagName("body")[0];
  doc.fromHTML(
      source,
      15,
      15,
      {
        'width': 180,'elementHandlers': elementHandler
      });

  doc.output("dataurlnewwindow");
  };
