# Productivity Coach 🎯

A Flask-based web application that uses machine learning to recommend optimal study/execution time splits for maximum productivity.

## Overview

Productivity Coach helps you find the best way to divide your available time between **studying** and **execution** based on your specific goal. Using a trained ML model, it predicts productivity scores for different time splits and recommends the optimal one.

## Features

- 🧠 **ML-Powered Recommendations** - Uses a Decision Tree Regressor to predict productivity
- 🎯 **Goal-Based Optimization** - Supports different goals: `exam`, `project`, and `chill`
- 📊 **Realistic Productivity Simulation** - Considers effort, balance, and goal-fit scores
- 🌐 **Simple Web Interface** - Easy-to-use Flask web app
- 📁 **Synthetic Dataset Generation** - Generates training data based on productivity algorithms

## Project Structure

```
productivity_coach/
├── app.py                 # Flask web application
├── config.py              # Configuration settings
├── core/
│   ├── productivity.py    # Productivity calculation logic
│   └── recommender.py     # Recommendation engine
├── data/
│   ├── data_manager.py    # Dataset generation and management
│   └── dataset.csv        # Synthetic training dataset
├── model/
│   ├── model.py           # ML model wrapper
│   ├── train_model.py     # Model training script
│   └── trained_model.pkl  # Pre-trained model
├── templates/
│   └── index.html         # Web interface
└── tests/
    ├── test_productivity.py
    └── test_recommender.py
```

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd productivity_coach
   ```

2. **Install dependencies**
   ```bash
   pip install flask pandas scikit-learn
   ```

## Usage

### Running the Web App

```bash
python app.py
```

Then open your browser and navigate to `http://127.0.0.1:5000/`

### How It Works

1. Enter your **goal** (exam, project, or chill)
2. Enter the **total hours** you have available
3. Get the **optimal split** between study and execution time for maximum productivity

### Programmatic Usage

```python
from data.data_manager import DataManager
from model.model import ProductivityModel
from core.recommender import RecommendationEngine

# Initialize components
dm = DataManager()
df = dm.generate_dataset(max_hours=8)

ml_model = ProductivityModel()
ml_model.train(df)

engine = RecommendationEngine(ml_model)

# Get best split for 5 hours with exam goal
best = engine.best_split(5, "exam")
print(f"Study: {best[0]}h, Execution: {best[1]}h, Productivity: {best[2]}%")
```

## How Productivity is Calculated

The productivity score is based on three factors:

| Factor | Weight | Description |
|--------|--------|-------------|
| **Effort Score** | 40% | Total hours with diminishing returns (√total_hours) |
| **Balance Score** | 30% | How balanced study vs execution time is |
| **Goal Score** | 30% | How close the split is to the ideal ratio for your goal |

### Ideal Goal Ratios

- **Exam**: 70% study, 30% execution
- **Project**: 30% study, 70% execution
- **Chill**: 50% study, 50% execution

## Running Tests

```bash
python -m pytest tests/
```

## API Reference

### `ProductivityCalculator`

```python
calculator = ProductivityCalculator()
productivity = calculator.calculate_productivity(study_hours, execution_hours, goal)
```

### `ProductivityModel`

```python
model = ProductivityModel()
model.train(df)
prediction = model.predict(study_hours, execution_hours, goal)
model.save_model("path/to/model.pkl")
model.load_model("path/to/model.pkl")
```

### `RecommendationEngine`

```python
engine = RecommendationEngine(ml_model)
best = engine.best_split(total_hours, goal)  # Returns (study, execution, productivity)
splits = engine.generate_splits(total_hours, goal)  # Returns all possible splits
```

## Technologies Used

- **Flask** - Web framework
- **pandas** - Data manipulation
- **scikit-learn** - Machine learning (Decision Tree Regressor)
- **pickle** - Model serialization

## License

MIT License

## Contributing

Feel free to fork this project and submit pull requests!
