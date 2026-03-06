import pandas as pd
import pickle
from sklearn.tree import DecisionTreeRegressor


class ProductivityModel:
    """
    ML wrapper to predict productivity based on study, execution, and goal.
    """

    def __init__(self):
        self.model = None
        self.goal_mapping = {}  # convert goal string → int for ML

    def prepare_data(self, df):
        """
        Converts goal to numeric and splits features/target
        """
        # Map goals to numbers
        self.goal_mapping = {goal: i for i, goal in enumerate(df["goal"].unique())}
        df["goal_num"] = df["goal"].map(self.goal_mapping)

        X = df[["study_hours", "execution_hours", "goal_num"]]
        y = df["productivity"]

        return X, y

    def train(self, df):
        """
        Trains a DecisionTreeRegressor on the dataset
        """
        X, y = self.prepare_data(df)
        self.model = DecisionTreeRegressor(max_depth=5, random_state=42)
        self.model.fit(X, y)
        print("Model trained successfully.")

    def predict(self, study_hours, execution_hours, goal):
        """
        Predict productivity for a single input
        """
        if self.model is None:
            raise ValueError("Model not trained yet")

        if goal not in self.goal_mapping:
            raise ValueError(f"Unknown goal '{goal}'")

        goal_num = self.goal_mapping[goal]
        X_input = [[study_hours, execution_hours, goal_num]]
        pred = self.model.predict(X_input)[0]
        return round(pred, 2)

    def save_model(self, filepath="model/trained_model.pkl"):
        """
        Save trained model to disk
        """
        with open(filepath, "wb") as f:
            pickle.dump({"model": self.model, "goal_mapping": self.goal_mapping}, f)
        print(f"Model saved to {filepath}")

    def load_model(self, filepath="model/trained_model.pkl"):
        """
        Load trained model from disk
        """
        with open(filepath, "rb") as f:
            data = pickle.load(f)
        self.model = data["model"]
        self.goal_mapping = data["goal_mapping"]
        print(f"Model loaded from {filepath}")
