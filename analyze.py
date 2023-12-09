import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

wine_data = pd.read_csv('./data/wine.csv')
output_dir = 'results/'
os.makedirs(output_dir, exist_ok=True)

summary_statistics = wine_data.describe()
summary_statistics.to_csv(os.path.join(output_dir, 'summary_statistics.csv'))





features = ['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of Ash', 'Magnesium', 'Total phenols', 'Flavanoids',
            'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
target = 'class'
X_train, X_test, y_train, y_test = train_test_split(
    wine_data[features], wine_data[target], test_size=0.2, random_state=42, stratify=wine_data[target]
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
with open(os.path.join(output_dir, 'classification_report.txt'), 'w') as f:
    f.write("Classification Report:\n")
    f.write(classification_rep)

with open(os.path.join(output_dir, 'confusion_matrix.txt'), 'w') as f:
    f.write("Confusion Matrix:\n")
    f.write(str(confusion_mat))





correlation_matrix = wine_data[features].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap for Selected Features')
plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
plt.show()