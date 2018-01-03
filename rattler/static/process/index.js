// Die Variablen müssen wegen Jinja in der html-Datei vorbereitet werden!

// Funktion, um Spalte in 2. Dimension als Zeile auszugeben
// https://stackoverflow.com/a/34979219
const arrayColumnAsRow = (arr, n) => arr.map(x => x[n]);
/*
console.log("Zeitreihe: ");
console.log(arrayColumnAsRow(results.data, zeitreihenSpalte));
*/


// Plotly: Graph von vorheriger Seite wieder plotten
    var traces = [];
    // s. Variablenname
    zeitreihenSpalteAlsZeile = arrayColumnAsRow(dataArray, zeitreihenSpalte);

    var layout = {
        'xaxis': {
            autotick: true
        }
    }

    // Alle Spalten durchlaufen und Daten für die Visualisierung aufbereiten
    for(i=0; i < anzSpalten; i++){ // i = Index über Spalten
        traces[i] = {
            x: zeitreihenSpalteAlsZeile,
            y: arrayColumnAsRow(dataArray, i),
            name: spaltenTitel[i] + "(" + spaltenEinheiten[i] + ")",
            type: 'scatter',
            line: {
                width: 1.5,
            }
        }
        var yaxisTitle;
        if(i==0){
            traces[i]['yaxis'] = 'y';
            yaxisTitle = 'yaxis';
        } else {
            traces[i]['yaxis'] = 'y' + (i+1);
            yaxisTitle = 'yaxis' + (i+1);
        }
        layout[yaxisTitle] = {
            showgrid: false,
            zeroline: false,
            showline: false,
            autotick: true,
            showticklabels: false,
        }
        if(i!=0){
            layout[yaxisTitle]['overlaying'] = 'y';
        }
    }
    /*
    console.log(traces);
    console.log(layout);
    */
    traces[zeitreihenSpalte] = [];
    traces[zeitreihenSpalte].shift();

    Plotly.newPlot('firstGraph', traces, layout);



    // Plotly: Graph von vorheriger Seite wieder plotten
    var traces = [];
    // s. Variablenname
    zeitreihenSpalteAlsZeile = arrayColumnAsRow(newDataArray, zeitreihenSpalte);

    var layout = {
        'xaxis': {
            autotick: true
        }
    }

    // Alle Spalten durchlaufen und Daten für die Visualisierung aufbereiten
    for(i=0; i < anzSpalten; i++){ // i = Index über Spalten
        traces[i] = {
            x: zeitreihenSpalteAlsZeile,
            y: arrayColumnAsRow(newDataArray, i),
            name: spaltenTitel[i] + "(" + spaltenEinheiten[i] + ")",
            type: 'scatter',
            line: {
                width: 1.5,
            }
        }
        var yaxisTitle;
        if(i==0){
            traces[i]['yaxis'] = 'y';
            yaxisTitle = 'yaxis';
        } else {
            traces[i]['yaxis'] = 'y' + (i+1);
            yaxisTitle = 'yaxis' + (i+1);
        }
        layout[yaxisTitle] = {
            showgrid: false,
            zeroline: false,
            showline: false,
            autotick: true,
            showticklabels: false,
        }
        if(i!=0){
            layout[yaxisTitle]['overlaying'] = 'y';
        }
    }


    console.log(traces);
    console.log(layout);


    traces[zeitreihenSpalte] = [];
    traces[zeitreihenSpalte].shift();
    Plotly.newPlot('secondGraph', traces,layout);


// Spalten aufzählen, um spaltenweise Features auswählen zu können
    for(i=0; i < anzSpalten; i++){
        // vor einem Pärchen von 2 Spalten eine Row einfügen
        if(i % 4 == 0){
            $("#dataColsSection").append("<div id='dataColumnRow" + i + "' class='row' style='background: #eee; padding: 10px 0'></div>");
        } else if(i % 2 == 0){ // bei jeder 2. Zeile => Zeile leicht grau hinterlegen
            $("#dataColsSection").append("<div id='dataColumnRow" + i + "' class='row' style='padding: 10px 0'></div>");
        }
        $("#spaltenColTemplate").clone().attr("id", "spaltenCol" + i).appendTo("#dataColumnRow" + (i - (i%2))).show();
        
        // Spaltentitel einfügen
        $("#spaltenCol" + i + " .colHeader").html("Spalte <b>" + spaltenTitel[i] + "</b>");
        
        // IDs, names, fors
            $("#spaltenCol" + i + " #hochpass").attr("name", "hochpass" + i).attr("id", "hochpass" + i);
            $("#spaltenCol" + i + " .hochpassLabel").attr("for", "hochpass" + i);

                $("#spaltenCol" + i + " #hochpassOrder").attr("id", "hochpassOrder" + i);
                $("#spaltenCol" + i + " .hochpassOrderLabel").attr("for", "hochpassOrder" + i);

                $("#spaltenCol" + i + " #hochpassCofreq").attr("id", "hochpassCofreq" + i);
                $("#spaltenCol" + i + " .hochpassCofreqLabel").attr("for", "hochpassCofreq" + i);
                
            $("#spaltenCol" + i + " #tiefpass").attr("name", "tiefpass" + i).attr("id", "tiefpass" + i);
            $("#spaltenCol" + i + " .tiefpassLabel").attr("for", "tiefpass" + i);

                $("#spaltenCol" + i + " #tiefpassOrder").attr("id", "tiefpassOrder" + i);
                $("#spaltenCol" + i + " .tiefpassOrderLabel").attr("for", "tiefpassOrder" + i);

                $("#spaltenCol" + i + " #tiefpassCofreq").attr("id", "tiefpassCofreq" + i);
                $("#spaltenCol" + i + " .tiefpassCofreqLabel").attr("for", "tiefpassCofreq" + i);
            
            $("#spaltenCol" + i + " #gauss").attr("name", "gauss" + i).attr("id", "gauss" + i);
            $("#spaltenCol" + i + " .gaussLabel").attr("for", "gauss" + i);

                $("#spaltenCol" + i + " #gaussStd").attr("id", "gaussStd" + i);
                $("#spaltenCol" + i + " .gaussStdLabel").attr("for", "gaussStd" + i);
    }