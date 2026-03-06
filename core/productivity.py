import math


class ProductivityCalculator:
    """
    Simulates realistic productivity based on study time,
    execution time, and goal type.
    """

    GOAL_RATIOS = {"exam": 0.7, "project": 0.3, "chill": 0.5}

    def calculate_productivity(self, study_hours, execution_hours, goal):
        """
        Main function that returns productivity percentage (0–100).
        """

        total_hours = study_hours + execution_hours

        # Edge case: no work done
        if total_hours == 0:
            return 0

        effort = self._effort_score(total_hours)
        balance = self._balance_score(study_hours, execution_hours, total_hours)
        goal_fit = self._goal_score(study_hours, total_hours, goal)

        raw_score = 0.4 * effort + 0.3 * balance + 0.3 * goal_fit

        productivity_percentage = raw_score * 25

        return round(productivity_percentage, 2)

    # ---- helper methods ----

    def _effort_score(self, total_hours):
        """Diminishing returns using square root."""
        return math.sqrt(total_hours)

    def _balance_score(self, study_hours, execution_hours, total_hours):
        """Penalize imbalance between study and execution."""
        imbalance = abs(study_hours - execution_hours) / total_hours
        return 1 - imbalance

    def _goal_score(self, study_hours, total_hours, goal):
        """How close the split is to the ideal ratio for the goal."""
        ideal_ratio = self.GOAL_RATIOS.get(goal, 0.5)
        study_ratio = study_hours / total_hours
        goal_distance = abs(study_ratio - ideal_ratio)
        return 1 - goal_distance
