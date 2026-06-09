from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

knn_params = {'n_neighbors': range(1, 21), 'weights': ['uniform', 'distance']}
knn = KNeighborsClassifier()
X_train_smote, y_train_smote = smote.fit_resample(X_train_scaled, y_train)

print("Sedang mencari parameter terbaik untuk KNN...")
knn_grid = GridSearchCV(knn, knn_params, cv=5, scoring='recall') 
knn_grid.fit(X_train_smote, y_train_smote)

print("Parameter KNN terbaik:", knn_grid.best_params_)

dt_params = {'max_depth': [3, 5, 7, 10, None], 'min_samples_split': [2, 5, 10]}
dt = DecisionTreeClassifier(random_state=42)

print("\nSedang mencari parameter terbaik untuk Decision Tree...")
dt_grid = GridSearchCV(dt, dt_params, cv=5, scoring='recall')
dt_grid.fit(X_train_smote, y_train_smote)

print("Parameter Decision Tree terbaik:", dt_grid.best_params_)

best_knn = knn_grid.best_estimator_
best_dt = dt_grid.best_estimator_