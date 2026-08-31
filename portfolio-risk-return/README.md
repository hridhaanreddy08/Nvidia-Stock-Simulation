# Portfolio Risk vs Return Analysis

## Overview

This project investigates the relationship between risk and return across
different portfolios. The assets used were JPM, MSFT, XOM and S&P500

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

## Results

<img width="628" height="467" alt="Screenshot 2026-08-31 at 12 06 02" src="https://github.com/user-attachments/assets/1015f20c-57b2-49e1-a4f3-55b43e7f8b0c" />
<img width="530" height="138" alt="Screenshot 2026-08-31 at 12 05 44" src="https://github.com/user-attachments/assets/03a7dab2-ef3e-4b1f-8174-a12a6ddeb934" />
<img width="470" height="112" alt="Screenshot 2026-08-31 at 12 05 16" src="https://github.com/user-attachments/assets/bef4c9ba-c99d-4ebd-b225-045f2a97b758" />

## Key Findings

Highest return : Portfolio 5 (26.94%)
Lowest risk: Portfolio 2 (18.57%)

