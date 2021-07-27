// Home price plot

function buildlinePlot() {

  const url = "/api/average_housing";
  d3.json(url).then(function(response) {

    

    const myData = response;

    var date = myData.date
    var average_home_price = myData.average_home_price

    var trace1 = {
        y: average_home_price,
        x: date,
        type: "line",
        orientation: "h"
    };

    var layout = {
        title: "Average Home Price"
    }
    var data = [trace1]

    Plotly.newPlot("line", data, layout);
}

buildlinePlot();
