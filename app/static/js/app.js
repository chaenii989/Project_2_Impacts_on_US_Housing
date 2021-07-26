function buildCommodityPlot() {

    /* data route */
  const url = "/api/lumber_steel";
  d3.json(url).then(function(response) {
    console.log(response);
  }
    /*Promise.all([
      loadData(
        "https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/plotting-multiple-series-on-time-axis-data.json"
      ),
      loadData(
        "https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/plotting-multiple-series-on-time-axis-schema.json"
      )
    ]).then(function(res) {
      const data = res[0];
      const schema = res[1];
    
      const dataStore = new FusionCharts.DataStore();
      const dataSource = {
        chart: {},
        caption: {
          text: "Sales Analysis"
        },
        subcaption: {
          text: "Grocery & Footwear"
        },
        series: "Type",
        yaxis: [
          {
            plot: "Sales Value",
            title: "Sale Value",
            format: {
              prefix: "$"
            }
          }
        ]
      };
      dataSource.data = dataStore.createDataTable(data, schema);
    
      new FusionCharts({
        type: "timeseries",
        renderAt: "chart-container",
        width: "100%",
        height: "500",
        dataSource: dataSource
      }).render();
    });
  }
)*/
    /*const data = response;

    const layout = {
      scope: "usa",
      title: "Pet Pals",
      showlegend: false,
      height: 600,
            // width: 980,
      geo: {
        scope: "usa",
        projection: {
          type: "albers usa"
        },
        showland: true,
        landcolor: "rgb(217, 217, 217)",
        subunitwidth: 1,
        countrywidth: 1,
        subunitcolor: "rgb(255,255,255)",
        countrycolor: "rgb(255,255,255)"
      }
    };

    Plotly.newPlot("plot", data, layout);
  });
}*/
  )}
buildCommodityPlot();