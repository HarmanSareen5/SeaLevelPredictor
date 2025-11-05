import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    
    df_clean = df[df['CSIRO Adjusted Sea Level'].notna()].copy()
    
    x = df_clean['Year']
    y = df_clean['CSIRO Adjusted Sea Level']
    
    plt.figure(figsize=(12, 6))
    
    plt.scatter(x, y, alpha=0.6, s=20, label='Original Data')
    
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x, y)
    
    years_extended = np.arange(x.min(), 2051)
    sea_level_pred1 = slope1 * years_extended + intercept1
    plt.plot(years_extended, sea_level_pred1, 'r', label='Best Fit Line (1880-2013)', linewidth=2)
    
    df_recent = df_clean[df_clean['Year'] >= 2000].copy()
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_recent, y_recent)
    
    years_recent = np.arange(2000, 2051)
    sea_level_pred2 = slope2 * years_recent + intercept2
    plt.plot(years_recent, sea_level_pred2, 'g', label='Best Fit Line (2000-2013)', linewidth=2)
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('sea_level_plot.png', dpi=300, bbox_inches='tight')
    
    return plt.gca()
