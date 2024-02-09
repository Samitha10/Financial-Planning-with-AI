import React from 'react';
import sales from '../images/sales.png';
import SegmentBarChart from '../Charts/BarChart_Segment';
import SalesChart from '../Cards_Charts/Sales_Charts';


const Sales_Card = () => {
    return (
      <>
      <div className='flex'>
        <div className="bg-slate-500 w-[500px] h-[400px] mx-[5px] my-[6px] rounded-lg ">
          <div className="flex m-2 border-2 border-solid border-sky-500">
          <div className="w-[60px] h-[60px] mx-[7px] my-[7px] flex-none bg-slate-300 rounded-lg ">
            <img src={sales} alt="Sales icon" className='h-[40px] w-[40px] mx-[10px] my-[10px]' />
            </div>
          <h1 className="flex-initial mx-[20%] my-[5%] font-bold text-xl">Sales</h1>
        </div>
        <div className='border-solid border-2 border-sky-500  h-[300px] bg-slate-300 m-2'>
        <SalesChart />  
        </div>
        </div>
        </div>
        
      </>
    );
  };

export default Sales_Card;