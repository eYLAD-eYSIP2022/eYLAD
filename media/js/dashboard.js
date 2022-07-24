// #### Our code starts here
// #### declare global variables
var curr_task=0,box_data;

// #### Declaring Global Variables
var data, y, conf, result, expnotsub, box_data, tableCells, token, conftype=["table-success", "table-warning", "table-danger"], new_rows,threshold, predthis, text = "ALL";
var  feedback_data,total_submissions = 0,this_task;
var team_status=["seen", "unseen"];
const theme_list = JSON.parse(localStorage.getItem("theme_list"));
console.log(theme_list, typeof(theme_list));
let mychart = document.getElementById("barChart2").getContext('2d');
var table = false
var threshold = JSON.parse(localStorage.getItem("thresh"));
threshold = parseFloat(threshold)
var parameters = JSON.parse(localStorage.getItem("parameters"));
var data = JSON.parse(localStorage.getItem("json_data"));
var this_task;
// console.log("{{this_task|es}}");
this_task = JSON.parse(localStorage.getItem("this_task"));
console.log(data, this_task);
var discourse_topics = JSON.parse(localStorage.getItem("discourse_topics"));
// console.log(discourse_topics);
var discourse_categories = JSON.parse(localStorage.getItem("discourse_categories"));
var current_task_no = localStorage.getItem("current_task");
// console.log(discourse_topics);
// console.log(discourse_categories);
let bargra = false;
let category_selector = document.getElementById("category_select");
let topic_selector = document.getElementById("topic_select");
var key_value = {
    'ALL':0,
    'AB':1,
    'BM':2,
    'DB':3,
    'FW':4,
    'SM':5,
    'SS':6
};
// Selected Teams list for sending emails
var selected_teams=[];
var accepted_email_list=[];

let nav_theme = document.getElementById("main_theme").value;
document.getElementById(`comment_title`).innerText = `${nav_theme} Feedback Comments`;
// doughnutChart();
const theme_change = () => {
    nav_theme = document.getElementById("main_theme").value;
    document.getElementById(`comment_title`).innerText = `${nav_theme} Feedback Comments`;
    // nav_theme = "BM";
    updateDoughnutChart();
    // console.log(total_submissions, result.length, expnotsub)
    updateOnChange();
    updateOnChange_topic();
    updateOnChange_comment();
}

console.log(nav_theme)
// console.log(discourse_categories)
// console.log(discourse_topics)
// Appending option tags in HTML of "Select Topic" of "Informed Teams Counter" table
Object.keys(discourse_categories["name"]).forEach((val,index)=>{
    let new_option = document.createElement("option")
    new_option.innerText=discourse_categories["name"][val]
    // console.log(discourse_categories["name"][val])
    new_option.value=discourse_categories["category_id"][val]
    category_selector.appendChild(new_option)
})
// category_selector.appendChild()
$(document).ready( function () {
    $.noConflict();
    
} );

const updateOnChange_category = () =>{
    let select_option = category_selector.value
    console.log(select_option)

    let new_option = document.createElement("option")
    new_option.innerText="Select Topic"
    new_option.value="-5"

    topic_selector.innerHTML=''
    topic_selector.appendChild(new_option)

    // console.log(discourse_topics["title"]);
    Object.keys(discourse_topics["title"]).forEach((val,index)=>{
        // console.log({"value":val,"title":discourse_topics["title"][val],"id":discourse_topics["id"][val],"category":discourse_topics["category_id"][val]})
        if (select_option == discourse_topics["category_id"][val]) {
            let new_option = document.createElement("option")
            new_option.innerText=discourse_topics["title"][val]
            new_option.value=discourse_topics["id"][val]
            topic_selector.appendChild(new_option)            
        }
    })
}


const getPredText = () => { 
    return `${topic_selector.options[topic_selector.selectedIndex].innerText}_${nav_theme}_Seen_unseen`;
}

