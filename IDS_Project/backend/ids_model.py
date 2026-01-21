import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("../dataset/network_data.csv")

# Use REAL packet length feature
df = df[['dst_bytes', 'protocol_type']]

# Rename correctly
df.columns = ['length', 'protocol']

# Convert protocol to numeric
df['protocol'] = df['protocol'].map({'tcp': 1, 'udp': 2, 'icmp': 3})

# Create intrusion label based on PACKET LENGTH
df['label'] = df['length'].apply(lambda x: 1 if x > 1000 else 0)

# Features and label
X = df[['length', 'protocol']]
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save model
joblib.dump(clf, "ids_model.pkl")
print("✅ Model trained & saved")

# Evaluate
y_pred = clf.predict(X_test)
print(f"✅ Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
