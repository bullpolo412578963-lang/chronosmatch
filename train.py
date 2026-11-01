import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# 1. Set the Experiment Name
mlflow.set_experiment("Iris_Classification_Experiment")

def train():
    # Load data
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    # Define hyperparameters
    C_param = 0.5
    # --- CHANGED THIS LINE BELOW ---
    solver_param = 'lbfgs' 
    # -------------------------------

    # 2. Start the MLflow Run
    with mlflow.start_run():
        
        # Log Hyperparameters
        mlflow.log_param("C", C_param)
        mlflow.log_param("solver", solver_param)

        # Train the model (max_iter increased to ensure it learns fully)
        model = LogisticRegression(C=C_param, solver=solver_param, max_iter=200)
        model.fit(X_train, y_train)
        
        # Predict and calculate metrics
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        # Log Metrics
        mlflow.log_metric("accuracy", accuracy)

        # Log the Model
        mlflow.sklearn.log_model(model, "model")
        
        print(f"Run Complete. Accuracy: {accuracy}")

if __name__ == "__main__":
    train()