import unittest
import sea_level_predictor
import matplotlib as mpl
import pandas as pd


class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Rise in Sea Level'")
    
    def test_plot_xlabel(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'Year'")
    
    def test_plot_ylabel(self):
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'Sea Level (inches)'")

    def test_plot_numlines(self):
        actual = len(self.ax.get_lines())
        expected = 2
        self.assertEqual(actual, expected, "Expected two lines on plot.")
    
    def test_data_coverage(self):
        df = pd.read_csv('epa-sea-level.csv')
        df_clean = df[df['CSIRO Adjusted Sea Level'].notna()]
        min_year = df_clean['Year'].min()
        max_year = df_clean['Year'].max()
        self.assertEqual(min_year, 1880, "Expected data to start from 1880")
        self.assertEqual(max_year, 2013, "Expected data to end at 2013")
        self.assertGreater(len(df_clean), 100, "Expected more than 100 data points")
    
    def test_prediction_range(self):
        lines = self.ax.get_lines()
        line1_xdata = lines[0].get_xdata()
        line2_xdata = lines[1].get_xdata()
        self.assertGreaterEqual(int(line1_xdata.max()), 2050, "Expected first line to extend to at least 2050")
        self.assertGreaterEqual(int(line2_xdata.max()), 2050, "Expected second line to extend to at least 2050")
        self.assertLessEqual(int(line1_xdata.min()), 1880, "Expected first line to start from 1880 or earlier")
        self.assertEqual(int(line2_xdata.min()), 2000, "Expected second line to start from 2000")


if __name__ == "__main__":
    unittest.main()
