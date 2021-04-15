// Palette de couleurs utilisée par tous les graphiques
var colors = ["#1D507A", "#2F6999", "#66A0D1", "#8FC0E9", "#4682B4"];

// List of groups (here I have one group per column)

d3.json('/types/', selectButton)
function selectButton(data){

  var allTypes = data.types
  // add the options to the button
  d3.select("#selectButton")
    .selectAll('myOptions')
    .data(allTypes)
    .enter()
    .append('option')
    .text(function (d) { return d; }) // text showed in the menu
    .attr("value", function (d) { return d; }) // corresponding value returned by the button


// When the button is changed, run the updateChart function
  d3.select("#selectButton").on("change", function(d) {
      // recover the option that has been chosen
      var selectedGroup = d3.select(this).property("value")
      // run the updateChart function with this selected option
      d3.json('/yield/mean/type/'+selectedGroup, nvd3_plot);
  })


  function nvd3_plot(data) {
        nv.addGraph(function() {

          // Adapt format for nvd3
            data_formated = new Array ( ) ;
            for(i=0 ; i<data['yields'].length; i++){
              data_formated.push(new Array(data['yields'][i].time, data['yields'][i].yield_mean));
            }

            var data_d3 = [
              {
                key: 'Mean yield',
                values: data_formated
              }
            ]


            var chart = nv.models.lineChart()
                .x(function(d) {
                    return d[0]
                })
                .y(function(d) {
                    return d[1]
                })
                // .yDomain([-5, 35])
                .height(270)
                .color(colors);

            chart.xAxis
                .showMaxMin(false)
                .axisLabel('Year')


            chart.yAxis //Chart y-axis settings
                .showMaxMin(false)
                .axisLabel('Yield (t/H)')
                .tickFormat(d3.format(',r'));

            d3.select('#yield svg')
              .datum(data_d3)
                .call(chart);

            nv.utils.windowResize(chart.update);

            return chart;
        });
  }
}


//Read the data

d3.json('/yield/0', plot_map);

function plot_map(data){
  // set the dimensions and margins of the graph
  var margin = {top: 30, right: 30, bottom: 30, left: 30},
    width = 450 - margin.left - margin.right,
    height = 450 - margin.top - margin.bottom;

  data_d3 = data['yield_map']
  console.log(data)

  // append the svg object to the body of the page
  var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

  svg.selectAll()
      .data(data, function(d) {return d.group+':'+d.variable;})
      .enter()
      .append("rect")
      .style("fill", function(d) { return myColor(d.value)} )

    d3.select('#yield_map svg')
      .data(data_d3)
}




// nv.models.lineChart()
//   .margin({left: 100})  //Adjust chart margins to give the x-axis some breathing room.
//   .useInteractiveGuideline(true)  //We want nice looking tooltips and a guideline!
//   .transitionDuration(350)  //how fast do you want the lines to transition?
//   .showLegend(true)       //Show the legend, allowing users to turn on/off line series.
//   .showYAxis(true)        //Show the y-axis
//   .showXAxis(true)        //Show the x-axis
