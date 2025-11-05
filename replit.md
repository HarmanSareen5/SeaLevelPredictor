# Sea Level Predictor

## Overview
This project analyzes historical global sea level data from 1880-2013 and uses linear regression to predict sea level changes through 2050. The application creates visualizations showing both long-term historical trends and recent acceleration in sea level rise.

## Purpose
- Analyze EPA sea level data using statistical methods
- Visualize sea level trends with scatter plots and regression lines
- Predict future sea level rise based on historical patterns
- Compare overall historical trends (1880-2013) with recent trends (2000-2013)

## Current State
The project is complete and fully functional. All unit tests pass successfully.

## Recent Changes
- **2025-11-05**: Initial project setup
  - Installed Python 3.11 with pandas, matplotlib, scipy, and numpy
  - Created `sea_level_predictor.py` with data analysis and visualization functions
  - Implemented two linear regression models (full dataset and 2000+ data)
  - Created comprehensive test suite in `test_module.py`
  - Set up workflow for automated testing

## Project Architecture

### Files
- **epa-sea-level.csv**: EPA sea level data from 1880-2013 with CSIRO adjusted measurements
- **sea_level_predictor.py**: Main module containing the `draw_plot()` function
  - Loads and cleans data using pandas
  - Creates scatter plot of historical data
  - Calculates two linear regression lines using scipy.stats.linregress
  - Extends predictions through year 2050
  - Saves visualization as sea_level_plot.png
- **main.py**: Test runner that executes the plot function and runs unit tests
- **test_module.py**: Unit tests validating plot labels, title, and structure
- **.gitignore**: Python-specific ignore rules

### Key Features
1. **Data Processing**: Uses pandas to import and clean EPA sea level data
2. **Dual Regression Analysis**:
   - Line 1: Full dataset (1880-2013) showing long-term trend
   - Line 2: Recent data (2000-2013) showing acceleration in sea level rise
3. **Visualization**: Professional matplotlib chart with proper labels and legend
4. **Testing**: Automated unit tests ensure correct plot structure and labels

### Dependencies
- Python 3.11
- pandas: Data manipulation and CSV parsing
- matplotlib: Plotting and visualization
- scipy: Statistical analysis (linregress for linear regression)
- numpy: Numerical operations for extended year ranges

## Data Source
Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

## Usage
Run `python main.py` to generate the sea level plot and execute unit tests. The plot will be saved as `sea_level_plot.png`.
