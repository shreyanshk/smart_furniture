// Our labels along the x-axis
var years = new array();
// For drawing the lines
var years = new array();
var africa = new array();
//var asia = new array();
//var europe = new array();
//var latinAmerica = new array();
//var northAmerica = new array();

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      { 
        data: africa,
        label: "C1",
        borderColor: "#3e95cd",
        fill: false
      }
    ]
  }
});