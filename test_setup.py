# test_setup.py
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import requests
from bs4 import BeautifulSoup
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings('ignore')

def test_libraries():
    print("Testing core libraries...")
    
    # Test pandas
    df = pd.DataFrame({'test': [1, 2, 3]})
    print(f"✅ Pandas: {pd.__version__}")
    
    # Test numpy
    arr = np.array([1, 2, 3])
    print(f"✅ NumPy: {np.__version__}")
    
    # Test matplotlib
    plt.figure(figsize=(1,1))
    plt.close()
    print(f"✅ Matplotlib: Working")
    
    # Test requests
    response = requests.get('https://httpbin.org/get')
    print(f"✅ Requests: {response.status_code}")
    
    # Test BeautifulSoup
    soup = BeautifulSoup('<html><body><h1>Test</h1></body></html>', 'html.parser')
    print(f"✅ BeautifulSoup: {soup.h1.text}")
    
    # Test scikit-learn
    model = RandomForestRegressor(n_estimators=10)
    print(f"✅ Scikit-learn: Working")
    
    print("\n🎉 All libraries installed successfully!")

if __name__ == "__main__":
    test_libraries()