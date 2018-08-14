// var db = openDatabase('db.sqlite3');
// db.transaction(function (tx) {
//   var temps = tx.executeSql('SELECT temperature FROM Senseur');
// });
Highcharts.chart('container', {
  chart: {
    zoomType: 'xy'
  },
  title: {
    text: 'Température & Mouvement par Mois'
  },
  subtitle: {
    text: 'My CowWow.com'
  },
  xAxis: [{
    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    crosshair: true
  }],
  yAxis: [{ // Primary yAxis
    labels: {
      format: '{value}°C',
      style: {
        color: Highcharts.getOptions().colors[1]
      }
    },
    title: {
      text: 'Température',
      style: {
        color: Highcharts.getOptions().colors[1]
      }
    }
  }, { // Secondary yAxis
    title: {
      text: 'Mouvement',
      style: {
        color: Highcharts.getOptions().colors[0]
      }
    },
    labels: {
      format: '{value} pas',
      style: {
        color: Highcharts.getOptions().colors[0]
      }
    },
    opposite: true
  }],
  tooltip: {
    shared: true
  },
  legend: {
    layout: 'vertical',
    align: 'left',
    x: 120,
    verticalAlign: 'top',
    y: 100,
    floating: true,
    backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
  },
  series: [{
    name: 'Mouvement',
    type: 'column',
    yAxis: 1,
    data: [9503, 12509,  6201,  7248, 15214,  9140, 11002, 14461, 17530,  6389],
    tooltip: {
      valueSuffix: ' pas'
    }

  }, {
    name: 'Température',
    type: 'spline',
    data: [36, 34.8, 34.9, 35.2, 35, 36.4, 36, 36.7, 36.2, 36],
    // $query = "SELECT temprature FROM Senseur",
    // data: data.push($query),
    tooltip: {
      valueSuffix: '°C'
    }
  }]
});
