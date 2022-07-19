// #### Declaring Global Variables
var data, y, conf, result, expnotsub, box_data, tableCells, token, conftype=["table-success", "table-warning", "table-danger"], new_rows,threshold, predthis, text = "ALL",doughnutChart,curr_task=num;
var  feedback_data,total_submissions = 0;
var link = String(window.location.href);
var num = link[link.length - 2]
num = parseInt(num)
// setInterval(function(){ alert("Hello"); }, 3000);
// #### Data of total teams in the event
// var total = JSON.parse(localStorage.getItem("total"));

// #### Data of teams submitted this task for bar chart
var this_task = JSON.parse(localStorage.getItem("this_task"));

// #### Data of teams submitted prev task
var prev_task = JSON.parse(localStorage.getItem("prev_task"));

// #### Getting task name i.e. Task1
var task_name = JSON.parse(localStorage.getItem("taskname"));

// #### Data of teams submitted this task for submission table
var sub_this_task = JSON.parse(localStorage.getItem("sub_this_task"));

// #### Data of teams submitted with date this task for line chart
var sub_by_date = JSON.parse(localStorage.getItem("sub_by_date"));
sub_by_date.reverse()
var threshold = JSON.parse(localStorage.getItem("thresh"));
threshold = parseFloat(threshold)
var parameters = JSON.parse(localStorage.getItem("parameters"));
var team_contact_details = JSON.parse(localStorage.getItem("details"));
var data = JSON.parse(localStorage.getItem("json_data"));
var time_passed = document.getElementById("time_pass_updated")
var key_value = {
    'ALL':0,
    'AB':1,
    'BM':2,
    'DB':3,
    'FW':4,
    'SM':5,
    'SS':6
};
var this_task_data = [0,0,0,0,0,0]
this_task.forEach((obj, index) => { 
    total_submissions = total_submissions + obj[1]; 
    this_task_data[key_value[obj[0]]-1]=obj[1];
})
// console.log(this_task_data);

var prev_task_data = [0, 0, 0, 0, 0, 0];
prev_task.forEach((obj, index) => {
    prev_task_data[(key_value[obj[0]]-1)] += obj[1]
})
// console.log(prev_task_data);
// console.log(sub_by_date)
//console.log(total.map((obj,index)=>{return(obj[0])}))
// console.log(result)

// To update all the graphs when theme is changed
let nav_theme = document.getElementById("main_theme").value;
// console.log(nav_theme);
const theme_change = () => {
    nav_theme = document.getElementById("main_theme").value;
    console.log(nav_theme);
    updateDoughnutChart();
    updateLineChart();
    updateOnChange2();
    var table=$('#table1').DataTable()
    table.destroy();
    var table2=$('#table2').DataTable()
    table2.destroy();
    load_table(data, threshold);
    var buttons = document.getElementsByClassName("dt-button");
    setTimeout(() => {
        style_buttons(buttons)
        set_in_line()
    }, 2000);
}
// console.log(nav_theme);
// console.log(typeof(key_value[nav_theme]));

// ########################################   Model metrics Start ###################################################
// #### Title of the model metrics
var params = document.getElementById("modelHeader")
params.innerText = params.innerText+"  "+task_name 

// #### Giving Basic data before Ajax call is completed
params = document.getElementById("modelParameters")
params.innerText = "Login count, Previous task feedback, Discourse activity, previous task scores"

// #### Adding the image to the model metrics element
params = document.getElementById("modelMetrics")
params.src=`/media/metrics/${task_name}.png`
// ########################################   Model Metrics End ###################################################


// ########################################   Bar Chart Start ###################################################
// #### Bar chart Constructor
let mychart = document.getElementById("barChart").getContext('2d');
let bargra = new Chart(mychart, {
    type: 'bar',
    data: {
        // #### Bar chart labels on X axis i.e. theme names
        labels: Object.keys(key_value).filter(i=> i !== 'ALL'),

        // #### Data 1 for all teams who submitted this task
        datasets: [{
            label: 'Submitted this task',
            data: this_task_data,
            borderColor: [`rgba(97, 216, 216, 1)`, `rgba(97, 216, 216, 1)`, `rgba(97, 216, 216, 1)`, `rgba(97, 216, 216, 1)`, `rgba(97, 216, 216, 1)`,`rgba(97, 216, 216, 1)`],
            backgroundColor: [`rgba(0, 175, 185, 1)`, `rgba(0, 175, 185, 1)`, `rgba(0, 175, 185, 1)`, `rgba(0, 175, 185, 1)`, `rgba(0, 175, 185, 1)`, `rgba(0, 175, 185, 1)`],
            stack: "Stack 0",
        },
        // #### Data 2 for teams submitted prev task
        {
            label: 'Submitted prev task',
            data: prev_task_data,
            borderColor: [`rgba(255,0,0,1)`, `rgba(255,0,0,1)`, `rgba(255,0,0,1)`, `rgba(255,0,0,1)`, `rgba(255,0,0,1)`, `rgba(255,0,0,1)`],
            backgroundColor: [`rgba(240, 113, 103, 1)`, `rgba(240, 113, 103, 1)`, `rgba(240, 113, 103, 1)`, `rgba(240, 113, 103, 1)`, `rgba(240, 113, 103, 1)`, `rgba(240, 113, 103, 1)`],
            stack: "Stack 1"
        },
        // #### Data 3 for total teams in the event
        // {
        //     label: 'Total teams',
        //     data: total.map((obj, index) => { return (obj[1]) }),
        //     backgroundColor: [`rgb(254, 217, 183)`, `rgb(254, 217, 183)`, `rgb(254, 217, 183)`, `rgb(254, 217, 183)`, `rgb(254, 217, 183)`],
        //     stack: "Stack 2"
        // },

        ]

    },

    options: {
        // #### Show theme name on top
        legend: { display: true },
        responsive: true,
        scales: {
            xAxes: [{
                stacked: true // #### this should be set to make the bars stacked
            }],
            yAxes: [{
                stacked: false // #### this also..
            }]
        },
        plugins: {
            title: {
                display: true,
                text: `${task_name} Submission`,
                font: {
                    size: 24
                }
            }
        }
    }
})
// ########################################   Bar Chart Ends #########################################

