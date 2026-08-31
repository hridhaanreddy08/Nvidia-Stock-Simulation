# Portfolio Risk vs Return Analysis

## Overview

This project investigates the relationship between risk and return across
different portfolios. The assets used were JPM, MSFT, XOM and AMZN

## Methodology

### 1. Data Preparation

Historical price data was cleaned and organised before calculating daily
percentage returns.

### 2. Individual Asset Analysis

Annualised returns and volatility were calculated for each asset.

### 3. Correlation Analysis

A correlation matrix was created to examine how the daily returns of the
assets move relative to one another.

### 4. Portfolio Construction

Five portfolios were created using different asset weightings.

### 5. Portfolio Return

Portfolio annualised return was calculated using the weighted returns of
the individual assets.

### 6. Portfolio Risk

Portfolio variance was calculated using the covariance matrix and portfolio
weights:

σ²p = wᵀΣw

Portfolio volatility was then calculated by taking the square root of
variance and annualising using √252.

## Results (Risk vs Return Graph, Portfolio summary, Correlation matrix)
<img width="623" height="466" alt="Screenshot 2026-08-31 at 14 29 51" src="https://github.com/user-attachments/assets/b18fb42c-6270-4888-b949-cc362cdbce23" />
<img width="556" height="131" alt="Screenshot 2026-08-31 at 14 29 37" src="https://github.com/user-attachments/assets/255e3147-d531-4d97-8c79-64b1aa2d25c5" />
<img width="889" height="119" alt="Screenshot 2026-08-31 at 14 51 34" src="https://github.com/user-attachments/assets/799ade48-6fe5-4719-8127-d78d3307ef86" />

## Key Findings

Highest return: Portfolio 5 had the highest return (21.6%), but also the second highest risk (21.4%), showing the trade-off between risk and reward.

Lowest risk: Portfolio 2 had lowest risk (19.8%), showing benefits of equal asset allocation.

The results did not show a perfectly linear relationship between risk and return, with some portfolios achieving higher returns without proportionally higher volatility.

The assets had different correlations, meaning they did not always move together. Combining them therefore provided potential diversification benefits by reducing reliance on the performance of individual assets.

