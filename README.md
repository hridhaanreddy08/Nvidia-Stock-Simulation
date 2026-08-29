# Nvidia Stock Price Monte Carlo Simulation

I built a Monte Carlo simulation using Geometric Brownian Motion (GBM) to project Nvidia's potential stock price paths over a 1-year period (252 trading days). The model runs 10,000 independent simulation paths powered by random shocks and historical volatility calculated from the past 5 years of stock data.

**How I Built It**
* **Data Prep:** Imported 5 years of daily price data into Pandas, converted the dates to `datetime` format for chronological sorting, and dropped duplicates.
* **Returns & Risk:** Used `.pct_change()` to get daily returns, dropped the initial `NaN` value, and calculated the mean daily return and standard deviation.
* **Running the Model:** Created a 252 x 10,000 matrix of random normal distributions ($\mu=0, \sigma=1$) and plugged them into the GBM formula to generate future price paths.
* **Plotting:** Visualised both the individual trajectories and the final price distribution using Matplotlib.

**Key Results**
* **Starting Price:** $214.72
* **Mean Final Price:** $
* **Median Final Price:** $
* **5th Percentile:** $
* **95th Percentile:** $
* **Probability of Loss:** %
* **Mean Return:** %

**Visual Results**


**Limitations**
* **Historical Bias:** The model assumes that the returns and volatility from the last 5 years is representative of future market conditions.
* **Simplified Market Dynamics:** The GBM model is useful for simulating possible prices, but it simplifies how real markets actually behave .

