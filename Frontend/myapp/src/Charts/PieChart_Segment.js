import React, { useEffect, useRef } from 'react';
import axios from 'axios';
import { Chart, PieController, ArcElement, CategoryScale, Tooltip, Legend } from 'chart.js';

// Register PieController, ArcElement, CategoryScale, Tooltip, and Legend
Chart.register(PieController, ArcElement, CategoryScale, Tooltip, Legend);

function SegmentPieChart() {
  const chartRef = useRef(null);
  let myChart;

  useEffect(() => {
    axios.get('http://localhost:8000/Froute/valueCounts_segment_Frontend')
      .then(response => {
        const data = {
          labels: Object.keys(response.data),
          datasets: [{
            data: Object.values(response.data),
            backgroundColor: [
              'rgb(255, 99, 132)',
              'rgb(54, 162, 235)',
              'rgb(255, 205, 86)',
              'rgb(205, 100, 86)'
            ],
            hoverBorderWidth: 10,
          }],
        };

        myChart = new Chart(chartRef.current, {
          type: 'pie',
          data: data,
          options: {
            hoverBorderWidth: 10,
            borderColor:'white',
            animation: {
            easing: 'easeInOutQuad',
           
            },
            responsive: true,
            plugins: {
              legend: {
                display: true,
                position:'bottom',
                labels: {
                    color: 'white',
                    font: {
                      size: 13,
                      weight: 'bold', 
                  },
                  boxWidth: 20,
                  textAlign: 'center',
                  },
              },
              tooltip: {
                callbacks: {
                  title: function(context) {
                    return context[0].label;
                  },
                  label: function(context) {
                    return 'Count: ' + context.raw;

                    
                  }
                }
              }
            }
          }
        });
      })
      .catch(error => {
        console.error(`There was an error retrieving the ship mode counts: ${error}`);
      });

    return () => {
      // Cleanup
      if (myChart) {
        myChart.destroy();
      }
    };
  }, []);

  return (
    <div>
      <h2 style={{textAlign: 'center', color: 'black',padding: '10px',fontWeight: 'bold',fontSize: '20px'}}>Segment</h2>
      <canvas ref={chartRef} />
    </div>
  );
}

export default SegmentPieChart;