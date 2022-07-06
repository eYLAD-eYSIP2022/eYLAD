var data = JSON.parse(localStorage.getItem("jsondata"));
var y = Object.values(data["team_id"])
var conf = Object.values(data["confidence"])
var result = conf.filter(con => con > 0.5)
var expnotsub = conf.length - result.length
var sortedstraight = false
// var userinput = document.getElementById("userinput")
var lowerTable = document.getElementById('tableContent')
var tableCells = lowerTable.getElementsByTagName("tr")
var token = 0
var prev_c = 0
var prev_x = "ALL"
var conftype = ["table-success", "table-warning", "table-danger"]
let new_rows = lowerTable.rows
// console.log(new_rows.length)
// console.log(tableCells.length)
function filter_theme() {
    var x = document.getElementById("theme").value;
    var trHTML = '';
    prev_x = x
    prev_c = 0
    for (var i = 0; i < y.length; ++i) {
        if (data["confidence"][i] > 0.66) {
            token = 0;
        } else if (data["confidence"][i] > 0.33) {
            token = 1;
        } else {
            token = 2;
        }

        if (x === "ALL") {
            trHTML += `<tr class=${conftype[token]}><td>` + y[i] +
                '</td><td>' + data["theme"][i] +
                '</td><td>' + data["prediction"][i] +
                '</td><td>' + (data["confidence"][i] * 100).toPrecision(4) +
                '</td></tr>';
        }
        if (data["theme"][i] === x) {
            trHTML += `<tr class=${conftype[token]}><td>` + y[i] +
                '</td><td>' + data["theme"][i] +
                '</td><td>' + data["prediction"][i] +
                '</td><td>' + (data["confidence"][i] * 100).toPrecision(4) +
                '</td></tr>';

        }



    }
    document.getElementById('tableContent').innerHTML = trHTML
    // th = document.getElementsByTagName('th');


    // for(let c=0; c < th.length; c++){

    //     th[c].addEventListener('click',item(c))
    // }
}


// console.log(lowerTable.rows.length)
// console.log(tableCells.length)
document.getElementById("teamIdHeader").addEventListener('click', item(0))
document.getElementById("confHeader").addEventListener('click', item(3))
new Chart(document.getElementById("myChart"), {
    type: 'doughnut',
    data: {
        labels: ['Predicted to submit', 'predicted not to submit'],
        datasets: [
            {
                label: "Task status",
                backgroundColor: ["#3e95cd", "#8e5ea2"],
                data: [result.length, expnotsub]
            }
        ]
    },
    options: {
        title: {
            display: true,
            text: 'Task4_stats'
        }
    }
});

// th = document.getElementsByTagName('th');

// for(let c=0; c < th.length; c++){

//     th[c].addEventListener('click',item(c))
// }


function item(c) {
    return async function () {
        // console.log(c)
        document.getElementById("spinner_home").innerHTML = `<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>`
        // let czor = await document.getElementById("spinner_home").innerHTML
        sortTable(c)
        document.getElementById("spinner_home").innerHTML = `Loaded`
    }

}


function sortTable(c) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("table1");
    // console.log(table);
    switching = true;
    var xar = document.getElementById("theme").value
    /*Make a loop that will continue until
    no switching has been done:*/
    if (c === prev_c && xar === prev_x) {
        rows = table.rows;
        /*Loop through all table rows (except the
        first, which contains table headers):*/
        let temp
        let temp2
        let rowlength = rows.length
        console.log("From reverse")
        // console.log(rows[3].className);
        // console.log(rows.length);
        for (i = 1; i < (rowlength - 1) / 2; i++) {
            temp = rows[i].innerHTML
            temp2 = rows[i].className
            rows[i].innerHTML = rows[rowlength - i].innerHTML
            rows[i].className = rows[rowlength - i].className
            rows[rowlength - i].innerHTML = temp
            rows[rowlength - i].className = temp2
        }

    }
    else {
        console.log("From sort")
        while (switching) {
            //start by saying: no switching is done:
            switching = false;
            rows = table.rows;
            /*Loop through all table rows (except the
            first, which contains table headers):*/
            // console.log(rows[2].innerHTML);
            // console.log(rows.length);
            for (i = 1; i < (rows.length - 1); i++) {
                //start by saying there should be no switching:
                shouldSwitch = false;
                /*Get the two elements you want to compare,
                one from current row and one from the next:*/
                x = rows[i].getElementsByTagName("td")[c];
                y = rows[i + 1].getElementsByTagName("td")[c];
                //check if the two rows should switch place:
                if (sortedstraight) {
                    if (parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) {
                        //if so, mark as a switch and break the loop:
                        shouldSwitch = true;
                        break;
                    }
                }
                else {
                    if (parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
                        //if so, mark as a switch and break the loop:
                        shouldSwitch = true;
                        break;
                    }
                }

            }
            if (shouldSwitch) {
                /*If a switch has been marked, make the switch
                and mark that a switch has been done:*/
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }
    }
    // document.getElementById("statusSpin").add("text-success");
    // document.getElementById("statusSpin").remove("text-light");


    if (sortedstraight) {
        sortedstraight = false
    }
    else {
        sortedstraight = true
    }
    prev_c = c;
    prev_x = xar
    // document.getElementById("spinner_home").innerHTML=" "
    // document.getElementById("statusSpin").add("text-light");
    // document.getElementById("statusSpin").remove("text-success");
}



function download_csv(csv, filename) {
    var csvFile;
    var downloadLink;

    // CSV FILE
    csvFile = new Blob([csv], { type: "text/csv" });

    // Download link
    downloadLink = document.createElement("a");

    // File name
    downloadLink.download = filename;

    // We have to create a link to the file
    downloadLink.href = window.URL.createObjectURL(csvFile);

    // Make sure that the link is not displayed
    downloadLink.style.display = "none";

    // Add the link to your DOM
    document.body.appendChild(downloadLink);

    // Lanzamos
    downloadLink.click();
}

function export_table_to_csv(html, filename) {
    var csv = [];
    var rows = document.querySelectorAll("table tr");

    for (var i = 0; i < rows.length; i++) {
        var row = [], cols = rows[i].querySelectorAll("td, th");

        for (var j = 0; j < cols.length; j++)
            row.push(cols[j].innerText);

        csv.push(row.join(","));
    }

    // Download CSV
    download_csv(csv.join("\n"), filename);
}

document.getElementById("export").addEventListener("click", function () {
    var html = document.getElementById("table1").outerHTML;
    var text = document.getElementById("theme").value
    export_table_to_csv(html, `${text}.csv`);
});