// ########################################   Line Chart Start #########################################

// #### Declaring necessary variables
let lineChartDate = []
let LinechartData = []
// let maxLineChartData = [0,0,0,0,0,0,0]
let currentDate = ""

// ####  Function to format data in 2D list format
// ####  [ALL,AB,BM,DB,FW,SM,SS]
// console.log(sub_by_date);
sub_by_date.slice().reverse().forEach(element => {
    var index
    var pos = 0
    if(element[2]===currentDate)
    {
        // #### Get the index of the date of submission if already exist
        index =  lineChartDate.indexOf(currentDate)
    }else{
        // #### push and get index of the date of submission if doesn't exist
        lineChartDate.push(element[2])
        currentDate = element[2]
        LinechartData.push([0,0,0,0,0,0,0])
        index =  lineChartDate.indexOf(currentDate)
    }
    // console.log(element, lineChartDate, LinechartData, index)
    // ####  get Column index 
    switch(element[1]) {
        case "AB":{
            pos=1;
            break;
        }
        case "BM":{
            pos=2;
            break;
        }
        case "DB":{
            pos=3;
            break;
        }
        case "FW":{
            pos=4;
            break;
        }
        case "SM":{
            pos=5;
            break;
        }
        case "SS":{
            pos=6;
            break;
        }
    }

    // ####  Set count of theme on that date
    LinechartData[index][pos] = element[0]
    // ####  Add to count of that date (for total login on that day)
    LinechartData[index][0] += element[0]
    // if (LinechartData[index][0] > maxLineChartData[0]) {
    //     maxLineChartData[0] = LinechartData[index][0]
    // }
    // if (element[0] > maxLineChartData[pos]) {
    //     maxLineChartData[pos] = element[0];
    //     console.log(maxLineChartData, pos);
    // }
});
// lineChartDate = lineChartDate.reverse()
// console.log(lineChartDate)
// console.log(LinechartData)
// console.log(maxLineChartData[key_value[nav_theme]]);       

// plugin function to move chart using buttons
const buttonScrollLineChart = {
    id: 'moveChart',
    afterEvent(chart, args) {
        const {ctx, canvas, chartArea: {left, right, top, bottom, width, height} } = chart;
        canvas.addEventListener('mousemove', (event) => {
            const x = args.event.x;
            const y = args.event.y;

            if (x >= left - 15 && x <= left + 15 && y >= height/2 + top - 15 
                && y <= height/2 + top + 15) {
                canvas.style.cursor = 'pointer';
            }
            else if (x >= right - 15 && x <= right + 15 && y >= height/2 + top - 15 
            && y <= height/2 + top + 15) {
                canvas.style.cursor = 'pointer';
            }
            else{
                canvas.style.cursor = 'default';
            }
        })
    },
    
    afterDraw(chart, args, pluginOptions) {
        const {ctx, chartArea: {left, right, top, bottom, width, height} } = chart;

        class CircleChevron {
            // constructor(x1, y1) {

            // }
            draw(ctx, x1, pixel) {
                const angle = Math.PI / 180;
                // Circle
                ctx.beginPath();
                ctx.lineWidth = 3;
                ctx.strokeStyle = 'rgba(102, 102, 102, 0.5)';
                ctx.fillStyle = 'white';
                ctx.arc(x1, height / 2 + top, 15, angle * 0, angle * 360, false)
                ctx.stroke();
                ctx.fill();
                ctx.closePath();
                // Arrow
                ctx.beginPath();
                ctx.lineWidth = 3;
                ctx.strokeStyle = '#088383';
                ctx.moveTo(x1 + pixel, height / 2 +top - 7.5);
                ctx.lineTo(x1 - pixel, height / 2 + top);
                ctx.lineTo(x1 + pixel, height / 2 +top + 7.5);
                ctx.stroke();
                ctx.closePath();
            }
        }

        let drawCircleLeft = new CircleChevron();
        drawCircleLeft.draw(ctx, left, 5);
        
        let drawCircleRight = new CircleChevron();
        drawCircleRight.draw(ctx, right, -5);
    }
}

