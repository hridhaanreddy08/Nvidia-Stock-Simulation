# Nvidia Stock Price Monte Carlo Simulation

This project uses NVIDIA price data from the last 5 years and a Monte Carlo simulation based on Geometric Brownian Motion to investigate the possible future stock-price outcomes over a one trading year period. I generated 10,000 possible price paths, with each path receiving independently generated random shocks.

Process:
Imported data from last 5 years. 
Converted data into a DataFrame using pandas.
Converted dates into datetime so that the dates could be sorted.
Sorted dates in ascending order then removed any duplicate dates.
Calculated daily percentage return using pandas method .pct_change().
Got rid of NaN from row 1 of daily returns.
Calculated mean return and volatility using mean and standard deviation.
Generated a 252 x 10000 matrix consisting of random numbers distributed by a normal distribution with mean 0 and standard deviation 1
Subbed these values into Geometric Brownian Motion formula.
Used matplotlib to visualise results.

Results:

Starting price:	$214.7200012,
Mean simulated final price:	$215.2079362138049,
Median simulated final price:	$215.02333449586396,
5th percentile:	$203.87857436680528,
95th percentile: $226.84905615865804, 
Probability of loss: 48.05%,
Mean simulated return: 0.2272424604498876%,

<img width="1200" height="500" alt="MonteCarloPlot" src="https://github.com/user-attachments/assets/35d8511f-e9ee-4c93-8b7a-3719f1434832" />

Limitations:

The model assumes that the returns and volatility from the last 5 years is representative of future market conditions.
The GBM model is useful for simulating possible prices, but it simplifies how real markets actually behave
