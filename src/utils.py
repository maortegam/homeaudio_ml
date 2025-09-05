def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def load_config(config_file):
    """Loads configuration settings from a given file."""
    import json
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def evaluate_performance(y_true, y_pred):
    """Evaluates the performance of the model using accuracy."""
    from sklearn.metrics import accuracy_score
    return accuracy_score(y_true, y_pred)

def save_model(model, filename):
    """Saves the trained model to a file."""
    import joblib
    joblib.dump(model, filename)

def load_model(filename):
    """Loads a trained model from a file."""
    import joblib
    return joblib.load(filename)