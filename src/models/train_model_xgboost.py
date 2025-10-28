import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from imblearn.under_sampling import RandomUnderSampler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.pipeline import Pipeline
import joblib

# Load data
df = pd.read_csv('data/processed/processed.csv')

# Input variables
X = df[['nu_idade', 'tp_sexo', 'febre', 'mialgia', 'cefaleia', 'vomito', 'nausea',
        'dor_costas', 'artralgia', 'petequia_n', 'dor_retro']]

# Target variable
y = df['tp_classificacao_final']

# Encode target variable
le_target = LabelEncoder()
y = le_target.fit_transform(y)

# Separate training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Define the pipeline with balancing + model
pipeline = Pipeline(steps=[
    ('undersample', RandomUnderSampler(random_state=42)),
    ('xgb', XGBClassifier(
        use_label_encoder=False,
        eval_metric='mlogloss'
    ))
])

# Define the grid of parameters for searching
param_grid = {
    'xgb__n_estimators': [200, 500, 1000],
    'xgb__learning_rate': [0.01, 0.05, 0.1],
    'xgb__max_depth': [3, 5, 7],
    'xgb__min_child_weight': [1, 3, 5],
    'xgb__colsample_bytree': [0.7, 0.8, 1.0]
}

# Grid Search with Cross-Validation
grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    scoring='accuracy',
    cv=3,
    verbose=1,
    n_jobs=-1
)

# Train the model with Grid Search and balancing
grid_search.fit(X_train, y_train)

# Best model found
best_model = grid_search.best_estimator_

print('Best parameters found:')
print(grid_search.best_params_)

# Evaluate on the test set
y_pred = best_model.predict(X_test)

print('\nAccuracy:', accuracy_score(y_test, y_pred))
print('\nRanking Report:')
print(classification_report(y_test, y_pred, target_names=le_target.classes_))

# Save the best model and label encoder
joblib.dump(best_model, 'models/xgb_best_model.pkl')
joblib.dump(le_target, 'models/label_encoder.pkl')