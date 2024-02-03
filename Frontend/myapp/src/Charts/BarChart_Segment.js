import React, { useEffect, useRef } from 'react';
import axios from 'axios';
import { Chart, BarController, BarElement, CategoryScale, LinearScale } from 'chart.js';

// Register BarController, BarElement, CategoryScale, and LinearScale
Chart.register(BarController, BarElement, CategoryScale, LinearScale);

function SegmentBarChart() {
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
              'red',
            ],
        
           
          }],
        };

        myChart = new Chart(chartRef.current, {
          type: 'bar',
          data: data,
          options: { 
            aspectRatio: 2,
            hoverBorderWidth: 8,
            borderColor: 'white',
            
           
            plugins: {
              title: {
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
                ticks: {
                  color: 'white',
                  font: {
                    size: 14,
                    
                  }, 
                  
                },
              },
              y: {
                ticks: {
                  color: 'white', 
                  font: {
                    size: 14,
                    
                  }, 
                },
              },
            },
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
      <canvas ref={chartRef} width="400px" height="400px" />
    </div>
  );
}

export default SegmentBarChart;