// #### Constructor of line chart
let LineChart = new Chart(document.getElementById("lineChart"),{
    type:'line',
    data:{
    // #### Dates as labels of line chart
        labels: lineChartDate,
        datasets: [{
            label: 'Number of Logins per day',
            // #### Show All themes by default
            data: LinechartData.map((obj)=>{return(obj[key_value[nav_theme]])}),
            fill: true,
            // #### Color of the chart
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    },
    options: {
        responsive: true,
        layout: {
            padding: {
                right: 18
            }
        },
        plugins: {
            title: {
                display: true,
                text: `Login Statistics`,
                font: {
                    size: 24
                }
            }
        },
        scales: {
            x: {
                min: LinechartData.length-10,
                max: LinechartData.length-1,
                title: {
                    display: true,
                    text: 'Date',
                    font: {size:14}
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Number of teams',
                    font: {size:14}
                },
                ticks: {
                    min: 0,
                    // max: maxLineChartData[key_value[nav_theme]],
                    beginAtZero: true,
                    callback: function(value, index, values) {
                        if (Math.floor(value) === value) {
                            return value;
                        }
                    }
                },
                // min: 0,
                // max: maxLineChartData[key_value[nav_theme]],
                beginAtZero: true
            },
        }
    },
    plugins: [buttonScrollLineChart]
})

// For button scroll
function moveScroll() {
    const { ctx, canvas, chartArea: {left, right, top, bottom, width, height} } = LineChart;
    canvas.addEventListener('click', (event) => {
        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        // console.log(x);
        // console.log(y);

        if (x >= left - 15 && x <= left + 15 && y >= height/2 + top - 15 
            && y <= height/2 + top + 15) {
            // console.log("Left");
            LineChart.options.scales.x.min = LineChart.options.scales.x.min - 2;
            LineChart.options.scales.x.max = LineChart.options.scales.x.max - 2;
            if (LineChart.options.scales.x.min <= 0) {
                LineChart.options.scales.x.min = 0;
                LineChart.options.scales.x.max = 9;
            };
        }
        if (x >= right - 15 && x <= right + 15 && y >= height/2 + top - 15 
        && y <= height/2 + top + 15) {
            // console.log("Right");
            LineChart.options.scales.x.min = LineChart.options.scales.x.min + 2;
            LineChart.options.scales.x.max = LineChart.options.scales.x.max + 2;
            if (LineChart.options.scales.x.max >= LinechartData.length) {
                LineChart.options.scales.x.min = LinechartData.length-10;
                LineChart.options.scales.x.max = LinechartData.length-1;
            };
        }
        LineChart.update();
    })
}
LineChart.ctx.onclick = moveScroll();

// For mouse wheel scroll
function scrollLineChart(scroll, chart, dataLength) {
    console.log("Scrolling Login chart");
    if (scroll.deltaX > 40) {
        if(LineChart.options.scales.x.max >= dataLength-1) {
            LineChart.options.scales.x.min = dataLength-10;
            LineChart.options.scales.x.max = dataLength-1;
        }
        else {
            LineChart.options.scales.x.min += 1;
            LineChart.options.scales.x.max += 1;
        }
    }
    else if (scroll.deltaX < -30) {
        if(LineChart.options.scales.x.min <= 0) {
            LineChart.options.scales.x.min = 0;
            LineChart.options.scales.x.max = 9;
        }
        else {
            LineChart.options.scales.x.min -= 1;
            LineChart.options.scales.x.max -= 1;
        }
    }
    // console.log(LineChart.options.scales.x.min, LineChart.options.scales.x.max);
    LineChart.update();
}

LineChart.canvas.addEventListener('wheel', (e) => {
    let dataLength = LineChart.data.labels.length;
    if (dataLength > 10)
        scrollLineChart(e, LineChart, dataLength);
});


// #### Function to update line chart
const updateLineChart = () =>{
    // #### get value of select i.e. theme selected
    // var value = document.getElementById(`line1`).value;
    // var pos = 0

    // #### Switch case fot index
    // switch(value) {
    //     case "AB":{
    //         pos=1;
    //         break;
    //     }
    //     case "BM":{
    //         pos=2;
    //         break;
    //     }
    //     case "DB":{
    //         pos=3;
    //         break;
    //     }
    //     case "FW":{
    //         pos=4;
    //         break;
    //     }
    //     case "SM":{
    //         pos=5;
    //         break;
    //     }
    //     case "SS":{
    //         pos=6;
    //         break;
    //     }
    //     default:{
    //         pos=0;
    //         break;
    //     }
    //   }

    // #### Updating line chart
    LinechartData.forEach((obj,index)=>{
        LineChart.data.datasets[0].data[index] = obj[key_value[nav_theme]];
    })
    LineChart.update()
}
// ########################################   Line Chart Ends #########################################




// ########################################   Doughnut Chart Start #########################################
let BarchartData = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

    

// ##########################################  AJAX BEGINS #################################################

const update_chart_data = () =>{
    console.log("Updating Data using ajax")
    $.ajax({
        // #### URL and datatype for ajax call
        url: `/taskdata/${num}/`,
        dataType: 'json',
        // #### Success function
        success: function (suc_data) {
            // #### Converting data in json format
            // console.log(suc_data);
            data = JSON.parse(suc_data.json_data)
            parameters=JSON.parse(suc_data.parameters)
            threshold = JSON.parse(suc_data.thresh)
            // console.log(threshold);
            team_contact_details = JSON.parse(suc_data.details)
            
            // #### Threshold for this model
            threshold = parseFloat(threshold)
            // console.log(team_contact_details);
    
            // #### Parameters for model metrics element
            parameters = parameters.split(",")
            var InnERhtml = ""
            parameters.forEach((obj)=>[
                InnERhtml += '<li class="list-group-item">'+obj+"</li>"
            ])
            var params = document.getElementById("threshold_val")
            params.innerHTML = threshold;
            var params = document.getElementById("modelParameters")
            params.innerHTML = '<ul class="list-group list-group-flush">'+InnERhtml+"</ul>"
            params.style.overflow = "auto";
    
            // #### Calculate data for doughnut chart
            // console.log(data)
            y = Object.values(data["team_id"])
            conf = Object.values(data["confidence"])
            result = conf.filter(con => con > threshold)
            expnotsub = conf.length - result.length
            // console.log(result)
            time_passed.innerText = 0;
            // #### Set table loading spinners to none
            document.getElementById("spinner_home2").style.display = "none";
            document.getElementById("spinner_home1").style.display = "none";
                
            // #### Call functions to populate and style the table
            // var table=$('#table1').DataTable()
            // table.clear().draw();
            // var table2=$('#table2').DataTable()
            // table2.clear().draw();
            load_table(data,threshold)
            setBarData(data,y,threshold)
            var buttons = document.getElementsByClassName("dt-button")
            setTimeout(() => {
                style_buttons(buttons)
                set_in_line()
            }, 2000);

            // #### Set data of 2D matrix
            BarchartData[0][0] = total_submissions
            BarchartData[1][0] = result.length
            BarchartData[2][0] = expnotsub
    
            // #### Draw Doughnut chart
            doughnutChart.destroy()
            doughnutChart = new Chart(document.getElementById("doughnutChart"), {
                type: 'doughnut',
                data: {
                    labels: ["Teams Submitted", 'Teams expected to submit', 'Teams not expected to submit'],
                    datasets: [
                        {
                            label: "Task status",
                            backgroundColor: ["#00AFB9", "#0081A7", "#F07167"],
                            data: [total_submissions, result.length, expnotsub],
                            hoverOffset: 10
                        }
                    ]
                },
                options: {
                    plugins: {
                        title: {
                            display: true,
                            text: 'Custom Chart Title'
                        }
                    }
                }
            });
    
        }
    })
}

// ##########################################  AJAX ENDS #################################################
// #### Populate rest of the themes
const setBarData=(data,y,threshold)=>{
    // console.log(data);
    for (var i = 0; i < y.length; ++i) {
            switch(data["theme"][i]) {
                case "AB":{
                    if (data["confidence"][i] > threshold) {
                        BarchartData[1][1] +=1
                    } else {
                        BarchartData[2][1] += 1
                    }
                    break;
                }
                case "BM":{
                    if (data["confidence"][i] > threshold) {
                        BarchartData[1][2] +=1
                    } else {
                        BarchartData[2][2] += 1
                    }
                    break;
                }
                case "DB":{
                    if (data["confidence"][i] > threshold) {
                        BarchartData[1][3] +=1
                    } else {
                        BarchartData[2][3] += 1
                    }
                    break;
                }
                case "FW":{
                    if (data["confidence"][i] > threshold) {
                        BarchartData[1][4] +=1
                    } else {
                        BarchartData[2][4] += 1
                    }
                    break;
                }
                case "SM":{
                    if (data["confidence"][i] > threshold) {
                        BarchartData[1][5] +=1
                    } else {
                        BarchartData[2][5] += 1
                    }
                    break;
                }
                case "SS":{
                    if (data["confidence"][i] > threshold) {
                        BarchartData[1][6] +=1
                    } else {
                        BarchartData[2][6] += 1
                    }
                    break;
                }
              }
    }
 
    // console.log(this_task);
    this_task.forEach((obj)=>{
        BarchartData[0][key_value[obj[0]]]=obj[1];
        // console.log(key_value[obj[0]],obj)
    })
    // console.log(BarchartData)

    // BarchartData[0][1] = this_task[0][1]
    // BarchartData[0][2] = this_task[1][1]
    // BarchartData[0][3] = this_task[2][1]
    // BarchartData[0][4] = this_task[3][1]
    // BarchartData[0][5] = this_task[4][1]
    // BarchartData[0][6] = this_task[5][1]
}

// #### Function to update doughnut chart based on themes
const updateDoughnutChart=()=>{
// #### get value of the selected item
    // var value = document.getElementById(`doughnut1`).value;
    // var pos = 0
    // #### Switch case for values
    // switch(value) {
    //     case "AB":{
    //         pos=1;
    //         break;
    //     }
    //     case "BM":{
    //         pos=2;
    //         break;
    //     }
    //     case "DB":{
    //         pos=3;
    //         break;
    //     }
    //     case "FW":{
    //         pos=4;
    //         break;
    //     }
    //     case "SM":{
    //         pos=5;
    //         break;
    //     }
    //     case "SS":{
    //         pos=6;
    //         break;
    //     }
    //     default:{
    //         pos=0;
    //         break;
    //     }
    //   }
    // #### update doughnut chart
    // console.log(BarchartData, nav_theme);
    doughnutChart.data.datasets[0].data[0] = BarchartData[0][key_value[nav_theme]];
    doughnutChart.data.datasets[0].data[1] = BarchartData[1][key_value[nav_theme]];
    doughnutChart.data.datasets[0].data[2] = BarchartData[2][key_value[nav_theme]];
    doughnutChart.update();
}

// console.log(team_contact_details);

// #### Parameters for model metrics element
parameters = parameters.split(",")
var InnERhtml = ""
parameters.forEach((obj)=>[
    InnERhtml += '<li class="list-group-item">'+obj+"</li>"
])
var params = document.getElementById("threshold_val")
params.innerHTML = threshold;
var params = document.getElementById("modelParameters")
params.innerHTML = '<ul class="list-group">'+InnERhtml+"</ul>"
params.style.overflow = "auto";

// #### Calculate data for doughnut chart
// console.log(data)
y = Object.values(data["team_id"])
conf = Object.values(data["confidence"])
result = conf.filter(con => con > threshold)
expnotsub = conf.length - result.length
// console.log(conf.length, result.length, expnotsub)

// #### Set table loading spinners to none
document.getElementById("spinner_home2").style.display = "none";
document.getElementById("spinner_home1").style.display = "none";
    
// #### Call functions to populate and style the table
load_table(data,threshold)
setBarData(data,y,threshold)
var buttons = document.getElementsByClassName("dt-button")
setTimeout(() => {
    style_buttons(buttons)
    set_in_line()
}, 2000);

// #### Set data of 2D matrix
BarchartData[0][0] = total_submissions
BarchartData[1][0] = result.length
BarchartData[2][0] = expnotsub
// console.log(key_value[nav_theme]);
// #### Draw Doughnut chart
doughnutChart = new Chart(document.getElementById("doughnutChart"), {
    type: 'doughnut',
    data: {
        labels: ["Teams Submitted", 'Teams expected to submit', 'Teams not expected to submit'],
        datasets: [{
            label: "Task status",
            backgroundColor: ["#00AFB9", "#0081A7", "#F07167"],
            data: [BarchartData[0][key_value[nav_theme]], BarchartData[1][key_value[nav_theme]], BarchartData[2][key_value[nav_theme]]],
        }],
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: `${task_name} Prediction`,
                font: {
                    size: 24
                }
            }
        }
    }
});


