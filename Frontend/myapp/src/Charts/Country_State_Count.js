import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Country_State_Count = () => {
  const [countries, setCountries] = useState({});
  const [states, setStates] = useState({});
  const [selectedCountry, setSelectedCountry] = useState('');
  const [countryCount, setCountryCount] = useState('');
  const [selectedState, setSelectedState] = useState('');
  const [stateCount, setStateCount] = useState('');

  useEffect(() => {
    const fetchLocationData = async () => {
      const countryResponse = await axios.get('http://localhost:8000/Froute/valueCounts_country_Frontend');
      const stateResponse = await axios.get('http://localhost:8000/Froute/valueCounts_state_Frontend');
      setCountries(countryResponse.data);
      setStates(stateResponse.data);
    };

    fetchLocationData();
  }, []);

  const handleCountryChange = (event) => {
    setSelectedCountry(event.target.value);
    setCountryCount(countries[event.target.value]);
  };

  const handleStateChange = (event) => {
    setSelectedState(event.target.value);
    setStateCount(states[event.target.value]);
  };

  return (
    <div className="p-6">
      <div className="mb-4">
        <label className="block mb-2 font-bold gray-700" htmlFor="country">
          Country
        </label>
        <select 
          id="country"
          value={selectedCountry} 
          onChange={handleCountryChange}
          className="w-full px-3 py-2 leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
        >
          {Object.keys(countries).map((country) => (
            <option key={country} value={country}>
              {country}
            </option>
          ))}
        </select>
        {countryCount && <p className="mt-2 text-gray-600">Country Count: {countryCount}</p>}
      </div>
      <div className="mb-4">
        <label className="block mb-2 font-bold text-black text-l" htmlFor="state">
          State
        </label>
        <select 
          id="state"
          value={selectedState} 
          onChange={handleStateChange}
          className="w-full px-3 py-2 leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
        >
          {Object.keys(states).map((state) => (
            <option key={state} value={state}>
              {state}
            </option>
          ))}
        </select>
        {stateCount && <p className="mt-2 text-gray-600">State Count: {stateCount}</p>}
      </div>
    </div>
  );
};

export default Country_State_Count;