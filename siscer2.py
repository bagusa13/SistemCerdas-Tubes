from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = df.drop('Surv_status', axis=1)
y = df['Surv_status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Dimensi X_train sebelum scaling:", X_train.shape)
print("Dimensi X_test:", X_test.shape)