// ########################################   Doughnut Chart Ends  #########################################

// ########################################   Box Chart Start ###################################################
// ##########################################  AJAX BEGINS #################################################

// #### check for box chart. if task 0 then no box chart
if (num===0) {
        document.getElementById("feedback_chart_container").style.display="none"
    } 
else {
    $.ajax({            
        // #### Url and datatype of ajax call
        url: `/feedbacktrack/${num-1}/`,
        dataType: 'json',
        success: function (suc_data) {
            // #### Parse json data
            box_data = JSON.parse(suc_data.all_feedback_data)
            // console.log(box_data)

            // #### Delete the entries object in box_data
            delete box_data.Entries;

            // #### Get value of the select
            // var val_index = document.getElementById(`feedback_select2`).value;
            var val_index = nav_theme;
            var opt1=""
            var options = ""

            // #### Dynamic options for question select
            var data = Object.keys(box_data).forEach((obj1,index1)=>{
                options+=`<option value=${obj1}>${obj1}</option>`
                if (opt1==="") {
                    opt1=obj1
                }
            })
            document.getElementById("question_select").innerHTML=options
            document.getElementById("question_select").value=opt1

            // #### For loop to arrange data for box chart
            document.getElementById(`feedback_title2`).innerText = `${val_index} ${opt1} comparisons`;
            var data2= []
            for(var i=0;i<num;i++){
                var z= {
                    x:`Task ${i}`,
                    val_index:val_index,
                    val:`('${val_index}', 'Task ${i}', 0.0)`,
                    low :box_data[opt1][`('${val_index}', 'Task ${i}', 0.0)`],
                    q1 : box_data[opt1][`('${val_index}', 'Task ${i}', 0.25)`],
                    median : box_data[opt1][`('${val_index}', 'Task ${i}', 0.5)`],
                    q3 : box_data[opt1][`('${val_index}', 'Task ${i}', 0.75)`],
                    high : box_data[opt1][`('${val_index}', 'Task ${i}', 1.0)`]
                }
                // console.log(z)
                data2.push(z)
            }
            // #### Create chart object and set the data
            chart = anychart.box();
            series = chart.box(data2);
            // #### style box chart
            series.whiskerWidth(30);
            series.normal().whiskerStroke("#dd2c00", 0.5);
            series.hovered().whiskerStroke("#dd2c00", 1);
            series.selected().fill("#00cc99", 0.5);
            series.normal().stemStroke("#dd2c00", 0.5);
            series.hovered().stemStroke("#dd2c00", 1);
            series.selected().stemStroke("#dd2c00", 2);
            var xAxis = chart.xAxis();
            xAxis.staggerMode(2);
            chart.yScale().maximum(5);
            chart.yScale().ticks().interval(1);
            // #### Create box chart
            chart.container("box_chart2");
            chart.draw();
        }
    })
}

  

