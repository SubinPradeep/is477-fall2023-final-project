from ydata_profiling import ProfileReport
import pandas as pd
import os 


file_path = 'data/wine.data'
df = pd.read_csv(file_path, delimiter=',', header=None)
output_path = 'data/wine.csv'
column_headers = ['class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of Ash', 'Magnesium', 'Total phenols', 'Flavanoids', "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"]
df.columns = column_headers
df.to_csv(output_path, index=False)
df = pd.read_csv('data/wine.csv')

if not os.path.exists("profiling"):
    os.makedirs("profiling")
    
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("profiling/report.html")