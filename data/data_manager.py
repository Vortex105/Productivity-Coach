import pandas as pd
from core.productivity import ProductivityCalculator


class DataManager:
    """
    Generates and manages synthetic dataset for productivity coaching.
    """

    GOALS = ["exam", "project", "chill"]

    def __init__(self):
        self.calculator = ProductivityCalculator()

    def generate_dataset(self, max_hours=8):
        """
        Returns a pandas DataFrame with study_hours, execution_hours, goal, productivity
        """
        rows = []

        for goal in self.GOALS:
            for total_hours in range(1, max_hours + 1):
                for study in range(total_hours + 1):
                    execution = total_hours - study
                    productivity = self.calculator.calculate_productivity(
                        study, execution, goal
                    )
                    rows.append(
                        {
                            "study_hours": study,
                            "execution_hours": execution,
                            "goal": goal,
                            "productivity": productivity,
                        }
                    )

        df = pd.DataFrame(rows)
        return df

    def save_dataset(self, df, filepath="data/dataset.csv"):
        df.to_csv(filepath, index=False)
        print(f"Dataset saved to {filepath}")
