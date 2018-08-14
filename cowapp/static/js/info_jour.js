
Highcharts.chart('container-jour', {
  chart: {
    zoomType: 'xy'
  },
  title: {
    text: 'Température & Mouvement Aujourd\'hui'
  },
  subtitle: {
    text: 'My CowWow.com'
  },
  xAxis: [{
    categories: ['-5', '-4.5', '-4', '-3.5',
      '-3', '-2.5', '-2', '-1.5', '-1', '-0.5'],
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
    data: [5946, 4981, 3457, 4763, 5343, 4588, 4977, 4278, 3764, 4316],
    tooltip: {
      valueSuffix: ' pas'
    }

  }, {
    name: 'Température',
    type: 'spline',
    data: [36, 35.8, 36, 35.9, 35.7, 36, 35.8, 35.5, 35.6, 35.8],
    tooltip: {
      valueSuffix: '°C'
    }
  }]
});