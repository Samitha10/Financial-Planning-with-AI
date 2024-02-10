import React from 'react';
import sales from '../images/sales.png';
import SalesChart from '../Cards_Charts/Sales_Charts';

const Sales_Card = () => {
    return (
        <>
            <div className='w-full h-screen bg-slate-200'>
                <div className ="bg-white w-[500px] h-[400px] ml-[9px] pt-[2px]  rounded-lg ">
                    <div className="flex m-3 border-2 border-solid border-sky-500 bg-slate-100">
                        <div className="w-[60px] h-[60px] mx-[5px] my-[9px] flex-none bg-slate-300 rounded-lg ">
                            <img src={sales} alt="Sales icon" className='h-[40px] w-[40px] mx-[10px] my-[10px]' />
                        </div>
                        <h1 className="flex-initial mx-[20%] my-[25px] font-bold text-xl">Sales</h1>
                    </div>
                    <div className='border-solid border-2 border-sky-500 h-[200px] bg-slate-100 m-2'>
                        <SalesChart />
                    </div>
                    <button className='px-4 py-2 w-[40%] font-bold text-white bg-blue-500 rounded hover:bg-blue-700 mx-[30%] mt-[20px]'>Get Full Analytics</button>
                </div>
            </div>
        </>
    );
};

export default Sales_Card;