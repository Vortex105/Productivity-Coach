from flask import Flask, render_template, request
from data.data_manager import DataManager
from model.model import ProductivityModel
from core.recommender import RecommendationEngine

# ---------------------
# 1️⃣ Initialize Flask
# ---------------------
app = Flask(__name__)

# ---------------------
# 2️⃣ Generate dataset and train model (once at startup)
# ---------------------
dm = DataManager()
df = dm.generate_dataset(max_hours=8)  # you can increase max_hours if you want

ml_model = ProductivityModel()
ml_model.train(df)

# Initialize ML-powered RecommendationEngine
engine = RecommendationEngine(ml_model)


# ---------------------
# 3️⃣ Routes
# ---------------------
@app.route("/", methods=["GET", "POST"])
def recommend():
    best = None

    if request.method == "POST":
        try:
            goal = request.form.get("goal")
            hours = int(request.form.get("hours"))

            if goal and hours > 0:
                best = engine.best_split(hours, goal)
        except Exception as e:
            # In real app, log the error
            print(f"Error: {e}")

    return render_template("index.html", best=best)


# ---------------------
# 4️⃣ Run Flask
# ---------------------
if __name__ == "__main__":
    app.run(debug=True)