const updateOnChange_topic = () =>{
    if ((category_selector.value > -1) &&(topic_selector.value > -1)) {
        // console.log(topic_selector.value)
        $('#table3').DataTable().clear();
        document.getElementById("informed_teams").style.display="none";
        document.getElementById("informed_teams_loader").style.display="block";
        $.ajax({
            // #### URL and datatype for ajax call
            url: `/get-seen-teams/${topic_selector.value}/`,
            dataType: 'json',
            // #### Success function
            success: function (suc_data) {
                // #### Converting data in json format
                let seen_teams = JSON.parse(suc_data.seen_teams)
                let unseen_teams=JSON.parse(suc_data.unseen_teams)

                console.log({seen_teams,unseen_teams})
                // console.log(seen_teams.email)

                let seen_list = Object.keys(seen_teams.theme).filter((val,index)=>{
                    if (nav_theme=="ALL") {
                        return seen_teams.team_id[val]
                    }
                    else if(seen_teams.theme[val]==nav_theme)
                    {
                        return seen_teams.team_id[val]
                    }
                    else return false;
                })

                let unseen_list = Object.keys(unseen_teams.theme).filter((val,index)=>{
                    if (nav_theme=="ALL") {
                        return unseen_teams.team_id[val]
                    }
                    else if(unseen_teams.theme[val]==nav_theme)
                    {
                        return unseen_teams.team_id[val]
                    }
                    else return false;
                })
                let count_seen = seen_list.length
                let count_unseen = unseen_list.length 
                if (bargra!==false) {
                    bargra.destroy();
                    console.log("destroyed the prev_canvas");
                }
                // ########################################   Bar Chart Start ###################################################
                // #### Bar chart Constructor
                bargra = new Chart(mychart, {
                    type: 'bar',
                    data: {
                        // #### Bar chart labels on X axis i.e. theme names
                        labels: [""],

                        // #### Data 1 for all teams who submitted this task
                        datasets: [{
                            label: 'Seen Task',
                            data: [count_seen],
                            borderColor: [`rgba(97, 216, 216, 1)`],
                            backgroundColor: [`rgba(0, 175, 185, 1)`],
                            stack: "Stack 0"
                        },
                        // #### Data 2 for teams submitted prev task
                        {
                            label: 'Not Seen Task',
                            data: [count_unseen],
                            borderColor: [`rgba(255,0,0,1)`],
                            backgroundColor: [`rgba(240, 113, 103, 1)`],
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
                        // #### Title of chart
                        title: {
                            display: true,
                            text: `Teams Seen Topic List`

                        },
                        responsive: true,
                        scales: {
                            xAxes: [{
                                stacked: true // #### this should be set to make the bars stacked
                            }],
                            yAxes: [{
                                stacked: false // #### this also..
                            }]
                        }
                    }
                })
                // ########################################   Bar Chart Ends #########################################
                $('#unseen-teams')[0].checked=false;
                $('#seen-teams')[0].checked=false;
                table = $(`#table3`).DataTable({
                    dom: 'Blfrtip',
                    destroy: true,
                    // #### buttons for datatable download
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
                            sFirst: '<<',
                            sLast: '>>'
                        }
                        } ,
                    // #### for search bar in footer
                    initComplete: function () {
                        // #### Apply the search
                        this.api().columns().every( function () {
                            var that = this;
                
                            $('#table3_search input', this.footer() ).on( 'keyup change clear', function () {
                                if( that.search() !== this.value ) {
                                    that
                                        .search( this.value )
                                        .draw();
                                }
                            });
                        });
                    },
                    columnDefs: [ {
                        orderable: false,
                        className: 'select-checkbox',
                        targets:   0
                    } ],
                    select: {
                        style:    'multi',
                        selector: 'td'
                    },
                    order: [[ 1, 'asc' ]],

                });

                Object.keys(seen_teams.team_id).forEach((val,index)=>{
                    if (nav_theme=="ALL"||seen_teams.theme[val]==nav_theme) {
                        var temp = [];
                        temp.push('<td></td>');
                        temp.push(seen_teams.team_id[val]);
                        temp.push('Seen by teams');
                        temp.push(seen_teams.name[val]);
                        temp.push(seen_teams.email[val]);
                        temp.push(seen_teams.contact[val]);
                        var tmp = table.row.add(temp).node();
                        // console.log(tmp);
                        $(tmp).addClass("table-success seen");
                    }
                }); 
                
                Object.keys(unseen_teams.team_id).forEach((val,index)=>{
                    if (nav_theme=="ALL"||unseen_teams.theme[val]==nav_theme) {
                        var temp = [];
                        temp.push('<td></td>');
                        temp.push(unseen_teams.team_id[val]);
                        temp.push('Unseen by teams');
                        temp.push(unseen_teams.name[val]);
                        temp.push(unseen_teams.email[val]);
                        temp.push(unseen_teams.contact[val]);
                        var tmp = table.row.add(temp).node();
                        // console.log(tmp);
                        $(tmp).addClass("table-danger unseen");
                    }
                }); 
                
                console.log("Table reinitialized");
                // To select/deselect "Seen teams" when checkbox in checked/unchecked
                $('#seen-teams').click(function() {
                    console.log($('#seen-teams')[0].checked);
                    if ($('#seen-teams')[0].checked) {
                        table.rows('.seen').select();
                    }
                    else {
                        table.rows('.seen').deselect();
                    }
                });

                // To select/deselect "Unseen teams" when checkbox in checked/unchecked
                $('#unseen-teams').click(function() {
                    console.log($('#unseen-teams')[0].checked);
                    if ($('#unseen-teams')[0].checked) {
                        table.rows('.unseen').select();
                    }
                    else {
                        table.rows('.unseen').deselect();
                    }
                });
                
                $('#MyTableCheckAllButton').click(function() {
                    if (table.rows({
                            selected: true
                        }).count() > 0) {
                        table.rows().deselect();
                        $('#unseen-teams')[0].checked=false;
                        $('#seen-teams')[0].checked=false;
                        return;
                    }
                    table.rows().select();
                });
            
                table.on('select deselect', function(e, dt, type, indexes) {
                    if (type === 'row') {
                        // We may use dt instead of myTable to have the freshest data.
                        if (dt.rows().count() === dt.rows({
                                selected: true
                            }).count()) {
                            // Deselect all items button.
                            $("#table-checkbox").attr('d', 'M19,19H5V5H15V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V11H19M7.91,10.08L6.5,11.5L11,16L21,6L19.59,4.58L11,13.17L7.91,10.08Z');
                            $('#seen-teams').prop('checked', true);
                            $('#unseen-teams').prop('checked', true);
                            // console.log("Select All " , $('#seen-teams')[0].checked);
                            return;
                        }
            
                        if (dt.rows({
                                selected: true
                            }).count() === 0) {
                            // Select all items button.
                            $("#table-checkbox").attr("d", "M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M19,5V19H5V5H19Z");
                            // console.log("Deselect All ", $('#seen-teams')[0].checked);
                            return;
                        }
            
                        // Deselect some items button.
                        $("#table-checkbox").attr('d', 'M19,19V5H5V19H19M19,3A2,2 0 0,1 21,5V19A2,2 0 0,1 19,21H5A2,2 0 0,1 3,19V5C3,3.89 3.9,3 5,3H19M17,11V13H7V11H17Z');
                    }
                });

                $("#draft-mail,#email-copy").click(function(){
                    selected_teams=[];
                    var rows_selected = table.rows('.selected').data();
                    $.each(rows_selected,function(i,v){
                        selected_teams.push([v[1], v[4]]);
                    });
                    console.log(selected_teams)
                    document.getElementById("alertSubmit").disabled=true;
                });

                table.on( 'draw', function () {
                    // console.log( 'Redraw occurred at: '+new Date().getTime() );
                    document.getElementById("informed_teams_loader").style.display="none";
                    document.getElementById("informed_teams").style.display="block";
                } );

                var mybuttons = $("#informed_teams").find(".dt-button")
                setTimeout(() => {
                    style_buttons(mybuttons);
                    style_table("table3");
                }, 2000);
                table.draw();
            }
        })
    }
}