// ##########################################  AJAX ENDS #################################################

// #### Function to update box chart based on themes
const updateOnChange2 = () =>{
    if (num===0) {
        return
    }
    // #### Clear previous chart to make new chart
    document.getElementById("box_chart2").innerHTML="";

    // #### get theme and question selected
    // var val_index = document.getElementById(`feedback_select2`).value;
    var val_index = nav_theme;
    var opt1 = document.getElementById("question_select").value;
    // #### Update the title
    document.getElementById(`feedback_title2`).innerText = `${val_index} ${opt1} comparisons`;
    // #### Function to update doughnut chrt based on themes
    var data2= []
    for(var i=0;i<num;i++){
        var z= {
            x:`Task ${i}`,
            val_index:val_index,
            val:`('${val_index}', 'Task ${i}', 0.0)`,
            low :box_data[opt1][`('${val_index}', 'Task ${i}', 0.0)`],
            q1 : box_data[opt1][`('${val_index}', 'Task ${i}', 0.25)`],
            median : box_data[opt1][`('${val_index}', 'Task ${i}', 0.5)`],
            q3 : box_data[opt1][`('${val_index}', 'Task ${i}', 0.75)`],
            high : box_data[opt1][`('${val_index}', 'Task ${i}', 1.0)`]
        }
        // console.log(z)
        data2.push(z)
    }
    // #### Create chart object and set the data
    chart = anychart.box();
    series = chart.box(data2);
    // #### style box chart
    series.whiskerWidth(30);
    series.normal().whiskerStroke("#dd2c00", 0.5);
    series.hovered().whiskerStroke("#dd2c00", 1);
    series.selected().fill("#00cc99", 0.5);
    series.normal().stemStroke("#dd2c00", 0.5);
    series.hovered().stemStroke("#dd2c00", 1);
    series.selected().stemStroke("#dd2c00", 2);
    var xAxis = chart.xAxis();
    xAxis.staggerMode(2);
    chart.yScale().maximum(5);
    chart.yScale().ticks().interval(1);
    // #### Create box chart
    chart.container("box_chart2");
    chart.draw();
}
// ########################################   Box Chart Ends   ###################################################


// ########################################   Table Functions Start ###################################################

// #### plugin for data filter
$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        if ( settings.nTable.id !== 'table1' ) {
            return true;
        }
        // #### lower threshold value
        var min = parseFloat( $('#min').val());
        // #### Upper threshold value
        var max = parseFloat( $('#max').val());
        // #### lower threshold value
        var coln = parseInt( $('#column_sel').val(), 10 );
        
        var age = parseFloat( data[coln] ) || 0; // use data for the selected column
 
        // #### Checking all criteria for data
        if ( ( isNaN( min ) && isNaN( max ) ) ||
             ( isNaN( min ) && age <= max ) ||
             ( min <= age   && isNaN( max ) ) ||
             ( min <= age   && age <= max ) )
        {
            return true;
        }
        return false;
    }
);

