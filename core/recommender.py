from model.model import ProductivityModel


class RecommendationEngine:
    """
    ML-powered recommendation engine that picks the optimal
    study/execution split for a goal and total hours.
    """

    def __init__(self, ml_model: ProductivityModel):
        """
        ml_model: instance of trained ProductivityModel
        """
        self.model = ml_model

    def generate_splits(self, total_hours, goal):
        """
        Returns a list of tuples: (study_hours, execution_hours, predicted_productivity)
        """
        splits = []

        for study in range(total_hours + 1):
            execution = total_hours - study
            productivity = self.model.predict(study, execution, goal)
            splits.append((study, execution, productivity))

        return splits

    def best_split(self, total_hours, goal):
        """
        Returns the split with the highest predicted productivity
        """
        splits = self.generate_splits(total_hours, goal)
        best = max(splits, key=lambda x: x[2])
        return best
