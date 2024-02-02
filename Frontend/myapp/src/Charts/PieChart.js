import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Doughnut } from 'react-chartjs-2';
import { Chart, ArcElement } from 'chart.js';

// Register the ArcElement
Chart.register(ArcElement);

function ShipModePieChart() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/valueCounts_shipMode_Frontend')
      .then(response => {
        setData({
          labels: Object.keys(response.data),
          datasets: [{
            data: Object.values(response.data),
            backgroundColor: [
              'red',
              'blue',
              'green',
              'yellow',
            ],
          }],
        });
      })
      .catch(error => {
        console.error(`There was an error retrieving the ship mode counts: ${error}`);
      });
  }, []);

  return data ? (
    <Doughnut 
      data={data} 
      options={{
        plugins: {
          tooltip: {
            callbacks: {
              label: function(context) {
                let label = context.label || '';
                if (label) {
                  label += ': ';
                }
                if (context.parsed.y !== undefined) {
                  label += context.parsed.y;
                }
                return label;
              }
            }
          }
        }
      }}
    />
  ) : null;
}

export default ShipModePieChart;