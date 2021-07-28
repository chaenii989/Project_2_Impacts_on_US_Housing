// Home price plot

function buildlinePlot() {

  const url = "/api/average_home_price";
  d3.json(url).then(function(myData) {

    

    

    var date = myData.date.toString()
    var average_home_price = myData.average_home_price

    var trace1 = {
        y: average_home_price,
        x: date,
        type: "scatter"
        
    };

    var layout = {
        title: "Average Home Price"
    }
    var data = [trace1]

    Plotly.newPlot("line", data, layout);
})
};

buildlinePlot();