function ValidateEmail(input) {
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    console.log("Validate Email: ", input);
    if (String(input).match(validRegex)) {
        // alert("Valid email address!");
        return true;
    } else {
        // alert("Invalid email address!");
        return false;
    }
}

$("#email-copy").click(function(){
    var copy_email=[];
    var rows_selected = table.rows('.selected').data();
    $.each(rows_selected,function(i,v){
        if(ValidateEmail(v[4])) {
            copy_email.push(v[4]);
        } 
    });
    navigator.clipboard.writeText(copy_email);
    // console.log(copy_email);

    /* Alert the copied text */
    alert("Emails copied successfully!!");
    console.log("Copied Emails: ", copy_email)
});

// ########################################   Alert To confirm the "Team IDs"   #########################################
$('#alertEmail').on('show.bs.modal', function (event) {
    console.log("Selected Teams: ", selected_teams);
    // selected_teams_len = selected_teams.length
    document.getElementById("alertTitle").innerHTML = `Total of ${selected_teams.length} team(s) selected`;
    console.log("Selected teams length: ", selected_teams.length);
    var rejected_email = '';
    var num_rejected_email = 0;
    accepted_email_list = []
    // var accepted_email = '';
    
    Object.keys(selected_teams).forEach((val,index)=>{
        // Filtering faulty emails
        console.log("Looping on: ", selected_teams[index], val, typeof(index));
        if(ValidateEmail(selected_teams[index][1])) {
            accepted_email_list.push(selected_teams[index])
            console.log("Accepted Email", selected_teams[index]);
        }
        else {
            num_rejected_email += 1;
            rejected_email += '<tr><th scope="row">'+ num_rejected_email + '</th>'+
                                '<td>'+ selected_teams[index][0] +'</td>'+
                                '<td>'+ selected_teams[index][1] +'</td></tr>';
            console.log("Rejected Email", selected_teams[index]);
        }
    })
    document.getElementById("rejectedEmailBtn").innerHTML=`Number of emails rejected: ${ (selected_teams.length)-(accepted_email_list.length) }`;
    // document.getElementById("acceptedEmailBtn").innerHTML=`Number of emails accepted: ${ (accepted_email_list.length) }`;
    document.getElementById("rejectedEmailList").innerHTML=rejected_email;
    console.log(accepted_email_list);
    if (accepted_email_list.length > 0) {
        document.getElementById("alertSubmit").disabled=false;
    }
});