// #### Function to populate the predicted and submitted table
function load_table(data,threshold) {
    var trHTML = '';
    var new_date = 0

    for (var i = 0; i < y.length; ++i) {
        // #### Filtering out the themes:
        if (data["theme"][i] == nav_theme) {
            // #### if confidence is above threshold value. Green color
            if (data["confidence"][i] > threshold) {
                token = 0;
            } else if (data["confidence"][i] > threshold-0.1) {
            // #### if confidence 10 % below threshold. yellow colour
                token = 1;
            } else {
            // #### else color red.
                token = 2;
            }
            if (data["confidence"][i] > threshold) {
            // #### for prediction column
                predthis = 1;
            } else {
                predthis = 0;
            }
            new_date = new Date(data["last_login"][i])
            var a = team_contact_details[y[i]][0];
            var b = team_contact_details[y[i]][1];
            // console.log({a:a,b:b})

            try {
                if (typeof(a)=="string") {
                    a = a.replace(/'/g, '"');
                    a = JSON.parse(a);
                    b = b.replace(/'/g, '"');
                    b = JSON.parse(b);
                }
            } catch (e) {
                if (e instanceof SyntaxError) {
                    a=[0,0,0,0]
                    b=[0,0,0,0]
                }
            }
            
            
            // console.log(a)
            // #### row for predicted table
            trHTML += `<tr class=${conftype[token]}><td>` + y[i] + // #### CSS for color of row and team id
                '</td><td>' + data["theme"][i] + // #### name of the theme
                '</td><td>' + predthis +  // #### prediction score 0 or 1
                '</td><td>' + (data["confidence"][i] * 100).toPrecision(4) +  // #### confidence score
                ' % </td><td>' + parseInt(data["login_count"][i]) +  // #### loginn count in e yantra portal
                // #### last login date in YYYY/MM/DD HH:MM:SS format
                '</td><td>' +`${new_date.getFullYear()}/${new_date.getMonth()+1}/${new_date.getDate()}  ${new_date.toLocaleTimeString("en-IN")}` +
                '</td><td>' + data["days online"][i] + // #### No. of days online on piazza platform
                '</td><td>' + data["posts"][i] +  // #### No. of Questions posted
                '</td><td>' + data["answers"][i] + // #### No. of answers contributed
                '</td><td>' + a[0] +  // #### Team Leader's email
                '</td><td>' + a[1] +  // #### second member's email
                '</td><td>' + a[2] +  // #### third member's email
                '</td><td>' + a[3] +  // #### fourth member's email
                '</td><td>' + b[0] +  // #### Team leader's phone No.
                '</td><td>' + b[1] +  // #### second member's phone No.
                '</td><td>' + b[2] +  // #### third member's phone No.
                '</td><td>' + b[3] +  // #### fourth member's phone No.
                '</td></tr>';  // #### closing tr tag
            // console.log(trHTML);
        }
    }
    // #### set inner html of tbody
    document.getElementById('table1Content').innerHTML = trHTML
    // console.log(JSON.parse(team_contact_details[y[0]][0]))
    // #### for table submitted
    trHTML = '';
    var date
    for (var i = 0; i < sub_this_task.length; ++i) {
        if ( sub_this_task[i][1] == nav_theme ) {
            date = new Date(sub_this_task[i][2])
            trHTML += `<tr class="table-success"><td>` + sub_this_task[i][0] + // #### team id
                '</td><td>' + sub_this_task[i][1] + // #### theme
                // #### date of latest submission in YYYY/MM/DD HH:MM:SS format
                '</td><td>' + `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}  ${date.toLocaleTimeString("en-IN")}` +
                '</td></tr>';
        }
    }
    // #### make all table footers as search bar
    $('#table1 tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input style="min-width: 112px; width:100%;" type="text" placeholder="Search '+title+'" />' );
    } );

    $('#table2 tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input style="min-width: 112px; width:100%;" type="text" placeholder="Search '+title+'" />' );
    } );    
    
    // #### inner html of tbody
    document.getElementById('table2Content').innerHTML = trHTML

    // #### function to make table into datatable
    $(document).ready(function () {
        var table=$('#table1').DataTable({
            dom: 'Blfrtip',
            destroy: true,
            // #### buttons on tables download option
            buttons: [
                'copyHtml5',
                {
                    extend: 'pdfHtml5',
                    title: function () { return getPredText(); }
                },
                {
                    extend: 'excelHtml5',
                    title: function () { return getPredText(); }
                },
                {
                    extend: 'csvHtml5',
                    title: function () { return getPredText(); }
                }

            ],
            // #### function for search on footer
            initComplete: function () {
                // #### Apply the search
                this.api().columns().every( function () {
                    var that = this;
     
                    $( 'input', this.footer() ).on( 'keyup change clear', function () {
                        if ( that.search() !== this.value ) {
                            that
                                .search( this.value )
                                .draw();
                        }
                    } );
                } );
            },
            "paging": true,
            "lengthChange": true,
            // #### options for pagelength i.e. first is value list and second is name list
            "lengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
            "pageLength": 10,
            "pagingType": "full_numbers",
            "language": {
                oPaginate: {
                //    sNext: '<i class="fa fa-forward"></i>',
                //    sPrevious: '<i class="fa fa-backward"></i>',
                   sFirst: '<<',
                   sLast: '>>'
                }
              }   
        });


        var table2=$('#table2').DataTable({
            dom: 'Blfrtip',
            destroy: true,
            // #### buttons for datatable download
            buttons: [
                'copyHtml5',
                {
                    extend: 'pdfHtml5',
                    title: function () { return getSubText(); }
                },
                {
                    extend: 'excelHtml5',
                    title: function () { return getSubText(); }
                },
                {
                    extend: 'csvHtml5',
                    title: function () { return getSubText(); }
                },
            ],
            "paging": true,
            responsive: true,
            "lengthChange": true,
            "lengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
            "pageLength": 10,
            "pagingType": "full_numbers",
            "language": {
                oPaginate: {
                //    sNext: '<i class="fa fa-forward"></i>',
                //    sPrevious: '<i class="fa fa-backward"></i>',
                   sFirst: '<<',
                   sLast: '>>'
                }
              } ,
            // #### for search bar in footer
            initComplete: function () {
                // #### Apply the search
                this.api().columns().every( function () {
                    var that = this;
     
                    $( 'input', this.footer() ).on( 'keyup change clear', function () {
                        if ( that.search() !== this.value ) {
                            that
                                .search( this.value )
                                .draw();
                        }
                    } );
                } );
            }
        });
    });

}


