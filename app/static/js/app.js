// Home price plot

function buildlinePlot() {

  const url = "/api/average_home_price";
  d3.json(url).then(function(response) {
   console.log(response);
   

    var data = response;
    

    var layout = {
        title: "Average Home Price", 
        type: "scatter"
    }
    

    Plotly.newPlot("line", data, layout);
})
};

buildlinePlot();