// For form validation, add "needs-validation" to the form tag and "required" to input tag
//    to skip validation add class "no-validate" to that particulat input tag 
(function () {
    'use strict'
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
    var btn = document.getElementById('draftEmailSubmit')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
        btn.addEventListener('click', function (event) {
            if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
            }
            form.classList.add('was-validated')
        }, false)
        })
})()

// AJAX to send data for the email to views.py
$('#draftEmailSubmit').on('click', function() {
    var cc = $('#draftEmail-cc').val();
    var bcc = $('#draftEmail-bcc').val();
    var sub = $('#draftEmail-sub').val();
    var msg = $('#draftEmail-msg').val();
    console.log(cc, "\n", bcc, "\n", sub, msg);
    $.ajax({
        type: 'POST',
        url: '/email/',
        data: {
            'emails': JSON.stringify(accepted_email_list),
            'cc': cc,
            'bcc': bcc,
            'sub': sub,
            'msg': msg,
        },
    }).done(function(data) {
        console.log(data);
        if (data == 'Success') {
            alert("Emails have been sent successfully !!")
        }
        else {
            alert("Failed to send Emails !!")
        }
    });
});

// ########################################   Task Prediction Start #########################################

// #### Initialize the semi-empty Doughnut Chart data object
var DoughchartData = {}
for (var j=0; j<theme_list.length; j++) {
    DoughchartData[theme_list[j]] = [0, 0, 0];
    // Initialize the number of teams submitted
    DoughchartData[theme_list[j]][0] = this_task[theme_list[j]];
    // console.log(DoughchartData);
}
console.log(DoughchartData);

// #### Populate data object for rest of the themes
const setBarData=(data,y,threshold)=>{
    console.log(DoughchartData.length, data, y, threshold);
    for (var i = 0; i < y.length; ++i) {
        console.log(i);
        if (data["confidence"][i] > threshold) {
            console.log(DoughchartData[data['theme'][i]][1]);
            DoughchartData[data['theme'][i]][1] += 1;
        }
        else {
            console.log(DoughchartData[data['theme'][i]]);
            DoughchartData[data['theme'][i]][2] += 1;
        }
    }
    console.log(DoughchartData[nav_theme][0], DoughchartData[nav_theme][1], DoughchartData[nav_theme][2]);
}

// #### Function to update doughnut chart based on theme-change
const updateDoughnutChart=()=>{
    // #### update doughnut chart
    doughnutChart.data.datasets[0].data[0] = DoughchartData[nav_theme][0];
    doughnutChart.data.datasets[0].data[1] = DoughchartData[nav_theme][1];
    doughnutChart.data.datasets[0].data[2] = DoughchartData[nav_theme][2];
    console.log(DoughchartData[nav_theme][0], DoughchartData[nav_theme][1], DoughchartData[nav_theme][2]);
    doughnutChart.update();
}

// #### Threshold for this model
threshold = parseFloat(threshold)

// #### Calculate data for doughnut chart
y = Object.values(data["team_id"])

// #### Set table loading spinners to none
document.getElementById("spinner_home1").style.display = "none";

// Call the function to populate the Doughnut data object
setBarData(data,y,threshold)

const config = {
    type: 'doughnut',
    data: {
        labels: [
            'Teams Submitted', 
            'Teams expected to submit', 
            'Teams not expected to submit'
        ],
        datasets: [{
            label: 'Task Status',
            data: [
                DoughchartData[nav_theme][0], 
                DoughchartData[nav_theme][1], 
                DoughchartData[nav_theme][2]
            ],
            backgroundColor: [
                "#00AFB9", 
                "#0081A7", 
                "#F07167"
            ],
            hoverOffset: 10
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: `Task ${current_task_no} Prediction`,
                font: {
                    size: 24
                }
            }
        }
    }
}

const doughnutChart = new Chart(
    document.getElementById('myChart'),
    config,
    console.log(DoughchartData[nav_theme][0], DoughchartData[nav_theme][1], DoughchartData[nav_theme][2])
);
// ########################################   Task Prediction Ends  #########################################


