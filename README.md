# Climate Forcing Factors Analysis

## Overview
This project implements a moving window regression analysis to study the relative contributions of different climate forcing factors to temperature changes during the period 1866-1914. The analysis focuses on year-over-year changes in various climate variables to understand their immediate relationships with temperature fluctuations.

## Data
The analysis includes the following climate variables:
- CO2: Atmospheric carbon dioxide levels
- Sun: Solar activity measurements
- SOx: Sulfur oxide emissions
- OT: Optical thickness
- SOI: Southern Oscillation Index (El Niño indicator)
- NAO: North Atlantic Oscillation
- Temp: Temperature anomalies
- CET: Central England Temperature

## Methodology

### 1. Data Preprocessing
- For each climate variable, year-over-year differences are calculated
- This transformation helps focus on immediate relationships and reduces the impact of long-term trends

### 2. Moving Window Linear Regression
The core analysis uses a moving window approach to solve a series of linear equations:
```
ΔT = β₁ΔCO₂ + β₂ΔSun + β₃ΔSOx + β₄ΔOT + β₅ΔSOI
```
where:
- ΔT represents temperature changes
- Δ represents year-over-year differences
- β values are regression coefficients

For each time window:
1. A subset of data points equal to the number of forcing factors is selected
2. A linear system is solved to find the contribution coefficients
3. The window moves forward one year, and the process repeats

### 3. Contribution Analysis
The relative contribution of each forcing factor is calculated by:
1. Computing the absolute contribution of each factor (|coefficient × change|)
2. Normalizing by the total absolute change across all factors

### 4. Visualization
The results are presented in two ways:
1. A line plot showing the evolution of relative contributions over time
2. Individual bar plots for each forcing factor's contribution

## Key Assumptions
1. **Additivity**: The effects of different forcing factors are assumed to be additive
2. **Immediate Response**: The analysis assumes temperature changes respond to forcing changes within the same year
3. **Linear Relationships**: The relationship between forcing factors and temperature is assumed to be linear within each window

## Dependencies
- NumPy: For numerical computations
- Pandas: For data handling
- Matplotlib/Seaborn/Plotly: For visualization

## Usage
```python
if __name__ == '__main__':
    datamatrix = np.column_stack((dCO2, dSun, dSOx, dOT, dSOI))
    tempdata = dTemp
    ForcingFactors = ['CO2', 'Sun', 'SOx', 'OT', 'SOI']
    MovingLinReg(ForcingFactors, datamatrix, tempdata)
```
