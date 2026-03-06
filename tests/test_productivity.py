from core.productivity import ProductivityCalculator

calculator = ProductivityCalculator()


def test_zero_hours():
    result = calculator.calculate_productivity(0, 0, "exam")
    assert result == 0


def test_balanced_beats_unbalanced():
    balanced = calculator.calculate_productivity(3, 3, "chill")
    unbalanced = calculator.calculate_productivity(6, 0, "chill")
    assert balanced > unbalanced


def test_exam_prefers_study():
    good_split = calculator.calculate_productivity(4, 2, "exam")
    bad_split = calculator.calculate_productivity(1, 5, "exam")
    assert good_split > bad_split


def test_project_prefers_execution():
    good_split = calculator.calculate_productivity(2, 4, "project")
    bad_split = calculator.calculate_productivity(5, 1, "project")
    assert good_split > bad_split


def test_more_hours_increase_productivity():
    small = calculator.calculate_productivity(1, 1, "chill")
    bigger = calculator.calculate_productivity(4, 4, "chill")
    assert bigger > small
