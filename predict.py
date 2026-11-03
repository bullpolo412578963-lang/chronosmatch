import mlflow

# ----------------------------------------------------------------
# PASTE YOUR RUN ID INSIDE THE QUOTES BELOW
# It should look like: run_id = "8234a92b3..."
run_id = "61b7b3aaaf364a5aba05f0bb3bef235f"
# ----------------------------------------------------------------

# This tells MLflow to go find the model folder inside that specific run
logged_model = f'runs:/{run_id}/model'

# Load the model from the folder
print(f"Loading model from: {logged_model}...")
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Make a prediction for a fake flower
# Data: [Sepal Length, Sepal Width, Petal Length, Petal Width]
test_data = [[5.1, 3.5, 1.4, 0.2]]
prediction = loaded_model.predict(test_data)

print(f"---------------------------------------------------")
print(f"The model predicts this is flower type: {prediction[0]}")
print(f"---------------------------------------------------")