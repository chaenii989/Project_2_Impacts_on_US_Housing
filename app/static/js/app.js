// Home price plot

function buildlinePlot() {

  const url = "/api/average_home_price";
  d3.json(url).then(function(myData) {
   console.log(myData);
    
    var date = myData[0].Date;
    
    var price = myData[0].Average_Home_Price;
   

    var trace1 = {
    x: date,
    y: price,
    type: "scatter"
    
    }
    var data = [trace1];
    

    var layout = {
        title: "Average Home Price", 
    }
    

    Plotly.newPlot("line", data, layout);
})
};

buildlinePlot();

// Home Construction Materials plot

function buildCommoditiesPlot() {

    const url = "/api/lumber_steel";
    d3.json(url).then(function(myData) {
     console.log(myData);
      
      var date = myData[0].Date;
      var steel_pct_change = myData[0].Steel_Percent_Change;
      var lumber_pct_change = myData[0].Lumber_Percent_Change;

      var trace1 = {
        x: date,
        y: steel_pct_change,
        type: "scatter",
        mode: 'lines+markers',
        name: 'Steel'
      };
      
      var trace2 = {
        x: date,
        y: lumber_pct_change,
        type: "scatter",
        mode: 'lines+markers',
        name: 'Lumber'
      };
      
      var data = [trace1, trace2];
  
      var layout = {
          title: "Steel & Lumber Percent Change in Price over Time", 
      }
      
  
      Plotly.newPlot("commodities", data, layout);
  })
};
  
buildCommoditiesPlot();
