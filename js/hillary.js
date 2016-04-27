// var pie = new d3pie("pieChartHillary", {
//   // "size": {
//   //    "canvasHeight": 120,
//   //    "canvasWidth": 140
//   // },
//   "header": {
//     "title": {
//       "text": "Hillary Clinton Results",
//       "fontSize": 32,
//       "font": "open sans"
//     },
//     "subtitle": {
//       "text": "Data Taken from 03/25/16-04/15/16",
//       "color": "#999999",
//       "fontSize": 15,
//       "font": "open sans"
//     },
//     "titleSubtitlePadding": 20
//   },
//   "footer": {
//     "text": "Total Tweets: 545,019",
//     "color": "#777777",
//     "fontSize": 20,
//     "font": "verdana",
//     "location": "bottom-center"
//   },
//   "misc": {
//     "gradient": {
//       "enabled": true,
//       "percentage": 100
//     },
//     "canvasPadding": {
//       "top": 25,
//       "left": 5
//     }
//   },
//   "data": {
//     "content": [
//       {
//         "label": "Negitive",
//         "value": 303419,
//         "color": "#7e3838"
//       },
//       {
//         "label": "Positive",
//         "value": 241600,
//         "color": "#587e38"
//       }
//     ]
//   },
//   "labels": {
//     "outer": {
//       "pieDistance": 10
//     },
//     "mainLabel": {
//       "fontSize": 17
//     },
//     "percentage": {
//         "color": "#ffffff",
//         "fontSize": 15,
//         "decimalPlaces": 0
//     }
//   }
// }
// );
//
//
function drawChart() {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Topping');
  data.addColumn('number', 'Slices');
  data.addRows([
    ['Mushrooms', 3],
    ['Onions', 1],
    ['Olives', 1],
    ['Zucchini', 1],
    ['Pepperoni', 2]
    ]);

    // Set chart options
    var options = {'title':'How Much Pizza I Ate Last Night',
      'width':400,
      'height':300};

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('pieChartHillary'));
    chart.draw(data, options);
}
