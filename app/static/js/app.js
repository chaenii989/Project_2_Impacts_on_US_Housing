// Home price plot

function buildlinePlot() {

  const url = "/api/average_home_price";
  d3.json(url).then(function(response) {

    

    const response;

    var date = response.date.toString()
    var average_home_price = response.average_home_price

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
})
};

buildlinePlot();