// ########################################   Feedback Starts  #########################################
// #### ajax for the box chart
$.ajax({
    // #### URL and Datatype for ajax call
    url: `/feedbackdata/0/`,
    dataType: 'json',
    success: function (suc_data) {
        // #### parsing json data
        box_data = JSON.parse(suc_data.box_chart_data)
        //  console.log(box_data)
        delete box_data.Entries;
        // #### clear the box chart element
        document.getElementById("box_chart").innerHTML="";

        // #### get theme name from select
        //   var val_index = document.getElementById(`feedback_select`).value;
        document.getElementById(`feedback_title`).innerText = `${nav_theme} Task 0 Feedback`;
        console.log(box_data);
        // #### create array of data in required format
        var data = Object.keys(box_data).map((obj1,index1)=>{
            return(
                {
                x:obj1,
                low :box_data[obj1][`('${nav_theme}', 0.0)`],
                q1 : box_data[obj1][`('${nav_theme}', 0.25)`],
                median : box_data[obj1][`('${nav_theme}', 0.5)`],
                q3 : box_data[obj1][`('${nav_theme}', 0.75)`],
                high : box_data[obj1][`('${nav_theme}', 1.0)`]
                }
            )
        })
        console.log(data)
    
        // #### Create chart object and set the data
        chart = anychart.box();
        series = chart.box(data);
        // #### style box chart
        series.whiskerWidth(30);
        series.normal().whiskerStroke("#000", 0.5);
        series.hovered().whiskerStroke("#000", 1);
        series.selected().fill("#ff3b55", 2);
        series.hover().fill("#ff3b55", 1);
        series.normal().fill("#ff3b55", 0.5);
        series.selected().stroke("#b03e00", 2);
        series.normal().stroke("#b03e00", 0.5);
        console.log(series)
        series.normal().stemStroke("#000", 0.5);
        series.hovered().stemStroke("#000", 1);
        series.selected().stemStroke("#000", 2);
        var xAxis = chart.xAxis();
        xAxis.staggerMode(2);
        chart.yScale().maximum(6);
        chart.yScale().ticks().interval(1);
        // #### Create box chart
        chart.container("box_chart");
        chart.draw();
    }
})

const updateOnChange = () =>{
    // #### get task name from select
    console.log("Changed task");
    var new_task = parseInt(document.getElementById(`task_select`).value);
    if (new_task !== curr_task) {
        curr_task=new_task
        // console.log(typeof(curr_task));
        $.ajax({
            // #### URL and Datatype for ajax call
            url: `/feedbackdata/${new_task}/`,
            dataType: 'json',
            success: function (suc_data) {
                // #### parsing json data
                box_data = JSON.parse(suc_data.box_chart_data)
                console.log(box_data)
                // console.log(suc_data.legend)
                document.getElementById("legend").innerHTML=suc_data.legend;
                delete box_data.Entries;
                // #### clear the box chart element
                document.getElementById("box_chart").innerHTML=" ";

                // #### get theme name from select
                // var val_index = document.getElementById(`feedback_select`).value;
                if (new_task==6 || new_task==7 || new_task==8 || new_task==9) {
                    document.getElementById(`feedback_title`).innerText = `${nav_theme} Task Stage 1 Feedback`;
                } else {
                    document.getElementById(`feedback_title`).innerText = `${nav_theme} Task ${new_task} Feedback`;
                }
              
      
                // #### create array of data in required format
                var data = Object.keys(box_data).map((obj1,index1)=>{
                    // console.log(
                    //     {
                    //         x:obj1,
                    //         val_index:val_index,
                    //         val:`('${val_index}', 0.0)`,
                    //         low :box_data[obj1][`('${val_index}', 0.0)`],
                    //         q1 : box_data[obj1][`('${val_index}', 0.25)`],
                    //         median : box_data[obj1][`('${val_index}', 0.5)`],
                    //         q3 : box_data[obj1][`('${val_index}', 0.75)`],
                    //         high : box_data[obj1][`('${val_index}', 1.0)`]
                    //     }
                    // )
                    return({
                        x:obj1,
                        low :box_data[obj1][`('${nav_theme}', 0.0)`],
                        q1 : box_data[obj1][`('${nav_theme}', 0.25)`],
                        median : box_data[obj1][`('${nav_theme}', 0.5)`],
                        q3 : box_data[obj1][`('${nav_theme}', 0.75)`],
                        high : box_data[obj1][`('${nav_theme}', 1.0)`]
                    })
                })
          
                // #### Create chart object and set the data
                chart = anychart.box();
                //  var legend = chart.legend();
                // // enable legend
                // legend.enabled(true);
                // legend.itemsSourceMode("categories");
                series = chart.box(data);
                // #### style box chart
                series.whiskerWidth(30);
                series.normal().whiskerStroke("#000", 0.5);
                series.hovered().whiskerStroke("#000", 1);
                series.selected().fill("#ff3b55", 2);
                series.hover().fill("#ff3b55", 1);
                series.normal().fill("#ff3b55", 0.5);
                series.selected().stroke("#b03e00", 2);
                series.normal().stroke("#b03e00", 0.5);
                console.log(series)
                series.normal().stemStroke("#000", 0.5);
                series.hovered().stemStroke("#000", 1);
                series.selected().stemStroke("#000", 2);
                var xAxis = chart.xAxis();
                xAxis.staggerMode(2);
                chart.yScale().maximum(6);
                chart.yScale().ticks().interval(1);
                // #### Create box chart
                chart.container("box_chart");
                chart.draw();
            }
        })
    } 
    else {
        // #### clear the box chart element
        document.getElementById("box_chart").innerHTML=" ";

        // #### get theme name from select
        //   var val_index = document.getElementById(`feedback_select`).value;
        document.getElementById(`feedback_title`).innerText = `${nav_theme} Task ${curr_task} Feedback`;
      
        // #### create array of data in required format
        var data = Object.keys(box_data).map((obj1,index1)=>{
            return(
                {
                    x:obj1,
                    low :box_data[obj1][`('${nav_theme}', 0.0)`],
                    q1 : box_data[obj1][`('${nav_theme}', 0.25)`],
                    median : box_data[obj1][`('${nav_theme}', 0.5)`],
                    q3 : box_data[obj1][`('${nav_theme}', 0.75)`],
                    high : box_data[obj1][`('${nav_theme}', 1.0)`]
                }
            )
        })
      
        // #### Create chart object and set the data
        chart = anychart.box();
        series = chart.box(data);
        // #### style box chart
        series.whiskerWidth(30);
        series.normal().whiskerStroke("#000", 0.5);
        series.hovered().whiskerStroke("#000", 1);
        series.selected().fill("#ff3b55", 2);
        series.hover().fill("#ff3b55", 1);
        series.normal().fill("#ff3b55", 0.5);
        series.selected().stroke("#b03e00", 2);
        series.normal().stroke("#b03e00", 0.5);
        console.log(series)
        series.normal().stemStroke("#000", 0.5);
        series.hovered().stemStroke("#000", 1);
        series.selected().stemStroke("#000", 2);
        var xAxis = chart.xAxis();
        xAxis.staggerMode(2);
        chart.yScale().maximum(6);
        chart.yScale().ticks().interval(1);
        // #### Create box chart
        chart.container("box_chart");
        chart.draw();
    }
}


