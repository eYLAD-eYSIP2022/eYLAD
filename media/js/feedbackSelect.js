let ajax_data;
let ajax_legend;

let graph_data;
var graph_header;
var graph_total_reponses;

const drawGraph = () => {
    document.getElementById('feedbackSelectContainer').innerHTML="";
    
    switch ($("#graph-type option:selected").val()) {
       
        // Anychart Graphs => https://www.anychart.com/products/anychart/gallery
        case '0':{
            console.log("Pie Anychart");
            var data = graph_data;
            var chart = anychart.pie(data);
            chart.animation(true);
            chart
                .innerRadius("50%")
                .explode(25);
            var title = chart.title();
            title.enabled(true);
            title.useHtml(true);
            title.text(
                `<div style="color: #000000; font-size: 18px;">${graph_header}</div>`+
                "<br><a style=\"color:#3d3d3d; font-size: 12px;\">"+
                `Total Responses: ${graph_total_reponses}</a>`
            );
            chart.palette(['#003f5c',
                '#ef5675',
                '#374c80',
                '#bc5090',
                '#7a5195',
                '#ff764a',
                '#ffa600']);
            var tooltip = chart.tooltip();
            tooltip.format(function(e){
                var percent = (parseInt(this.value) / parseInt(graph_total_reponses)) * 100;
                return "Percentage: "+ percent.toFixed(1) +"%\nData: "+ (this.value) +"\nTotal Responses: " + graph_total_reponses;
            });
            chart.container("feedbackSelectContainer");
            chart.draw();
            document.getElementById("feedbackSelectContainer").style.display="block";
            break;
        }
        
        case '1':{
            console.log("Bar Anychart");
            var data = graph_data;
            var chart = anychart.column();

            chart.animation(true);
            
            var title = chart.title();
            title.enabled(true);
            title.useHtml(true);
            title.text(
                `<div style="color: #000000; font-size: 18px;">${graph_header}</div>`+
                "<br><a style=\"color:#3d3d3d; font-size: 12px;\">"+
                `Total Responses: ${graph_total_reponses}</a>`
            );

            var series = chart.column(data);
            
            series.normal().fill('#53a0e2');
            series.hovered().fill('#7fc3e5');
            series.selected().fill('#2e59a8');
            series.normal().stroke('null');
            series.hovered().stroke('null');
            series.selected().stroke('null');

            var tooltip = chart.tooltip();
            tooltip.format(function(e){
                var percent = (parseInt(this.value) / parseInt(graph_total_reponses)) * 100;
                return "Percentage: "+ percent.toFixed(1) +"%\nData: "+ (this.value) +"\nTotal Responses: " + graph_total_reponses;
            });

            chart.yAxis().title('Number of Teams');

            chart.container("feedbackSelectContainer");
            chart.draw();
            document.getElementById("feedbackSelectContainer").style.display="block";
            break;        
        }
        case '2':{
            console.log("Bar-Spline Anychart");
            var chart = anychart.column();
            
            chart.animation(true);
            
            var title = chart.title();
            title.enabled(true);
            title.useHtml(true);
            title.text(
                `<div style="color: #000000; font-size: 18px;">${graph_header}</div>`+
                "<br><a style=\"color:#3d3d3d; font-size: 12px;\">"+
                `Total Responses: ${graph_total_reponses}</a>`
            );
            
            var columnSeries = chart.column(graph_data);
            columnSeries.name('Column');

            var lineSeries = chart.spline(graph_data);
            lineSeries.name('Line');

            var tooltip = chart.tooltip();
            tooltip.format(function(e){
                var percent = (parseInt(this.value) / parseInt(graph_total_reponses)) * 100;
                return "Percentage: "+ percent.toFixed(1) +"%\nData: "+ (this.value) +"\nTotal Responses: " + graph_total_reponses;
            });

            chart.yAxis().title('Number of Teams');

            chart.container('feedbackSelectContainer');

            chart.draw();
            document.getElementById("feedbackSelectContainer").style.display="block";
            break;
        }
        case '3':{
            console.log("Polar Anychart");
            var chart = anychart.polar();

            chart.animation(true);

            var columnSeries = chart.column(graph_data);

            var title = chart.title();
            title.enabled(true);
            title.useHtml(true);
            title.text(
                `<div style="color: #000000; font-size: 18px;">${graph_header}</div>`+
                "<br><a style=\"color:#3d3d3d; font-size: 12px;\">"+
                `Total Responses: ${graph_total_reponses}</a>`
            );

            chart.yAxis(false);

            var tooltip = chart.tooltip();
            tooltip.format(function(e){
                var percent = (parseInt(this.value) / parseInt(graph_total_reponses)) * 100;
                return "Percentage: "+ percent.toFixed(1) +"%\nData: "+ (this.value) +"\nTotal Responses: " + graph_total_reponses;
            });

            chart.xScale('ordinal');

            chart.container('feedbackSelectContainer');

            chart.draw();
            document.getElementById("feedbackSelectContainer").style.display="block";
            break;
        }
        
        default: {
            console.log("ERR occured!");
            break;
        }
    }
}


$('#feedback-task').on('change', function (e) {
    var taskSelected = this.value;  
    console.log("Task No. ", taskSelected);
    $('#feedback-ques').find('option').not(':first').remove();
    $.ajax({
        // #### URL and datatype for ajax call
        url: `/feedbackSelect/${taskSelected}/`,
        dataType: 'json',
        // #### Success function
        success: function (suc_data) {
            // console.log("AJAX called!:>");
            // console.log();
            // #### Converting data in json format
            ajax_data = JSON.parse(suc_data.data);
            ajax_legend = suc_data.legend;
            console.log(ajax_data, ajax_legend);
            var ques = Object.keys(ajax_data);
            ques.forEach((element) => {
                // console.log(element);
                $('#feedback-ques').append(new Option(element, element));
            });
            // console.log(ajax_data);
            
        }
    });
})

// On Graph-selection "Button" click
$('#graph-selection-btn').click(function() {
    var FB_task = $("#feedback-task option:selected").val();
    var FB_ques = $("#feedback-ques option:selected").val();
    var FB_graph = $("#graph-type option:selected").val();
    if ( (FB_graph != -1) && (FB_ques != -1) && (FB_task != -1) ) {
        // console.log(ajax_data);
        var legend_data = ajax_legend[FB_ques];
        graph_data = [];
        // console.log(ajax_data, FB_ques, ajax_legend);
        var ques_data = ajax_data[FB_ques];
        // console.log(ques_data);
        let j = 6;
        graph_total_reponses = 0;
        if ((FB_task == 6) || (FB_task == 13))
            j = 7;
        for(let i=1;i<j;i++) {
            var str='';
            str = nav_theme+"_"+i;
            // console.log(str, ques_data[str]);
            if (ques_data[str] != null) {
                graph_data.push([legend_data[i],ques_data[str]]);
                graph_total_reponses += parseInt(ques_data[str]);
            }
        }
        console.log(graph_data);
        // Graph
        graph_header = FB_ques;
        drawGraph();
    }
    else {
        alert("Please, select the values !!");
        console.log("Option not selected !!");
    }
});