// #### function to style the download buttons 
const style_buttons = (buttons) => {
    // console.log(buttons)
    for (let index = 0; index < buttons.length; index++) {
        buttons[index].classList.add("btn")

        if (buttons[index].classList[1] === "buttons-pdf") {
            // #### if button is for downloading pdf: color red and add the pdf symbol
            buttons[index].classList.add("btn-danger")
            buttons[index].innerHTML = buttons[index].innerHTML + `  <i class="mdi mdi-file-pdf-outline" style="font-size: 1.2em;"></i>`;
        } else if (buttons[index].classList[1] === "buttons-csv") {
            // #### if button is for downloading CSV: color blue and add the arrow symbol
            buttons[index].classList.add("btn-primary")
            buttons[index].innerHTML = buttons[index].innerHTML + `  <i class="mdi mdi-arrow-right" style="font-size: 1.2em;"></i>`;
        } else if (buttons[index].classList[1] === "buttons-excel") {
            // #### if button is for downloading excel: color green and add the excel symbol
            buttons[index].classList.add("btn-success")
            buttons[index].innerHTML = buttons[index].innerHTML + `  <i class="mdi mdi-file-excel" style="font-size: 1.2em;"></i>`;
        } else {
            // #### if button is for Copying: color grey and add the clipboard symbol
            buttons[index].classList.add("btn-secondary")
            buttons[index].innerHTML = buttons[index].innerHTML + `  <i class="mdi mdi-clipboard-outline" style="font-size: 1.2em;"></i>`;
        }
    }
}