// #### for dynamic naming of comment table download
const getComText = (theme, task) => {
    return `${theme}_Comments_${task}`;
}

const updateOnChange_comment = () =>{
    $("#comment").css("display", "none");
    $("#toggle_switch").css("display", "none");
    var table=$('#commentsTable').DataTable()
    table.destroy();
    var new_task = parseInt(document.getElementById(`comment_task_select`).value);
    if(new_task === -5){
        $("#comment").css("display", "none");
        document.getElementById(`comment_title`).innerText = `${nav_theme} Feedback Comments`;
        document.getElementById("comments_loader").style.display="none";
    }
    else {
        document.getElementById("comments_loader").style.display="block";
        curr_task=new_task
        if (new_task==6 || new_task==7) {
            document.getElementById(`comment_title`).innerText = `${nav_theme} Stage ${new_task-5} Feedback Comments`;
        } else {
            document.getElementById(`comment_title`).innerText = `${nav_theme} Task ${new_task} Feedback Comments`;
        }
        // $('#commentsTable').DataTable().clear();
        var trHTML = '';
        $.ajax({
            // #### URL and datatype for ajax call
            url: `/get-comments/${new_task}/`,
            dataType: 'json',
            // #### Success function
            success: function (suc_data) {
                // #### Converting data in json format
                let taskComments = JSON.parse(suc_data.task_comments)
                //console.log(taskComments)

                Object.keys(taskComments.team_member_id).forEach((val,index)=>{
                    if (taskComments.theme[val]==nav_theme) {
                        trHTML += "<tr class='table-success seen'>"+
                    '<td>' + taskComments.team_member_id[val]+
                    '</td><td>' + taskComments.team_id[val] +
                    '</td><td>' + taskComments.theme[val] +
                    '</td><td>' + taskComments.name[val] +
                    `</td><td id="comm_col" style="text-align: left; white-space: break-spaces;">` + taskComments.comment[val] +
                    '</td></tr>';
                    } 
                })
                $("#commentTableContent").html(trHTML)
                $(document).ready(function () {
                    var table=$('#commentsTable').DataTable({
                        dom: 'Blfrtip',
                        destroy: true,
                        // #### buttons on tables download option
                        buttons: [
                            'copyHtml5',
                            {
                                extend: 'pdfHtml5',
                                title: function () { return getComText(nav_theme, new_task); }
                            },
                            {
                                extend: 'excelHtml5',
                                title: function () { return getComText(nav_theme, new_task); }
                            },
                            {
                                extend: 'csvHtml5',
                                title: function () { return getComText(nav_theme, new_task); }
                            }
            
                        ],
                        // #### function for search on footer
                        initComplete: function () {
                            // #### Apply the search
                            this.api().columns().every( function () {
                                var that = this;
                
                                $('#commentsTable', this.footer() ).on( 'keyup change clear', function () {
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
                    var mybuttons = $("#comment").find(".dt-button");
                    table.columns([0,1,2,3]).visible(false);
                    setTimeout(() => {
                        style_buttons(mybuttons);
                        style_table("commentsTable");
                        document.getElementById("comments_loader").style.display="none";
                        $("#comment").css("display", "block");
                        table.columns([0,1,2,3]).visible(false);
                        $("#toggle_button_holder").html('<button type="button" id="toggle_switch" class="btn btn-outline-success" onclick="toggleColumns()" style="display: inline-block;">Show Details</button>');
                        $("#toggle_switch").css("display", "block");
                    }, 2000);
                })
            }
        })
    }
}

const toggleColumns = () =>{
    var table = $(`#commentsTable`).DataTable();
    var toggle_switch = document.getElementById("toggle_switch");
    // console.log(toggle_switch)
    
    // #### text is to show then make columns visible and change text to hide
    if(toggle_switch.innerText==="Show Details"){
        toggle_switch.innerText="Hide Details";
        table.columns([0,1,2,3]).visible(true);
    }
    else{
        // #### text is hide then hide columns and change text to show
        toggle_switch.innerText="Show Details";
        table.columns([0,1,2,3]).visible(false);
    }

    // #### make css changes
    toggle_switch.classList.toggle("btn-outline-info");
    toggle_switch.classList.toggle("btn-outline-success");
    // table.draw()
}

// #### function for getting quotes on dashboard
$.getJSON('https://api.allorigins.win/get?url=' + encodeURIComponent('https://api.quotable.io/random?tags=technology,famous-quotes'), function (data) {
    // alert(data.contents);
    suc_data = JSON.parse(data.contents)
    // console.log(suc_data);
    // #### set data quote element
    document.getElementById("quotes").innerText =suc_data.content
    document.getElementById("author").innerText = "-  "+suc_data.author
});

// console.log(discourse_topics)


const style_buttons = (buttons) => {
    // console.log(buttons)
    // buttons.style.display="flex"
    // var button_box = document.getElementsByClassName("dt-buttons")[0]
    // button_box.style.display="flex"
    // button_box.style.justifyContent="space-evenly"
    // button_box.style.margin="5px"

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

const style_table = (table_id) => {

        // #### get the table length filter
        var table_len = document.getElementById(`${table_id}_length`);
        // #### get the table search
        var table_filter = document.getElementById(`${table_id}_filter`);
        
        table_len.style.marginLeft = "1px";
        table_filter.style.marginRight = "15px";

        var parent = table_len.parentNode;
    
        // Create and add a new wrapper div
        var wrapper = document.createElement('div');
        wrapper.classList.add("row")
        
        c1 = document.createElement("div")
        c1.classList.add("col-6")
        // c1.classList.add("col-md-4")
        table_len.classList.add("form-inline")
        table_len.getElementsByTagName("select").item(0).style.margin="5px"
        // table_len.childNodes[0].childNodes[0].
    
        // c2 = document.createElement("div")
        // c2.classList.add("col-12")
        // c2.classList.add("col-md-4")
    
        c3 = document.createElement("div")
        c3.classList.add("col-6")
        // c3.classList.add("col-md-4")
        
        // #### insert wrapper element
        parent.replaceChild(wrapper, table_len);
    
        // #### set elements as childrens of wrapper
        wrapper.appendChild(c1);
        // wrapper.appendChild(c2);
        wrapper.appendChild(c3);
        c1.appendChild(table_len)
        // c2.appendChild(el)
        c3.appendChild(table_filter)
    
        table_len.firstElementChild.firstElementChild.style.maxHeight="36px"
        table_len.firstElementChild.classList.add("d-flex")
        table_len.firstElementChild.style.marginTop="6px"
        table_len.firstElementChild.style.alignItems="center"
        table_len.firstElementChild.style.marginBottom="0px"
        table_len.firstElementChild.style.marginTop="0px"


        table_filter.parentElement.style.margin="auto"
        table_filter.firstChild.style.marginBottom="0px"
        table_filter.style.marginTop="0px"
        
        $(table_filter.firstChild).contents().filter(function(){
            return (this.nodeType == 3);
        }).remove();

        table_filter.firstChild.firstChild.placeholder="Search"
        table_filter.firstChild.firstChild.style.maxWidth="30vw"
        table_filter.firstChild.firstChild.setAttribute('id','table3_search');

        // #### wrapper for table
        tb2 = document.getElementById(`${table_id}`);
        var p_tag = tb2.parentNode;
        console.log(p_tag);
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
                                + 'margin-top:10px;'
                                + 'border: 1px solid #9d9d9da6;'
                                + 'box-shadow: 0px 0px 2px #9d9d9d;';
    

}

// const checkbox_1 = $.querySelector("#t3-seen-teams");
// checkbox_1.addEventListner("change",(e) => {
//     console.log(e.target.value);
// })
const seen_teams = (e) => {
    return true;
}
// $.getJSON('https://api.allorigins.win/get?url=' + encodeURIComponent('https://www.metaweather.com/api/location/12586539/'), function (data) {
//     // alert(data.contents);
//     suc_data = JSON.parse(data.contents)
//     // console.log(suc_data);
//     // #### Set temperature in dashboard
//     document.getElementById("temperature").innerText = parseInt(suc_data.consolidated_weather[0].the_temp)

// });

// $.ajax({
//     url: `https://cors-proxy.htmldriven.com/?url=https://www.metaweather.com/api/location/12586539/`,
//     dataType: 'json',
//     success: function (suc_data) {
//         console.log(suc_data)
//         document.getElementById("temperature").innerText = parseInt(suc_data.consolidated_weather[0].the_temp)
//     }

// })


// $.ajax({
//     url: `https://cors-proxy.htmldriven.com/?url=https://api.quotable.io/random?tags=technology,famous-quotes`,
//     dataType: 'json',
//     success: function (suc_data) {
//         console.log(suc_data)
//         document.getElementById("quotes").innerText =suc_data.content
//         document.getElementById("author").innerText = "-  "+suc_data.author

//     }

// })

// $('')

//  PERFORMANCE GRAPH --> ON HOLD   //

// function performanceGraph
// var performance_task=0;
// var performance_sub_task=0;
// $.ajax({
//     url: `/performance/${nav_theme}/${performance_task}/${performance_sub_task}`,
//     dataType: 'json',
//     success: function (suc_data) {
//         var performanceData = JSON.parse(suc_data.result);
//         console.log(suc_data, performanceData['marks']);
//         var marksList = Object.values(performanceData['marks']);
//         console.log(marksList);
        
//     }
// })

// // Performance Graph Modal: Add more input rows 
// $("#performModalAdd").click(function () {
//     var getLastChild = $('#performModalInputList #performModalInput').last();
//     console.log(getLastChild);
//     var lastChildLowerValue = parseInt(getLastChild.find('input:first').val());
//     var lastChildUpperValue = parseInt(getLastChild.find('input:last').val());
//     console.log(lastChildUpperValue, lastChildLowerValue);
//     if ( ($.isNumeric(lastChildUpperValue)) && ($.isNumeric(lastChildLowerValue)) 
//             && (lastChildLowerValue >= 0) && (lastChildUpperValue >= 0) ) {
//         if ( lastChildUpperValue >= lastChildLowerValue ) {
//             var tmp = $('#performModalInput').clone();
//             // var vl = tmp.find('input:last').val();
//             tmp.find('input:first').val(parseInt(lastChildUpperValue)+1);
//             // $(tmp.find('input:first')).prop('readonly', true);
//             // $(tmp.find('input:last')).prop('readonly', true);
//             tmp.find('input:last').val('');
//             tmp.appendTo('#performModalInputList');
//         }
//         else {
//             alert("Upper value should be greater than the lower value !!");
//         }
//     }
//     else {
//         alert("Input only positive Integers !!")
//     }
//     if ($("#performModalInputList > #performModalInput").length > 1) {
//         document.getElementById("performModalRemove").disabled=false;
//     }
// });

// // Performance Graph Modal: Remove input rows
// $('#performModalRemove').click(function() {
//     if ($("#performModalInputList > #performModalInput").length > 1) {
//         var getLastChild = $('#performModalInputList #performModalInput').last();
//         $(getLastChild).remove();
//     }
//     if ($("#performModalInputList > #performModalInput").length < 2) {
//         document.getElementById("performModalRemove").disabled=true;
//     }
//     console.log("Remove not possible!");
// })


// var performRangeList;
// // Performance Graph Modal: Validate Customize Modal on Submit
// $("#performModalSubmit").click(function () {
//     performRangeList = [];
//     var validate = true;
//     $('#performModalInputList #performModalInput').each((index, row) => {
//         var tmp = [];
//         $(row).find("input").each((i, e) => {
//             var vl = $(e).val();
//             if ( !($.isNumeric(vl)) && (vl >= 0) ) {
//                 alert("ERROR: \nField empty or negative number encountered !!");
//                 performRangeList = [];
//                 validate = false;
//                 return false;
//             }
//             tmp.push(parseInt(vl));
//             console.log(performRangeList[performRangeList.length-1], i, tmp[i]);
//             if ( (i == 0) && (performRangeList.length != 0) 
//                         && (performRangeList[performRangeList.length-1][1] >= tmp[0]) ) {
//                 alert("ERROR: \nLower value is greater than or equal to Upper value of previous Column Range !!");
//                 performRangeList = [];
//                 validate = false;
//                 return false;
//             }
//             console.log(i, tmp);
//             if ( (i == 1) && (tmp[1] < tmp[0]) ) {
//                 alert("ERROR: \nUpper value less than Lower value of same Column Range !!");
//                 performRangeList = [];
//                 validate = false;
//                 return false;
//             }
//         });
//         performRangeList.push(tmp);
//     });
//     console.log(performRangeList, validate);
// })

// console.log("final", performRangeList);


// each((_, row) => {
//     var value = {};
//     $(row).find(":input").each((__, e) =>
//       value[e.name] = $(e).val()
//     );
//     values.push(value);
//   });
//   console.log(values)