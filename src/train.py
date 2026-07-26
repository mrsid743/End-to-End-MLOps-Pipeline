import os
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set MLflow tracking URI (ensure MLflow server is running)
# Example: export MLFLOW_TRACKING_URI="http://localhost:5000"
mlflow.set_tracking_uri(os.environ.get("MLFLOW_TRACKING_URI", "http://localhost:5000"))
mlflow.set_experiment("iris-classification")

def train():
    with mlflow.start_run():
        # 1. Load Data
        print("Loading data...")
        iris = load_iris()
        X, y = iris.data, iris.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # 2. Define Hyperparameters
        n_estimators = 100
        max_depth = 5
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)

        # 3. Train Model
        print("Training model...")
        rf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        rf.fit(X_train, y_train)

        # 4. Evaluate Model
        y_pred = rf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy}")
        mlflow.log_metric("accuracy", accuracy)

        # 5. Log Model to MLflow
        print("Logging model...")
        # Log the model and register it as "IrisClassifier"
        mlflow.sklearn.log_model(
            sk_model=rf,
            artifact_path="model",
            registered_model_name="IrisClassifier"
        )
        print("Training complete and model registered.")

if __name__ == "__main__":
    train()