// #### function for setting line column numbers ,theme filter and search in order on both datatables
const set_in_line = () => {
    // #### create the element for the theme select
    // var el = document.createElement("div");
    // el.classList.add("row")
    // el.innerHTML = `<div class="col-6"><label style="margin-top: 14px;">Select Theme:</label></div>
    //       <div class="col-6" style="padding: 3px;">
    //         <select id="theme1" class="form-select " onchange="filter_data(1)" value="ALL">
    //           <!-- <option value="sel">Select theme</option> -->
    //           <option value="ALL">All Teams</option>
    //           <option value="AB">AB</option>
    //             <option value="BM">BM</option>
    //             <option value="DB">DB</option>
    //             <option value="FW">FW</option>
    //             <option value="SM">SM</option>
    //             <option value="SS">SS</option>
    //       </select>
    //       </div>`;

    // #### get the table_length filter
    var div = document.getElementById("table1_length");

    // #### get the table search
    var search = document.getElementById("table1_filter");
    div.style.marginLeft = "1px"
    search.style.marginRight = "15px"

    // #### get parent of the table_search
    var parent = div.parentNode;
    
    // Create and add a new wrapper div
    var wrapper = document.createElement('div');
    wrapper.classList.add("row")
    
    c1 = document.createElement("div")
    c1.classList.add("col-6")
    // c1.classList.add("col-md-4")
    div.classList.add("form-inline")
    div.getElementsByTagName("select").item(0).style.margin="5px"

    // c2 = document.createElement("div")
    // c2.classList.add("col-12")
    // c2.classList.add("col-md-4")

    c3 = document.createElement("div")
    c3.classList.add("col-6")
    // c3.classList.add("col-md-4")
    
    // #### insert wrapper element
    parent.replaceChild(wrapper, div);

    // #### set elements as childrens of wrapper
    wrapper.appendChild(c1);
    // wrapper.appendChild(c2);
    wrapper.appendChild(c3);
    c1.appendChild(div)
    // c2.appendChild(el)
    c3.appendChild(search)

    div.firstElementChild.firstElementChild.style.maxHeight="36px"
    div.firstElementChild.classList.add("d-flex")
    div.firstElementChild.style.marginTop="6px"
    div.firstElementChild.style.alignItems="center"
    div.firstElementChild.style.marginBottom="0px"
    div.firstElementChild.style.marginTop="0px"

    search.parentElement.style.margin="auto"
    search.firstChild.style.marginBottom="0px"
    search.style.marginTop="0px"

    $(search.firstChild).contents().filter(function(){
        return (this.nodeType == 3);
    }).remove();

    search.firstChild.firstChild.placeholder="Search"
    search.firstChild.firstChild.style.maxWidth="30vw"

    // #### create the element for the theme select
    // var el = document.createElement("div");
    // el.classList.add("row")
    // el.innerHTML = `<!-- <label style="margin-top: 14px;"></label>
    //       <div class="col-6" style="padding: 3px;"> -->
    //         <select id="theme2" class="form-select " onchange="filter_data(2)" value="ALL">
    //           <!-- <option value="sel">Select theme</option> -->
    //           <option value="ALL">Select Theme</option>
    //           <option value="AB">AB</option>
    //         <option value="BM">BM</option>
    //         <option value="DB">DB</option>
    //         <option value="FW">FW</option>
    //         <option value="SM">SM</option>
    //         <option value="SS">SS</option>
    //       </select>`;

    // #### get the table_length filter
    var div = document.getElementById("table2_length");

    // #### get the table search
    var search = document.getElementById("table2_filter");

    // var search_input = search_label.firstChild;
    // search_input.placeholder = "Search";
    //   insertAfter(div, el);
    div.style.marginLeft = "1px"
    search.style.marginRight = "5px"

    // #### get parent of the table_search
    var parent = div.parentNode;

    // Create and add a new wrapper div
    var wrapper = document.createElement('div');
    wrapper.classList.add("row")

    c1 = document.createElement("div")
    c1.classList.add("col-6")
    // c1.classList.add("col-md-4")
    div.classList.add("form-inline")
    div.getElementsByTagName("select").item(0).style.margin="5px"

    // c2 = document.createElement("div")
    // c2.classList.add("col-12")
    // c2.classList.add("col-md-4")

    c3 = document.createElement("div")
    c3.classList.add("col-6")
    // c3.classList.add("col-md-4")

    // #### insert wrapper element
    parent.replaceChild(wrapper, div);
    // #### set elements as childrens of wrapper
    wrapper.appendChild(c1);
    // wrapper.appendChild(c2);
    wrapper.appendChild(c3);
    c1.appendChild(div)
    // c2.appendChild(el)
    c3.appendChild(search)

    div.firstElementChild.firstElementChild.style.maxHeight="36px"
    div.firstElementChild.classList.add("d-flex")
    // div.firstElementChild.style.marginTop="6px"
    div.firstElementChild.style.alignItems="center"
    div.firstElementChild.style.marginBottom="0px"
    div.firstElementChild.style.marginTop="0px"

    search.parentElement.style.margin="auto"
    search.firstChild.style.marginBottom="0px"
    search.style.marginTop="0px"
    
    $(search.firstChild).contents().filter(function(){
        return (this.nodeType == 3);
    }).remove();

    search.firstChild.firstChild.placeholder="Search"
    search.firstChild.firstChild.style.maxWidth="30vw"

    // #### for filter function 
    var table = $(`#table1`).DataTable();
    
    // #### hide team member's details 
    table.columns([9,10,11,12,13,14,15,16]).visible(false);

    // #### add event listener for the filter 
    $('#min, #max').keyup( function() {
        table.draw();
    } );

    // #### wrapper for table1
    tb2 = document.getElementById("table1");
    var p_tag = tb2.parentNode;
    // console.log(p_tag);
    var w_tag = document.createElement('div');
    // set the wrapper as child (instead of the element)
    p_tag.replaceChild(w_tag, tb2);
    // set element as child of wrapper
    w_tag.appendChild(tb2);
    // w_tag.style.maxHeight = "300px";
    // w_tag.style.display = "block";
    // w_tag.style.overflow = "auto";
    // w_tag.style.marginTop = "10px";
    w_tag.style.cssText += 'max-height:300px;'
                            + 'display:block;'
                            + 'overflow:auto;'
                            + 'margin-top:10px;';

    // #### wrapper for table2
    tb2 = document.getElementById("table2");
    var p_tag = tb2.parentNode;
    // console.log(p_tag);
    var w_tag = document.createElement('div');
    // set the wrapper as child (instead of the element)
    p_tag.replaceChild(w_tag, tb2);
    // set element as child of wrapper
    w_tag.appendChild(tb2);
    // w_tag.style.maxHeight = "300px";
    // w_tag.style.display = "block";
    // w_tag.style.overflow = "auto";
    // w_tag.style.marginTop = "10px";
    w_tag.style.cssText += 'max-height:300px;'
                            + 'display:block;'
                            + 'overflow:auto;'
                            + 'margin-top:10px;';

}

// #### for dynamic naming of predicted table download
const getPredText = () => {
    return `${task_name}_Predicted_${text}`;
}

// #### for dynamic naming of submitted table download
const getSubText = () => {
    return `${task_name}_Submitted_${text}`;
}

// #### function to hide/show team members details
const toggleColumns = () =>{
    var table = $(`#table1`).DataTable();
    var toggle_switch = document.getElementById("toggle_switch");
    // console.log(toggle_switch)
    
    // #### text is to show then make columns visible and change text to hide
    if(toggle_switch.innerText==="Show Member Details"){
        toggle_switch.innerText="Hide Columns"
        table.columns([9,10,11,12,13,14,15,16]).visible(true);
    }
    else{
        // #### text is hide then hide columns and change text to show
        toggle_switch.innerText="Show Member Details"
        table.columns([9,10,11,12,13,14,15,16]).visible(false);
    }

    // #### make css changes
    toggle_switch.classList.toggle("btn-outline-info");
    toggle_switch.classList.toggle("btn-outline-success");
    // table.draw()
}



setTimeout(function(){ 
    // console.log(data["time_stamp"][0])
    var time_stamp = Date.parse(data["time_stamp"][0]);
    time_passed.innerText= parseInt((Date.now() - time_stamp)/60000-330);
    // console.log(time_stamp)
    // console.log((Date.now() - time_stamp)/60000-330)
    if(((Date.now() - time_stamp)/60000-330) > 60)
    {
        update_chart_data()
    }
}, 5000);

setInterval(function(){ 
    var time1 = time_passed.innerText;
    time1 = parseInt(time1);
    time1 = time1 + 1;
    time_passed.innerText = time1;
    if (time1===60) {
        update_chart_data()
    }
 }, 60*1000);

// #### function to filter team wise
const filter_data = (id) => {
    // #### select the required datatable
    var table = $(`#table${id}`).DataTable();

    // #### the the theme selected
    // text = document.getElementById(`theme${id}`).value;
    // text = nav_theme;

    // #### if selected is all
    if (text === "ALL") {
        table.search("");
    } else {
        // #### if selected is not all
        table.search(text);
    }
    table.draw();
}

// ########################################   Table Functions Ends ###################################################