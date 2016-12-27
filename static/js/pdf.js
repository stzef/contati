function pdf(){
      debugger
   	 	var doc = new jsPDF();
   	 	var imgHeight=140 ;
	    var imgWidth=140 ;
	    var positionY=20;
	    var positionX=20;

   	 	doc.setFontSize(15);
   	    doc.text(15, 15, "Hola JSPDF y html2canvas");

   	 	html2canvas($("#content"), {
            onrendered: function(canvas) {
				var img = canvas.toDataURL("img/bg");
				doc.addImage(img, 'JPG', positionX ,  positionY, 140, imgWidth);
				doc.save('MyPdf.pdf');
				}
        });

   	 	};
