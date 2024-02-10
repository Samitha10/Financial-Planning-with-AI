import React, { useState, useEffect } from 'react';
import ShipModePieChart from './Charts/PieChart_ShipCounts';
import ShipModeBarChart from './Charts/BarChart_ShipCounts';
import SegmentPieChart from './Charts/PieChart_Segment';
import SegmentBarChart from './Charts/BarChart_Segment';
import Country_State_Count from './Charts/Country_State_Count';
import Sales_Card from './Cards/Sales_Card';
import Sales_Chart from './Cards_Charts/Sales_Charts';




function App() {
  // const [chartType, setChartType] = useState('pie');
  // const [chartType1, setChartType1] = useState('pie');



  
  return (
    <>
      {/* <div className="flex flex-row gap-5 bg-gradient-to-r from-black to-grey">
        <div className="w-1/3 m-4 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 ">
          <div className='flex items-center justify-center '>
            <input type="radio" id="pie_ship_count" name="chartType" value="pie" checked={chartType === 'pie'} onChange={(e) => setChartType(e.target.value)} />
            <label htmlFor="pie_ship_count" className="mr-2 text-base font-extrabold">Pie Chart</label>
            <input type="radio" id="bar_ship_count" name="chartType" value="bar" checked={chartType === 'bar'} onChange={(e) => setChartType(e.target.value)} />
            <label htmlFor="bar_ship_count" className="mr-2 text-base font-extrabold">Bar Chart</label>
          </div>
          {chartType === 'pie' ? <ShipModePieChart/> : <ShipModeBarChart/>}
        </div>
        <div className="w-1/3 m-4 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500">
          <div className='flex items-center justify-center'>
            <input type="radio" id="pie_segment" name="chartType1" value="pie" checked={chartType1 === 'pie'} onChange={(e) => setChartType1(e.target.value)} />
            <label htmlFor="pie_segment" className="mr-2 text-base font-extrabold">Pie Chart</label>
            <input type="radio" id="bar_segment" name="chartType1" value="bar" checked={chartType1 === 'bar'} onChange={(e) => setChartType1(e.target.value)} />
            <label htmlFor="bar_segment " className="mr-2 text-base font-extrabold">Bar Chart</label>
          </div>
          {chartType1 === 'pie' ? <SegmentPieChart/> : <SegmentBarChart/>}
        </div>
        <div className="flex items-center justify-center w-1/3 m-4 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500">
          <Country_State_Count/>
        </div>
      </div>  */}
       <Sales_Card/>
    </>
  );
}



export default App;