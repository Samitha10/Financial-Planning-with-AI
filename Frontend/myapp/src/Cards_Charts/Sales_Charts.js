import React, { useEffect, useRef } from 'react';
import axios from 'axios';
import { Chart, BarController, BarElement, CategoryScale, LinearScale } from 'chart.js';

Chart.register(BarController, BarElement, CategoryScale, LinearScale);

function SalesChart() { // Remove selectedYear as a prop
  const chartRef = useRef(null);
  let myChart;
  const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/Sales/Sales_Frontend')
      .then(res => {
        const parsedData = res.data;
        let totalSales = 0;
        const labels = [];
        const data = [];

        Object.values(parsedData.year).forEach((year, index) => {
          if (year === 2014) { // Hardcode the year to 2014
            labels.push(`${year} ${monthNames[Object.values(parsedData.month)[index] - 1]}`);
            data.push(Object.values(parsedData.fsales)[index]);
            totalSales += Object.values(parsedData.fsales)[index];
          }
        });

        const chartData = {
          labels: labels,
          datasets: [
            {
              data: data,
              backgroundColor: 'rgb(75, 192, 192)',
              borderColor: 'rgba(77, 192, 192, 0.2)',
              barThickness: 20, 
            }
          ]
        };

        myChart = new Chart(chartRef.current, {
          type: 'bar',
          data: chartData,
          options: {
            plugins: {  title: {
              display: false,
              text: 'Custom Chart Title',
              font: {
                size: 30,
                weight: 'bold',
              },
             
          },
            legend: {
              text: 'Ship Mode',
              display:false,
              position: 'bottom',
              color: 'blue'
            },
            tooltip: {
              callbacks: {
                title: function(context) {
                  return context[0].label;
                },
                label: function(context) {
                  return 'Count: ' + context.parsed.y;
                }
              }
            }
              
             
            },
            scales: {
              x: {
                display: false,
              },
              y: {
                display: false,
              }
            }
          }
        });
      })
      .catch(err => console.error(err));

    return () => {
      // Cleanup
      if (myChart) {
        myChart.destroy();
      }
    };
  }, []); // Remove selectedYear from the dependency array

  return (
    <div className ='w-[350px] h-[150px] flex-none'>
      <canvas ref={chartRef} />
    </div>
  );
}

export default SalesChart;