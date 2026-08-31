import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Coverting data about each stock into dataframe
jpm = pd.read_csv("/Users/hridhaan/Downloads/Spring_Weeks/Spring_Week/Projects/Quant_CV_Projects/Monte_Carlo_Project1/Data/JPM.csv",header=2)
msft = pd.read_csv("/Users/hridhaan/Downloads/Spring_Weeks/Spring_Week/Projects/Quant_CV_Projects/Monte_Carlo_Project1/Data/MSFT.csv",header=2)
amzn = pd.read_csv("/Users/hridhaan/Downloads/Spring_Weeks/Spring_Week/Projects/Quant_CV_Projects/Monte_Carlo_Project1/Data/AMZN.csv",header=2)
xom = pd.read_csv("/Users/hridhaan/Downloads/Spring_Weeks/Spring_Week/Projects/Quant_CV_Projects/Monte_Carlo_Project1/Data/XOM.csv",header=2)

# Coverting date to datetime type
jpm["Date"] = pd.to_datetime(jpm["Date"], dayfirst = True)
msft["Date"] = pd.to_datetime(msft["Date"], dayfirst = True)
amzn["Date"] = pd.to_datetime(amzn["Date"], dayfirst = True)
xom["Date"] = pd.to_datetime(xom["Date"], dayfirst = True)

# Sorting dates in ascending order
jpm.sort_values(by = "Date", ascending = True, inplace = True)
msft.sort_values(by = "Date", ascending = True, inplace = True)
amzn.sort_values(by = "Date", ascending = True, inplace = True)
xom.sort_values(by = "Date", ascending = True, inplace = True)

# Removing any duplicate dates
jpm.drop_duplicates(subset = "Date", inplace = True)
msft.drop_duplicates(subset = "Date", inplace = True)
amzn.drop_duplicates(subset = "Date", inplace = True)
xom.drop_duplicates(subset = "Date", inplace = True)

# Renaming Price column to ticker symbol to prevent merge error
jpm.rename(columns = {"Adj Close": "JPM"}, inplace = True)
msft.rename(columns = {"Adj Close": "MSFT"}, inplace = True)
amzn.rename(columns = {"Adj Close": "AMZN"}, inplace = True)
xom.rename(columns = {"Adj Close": "XOM"}, inplace = True)

# Combining datframes into one dataframe with price of each asset aligning with each date
combined = pd.merge(msft[["Date","MSFT"]], xom[["Date","XOM"]], on = "Date")
combined2 = pd.merge(combined, jpm[["Date","JPM"]], on = "Date")
combined3 = pd.merge(combined2, amzn[["Date","AMZN"]], on = "Date")

# Calculating daily returns for each asset
combined3["MSFT Daily Returns"] = combined3["MSFT"].pct_change()
combined3["JPM Daily Returns"] = combined3["JPM"].pct_change()
combined3["AMZN Daily Returns"] = combined3["AMZN"].pct_change()
combined3["XOM Daily Returns"] = combined3["XOM"].pct_change()

# Removing missing value
combined3.dropna(subset = "MSFT Daily Returns", inplace = True)
combined3.dropna(subset = "JPM Daily Returns", inplace = True)
combined3.dropna(subset = "AMZN Daily Returns", inplace = True)
combined3.dropna(subset = "XOM Daily Returns", inplace = True)

# Calculate average daily return and volatillity for each asset
jpm_meanR = combined3["JPM Daily Returns"].mean()
msft_meanR = combined3["MSFT Daily Returns"].mean()
amzn_meanR = combined3["AMZN Daily Returns"].mean()
xom_meanR = combined3["XOM Daily Returns"].mean()

jpm_stdR = combined3["JPM Daily Returns"].std()
msft_stdR = combined3["MSFT Daily Returns"].std()
amzn_stdR = combined3["AMZN Daily Returns"].std()
xom_stdR = combined3["XOM Daily Returns"].std()

# Annualise returns and volatillity
jpm_annualisedR = jpm_meanR * 252
msft_annualisedR = msft_meanR * 252
amzn_annualisedR = amzn_meanR * 252
xom_annualisedR = xom_meanR * 252

