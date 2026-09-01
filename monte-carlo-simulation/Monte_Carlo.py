# Data from Last 5 years

import yfinance as yf

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

# Coverting data about each stock into dataframe

nvda = pd.read_csv("/Users/hridhaan/Downloads/Spring_Weeks/Spring_Week/Projects/Quant_CV_Projects/Monte_Carlo_Project1/Data/NVDA.csv",header=2)


# Coverting Date to datetime

nvda["Date"] = pd.to_datetime(nvda["Date"], dayfirst = True) # Prevents pandas from misinterpreting dates(US dates) - Puts dates into International style

nvda.sort_values(by = "Date", ascending = True, inplace = True)

# Remove duplicate dates

nvda.drop_duplicates(subset="Date", inplace = True) # Inplace means we don't have to reassign changes

# Calculate daily percentage return

nvda["Daily % Return"] = nvda["Adj Close"].pct_change()

nvda.dropna(subset = ["Daily % Return"], inplace = True) # get rid of NaN from day 1

mean_return = nvda["Daily Return"].mean()
volatillity = nvda["Daily Return"].std()
current_price = nvda["Adj Close"].iloc[-1]

# Unpredictable events causing sudden changes in stock price
random_shocks = np.random.normal(loc=0, scale = 1, size = (252,10000)) # loc = mean, scale = std, size = 252 tarding days and 10000 simulation paths

matrix = np.zeros((253,10000)) # Creating a matrix where trading days represents rows and simualtion paths represent columns

matrix[0] = current_price # Setting Day 0 to current price

# Geometric brownian formula - Separate formula into sections

dt = 1

# Section 1 
s1 = mean_return - (0.5 * (volatillity**2))

# Section 2
s2 = s1 * dt

# Section 3
s3 = (volatillity * np.sqrt(dt)) * random_shocks

# Section 4
s4 = np.exp(s2 + s3)

# Section 5
for i in range(0,252):
    matrix[i + 1] = matrix[i]* s4[i] # Previous simulated prices × growth factors = next simulated prices

final_prices = matrix[-1, :]

# Analysis of final_prices

average_simulated_price = np.mean(final_prices) # Average price of final prices
median_simulated_price = np.median(final_prices) # Median price of final prices

# 90% range of simulated outcomes.

lower_bound = np.percentile(final_prices, 5) # 5% of simulations end below this price
upper_bound = np.percentile(final_prices, 95) # 95% of simulations end below this price

loss_count = np.sum(final_prices < current_price) # Probabillity of losing money
prob_loss = loss_count / 10000

# Analysis of returns

simulated_returns = (final_prices - current_price) / current_price
simulated_mean = np.mean(simulated_returns)
simulated_std = np.std(simulated_returns)

# Matplotlib to plot results

# Price trajectory plot
fig, (ax1,ax2) = plt.subplots(1,2, figsize = (12,5)) # Create a figure and axes
ax1.set_title("50 Simulation paths of Nvidia's stock price")
ax1.set_xlabel("Trading Days")
ax1.set_ylabel("Price")

days = np.arange(0,253) # List from 0 to 252
ax1.plot(days,matrix[:,:50]) # Plots days on x-axis and price on y-axis

# Histogram of final prices plot
ax2.hist(matrix[-1, :], bins = 50) # bins = number of boxes
ax2.set_title("Distribution of Final Simulated Prices")
ax2.set_xlabel("Final Price")
ax2.set_ylabel("Frequency")

plt.tight_layout() # Prevents text in both figures from overlapping
plt.show()


           





    