jpm_annualisedV = jpm_stdR * np.sqrt(252)
msft_annualisedV = msft_stdR * np.sqrt(252)
amzn_annualisedV = amzn_stdR * np.sqrt(252)
xom_annualisedV = xom_stdR * np.sqrt(252)

# Create a new dataframe comapring individual assets
asset_summary = {
    "Annual Return": [jpm_annualisedR,msft_annualisedR,xom_annualisedR,amzn_annualisedR],
    "Annual Volatility": [jpm_annualisedV,msft_annualisedV,xom_annualisedV,amzn_annualisedV]
    }

summary_df = pd.DataFrame(asset_summary, index = ["JPM","MSFT","XOM","AMZN"])

# Calculating correlation matrix to see how individual assets returns move in relation to each other
correlation_matrix = combined3[["MSFT Daily Returns","JPM Daily Returns","XOM Daily Returns","AMZN Daily Returns"]].corr()

# Creating different portfolios
weights_1 = np.array([1,0,0,0])
weights_2 = np.array([0.25,0.25,0.25,0.25])
weights_3 = np.array([0.50,0.20,0.20,0.10])
weights_4 = np.array([0.20,0.20,0.30,0.30])
weights_5 = np.array([0.10,0.10,0.40,0.40])

# Calculating annualised return of portfolios based on weight
portfolio1 = np.dot(weights_1,[msft_annualisedR,jpm_annualisedR,xom_annualisedR,amzn_annualisedR]) 
portfolio2 = np.dot(weights_2,[msft_annualisedR,jpm_annualisedR,xom_annualisedR,amzn_annualisedR]) 
portfolio3 = np.dot(weights_3,[msft_annualisedR,jpm_annualisedR,xom_annualisedR,amzn_annualisedR]) 
portfolio4 = np.dot(weights_4,[msft_annualisedR,jpm_annualisedR,xom_annualisedR,amzn_annualisedR]) 
portfolio5 = np.dot(weights_5,[msft_annualisedR,jpm_annualisedR,xom_annualisedR,amzn_annualisedR]) 

# Calculating covariance matrix for portfolio variance formula
covariance_matrix = combined3[["MSFT Daily Returns","JPM Daily Returns","XOM Daily Returns","AMZN Daily Returns"]].cov()
portfolio1_variance = np.dot(weights_1, np.dot(covariance_matrix,weights_1))
portfolio2_variance = np.dot(weights_2, np.dot(covariance_matrix,weights_2))
portfolio3_variance = np.dot(weights_3, np.dot(covariance_matrix,weights_3))
portfolio4_variance = np.dot(weights_4, np.dot(covariance_matrix,weights_4))
portfolio5_variance = np.dot(weights_5, np.dot(covariance_matrix,weights_5))

# Calculating annualised portfolio volatility
portfolio1_volatility = np.sqrt(portfolio1_variance) * np.sqrt(252)
portfolio2_volatility = np.sqrt(portfolio2_variance) * np.sqrt(252)
portfolio3_volatility = np.sqrt(portfolio3_variance) * np.sqrt(252)
portfolio4_volatility = np.sqrt(portfolio4_variance) * np.sqrt(252)
portfolio5_volatility = np.sqrt(portfolio5_variance) * np.sqrt(252)

# Portfolio results table
portfolio_results = {
    "Portfolio": ["Portfolio 1","Portfolio 2","Portfolio 3","Portfolio 4","Portfolio 5"],
    "Annual Return": [portfolio1,portfolio2,portfolio3,portfolio4,portfolio5],
    "Annual Volatility": [portfolio1_volatility,portfolio2_volatility,portfolio3_volatility,portfolio4_volatility,portfolio5_volatility,]
    }

portfolios_df = pd.DataFrame(portfolio_results)

# Outputting other results
print(summary_df)
print(correlation_matrix)
print(portfolios_df)

# Plotting risk against return
fig, ax = plt.subplots()
ax.scatter(portfolios_df["Annual Volatility"],portfolios_df["Annual Return"])
ax.set_xlabel("Risk")
ax.set_ylabel("Return")
ax.set_title("Portfolio Risk vs Return")

for i in range(1,6):
    ax.annotate("portfolio" + str(i),(portfolios_df["Annual Volatility"][i-1],portfolios_df["Annual Return"][i-1]))

plt.show()





# Removing missing value
