import argparse

import numpy as np
from sklearn.tree import DecisionTreeClassifier

TRAINING_FEATURES = np.array([
    [80, 20, 3], [70, 22, 4], [65, 18, 2], [55, 25, 5],
    [35, 24, 6], [30, 28, 8], [25, 30, 9], [40, 26, 7],
    [10, 35, 10], [15, 32, 9], [20, 34, 8], [45, 20, 3],
], dtype=float)
TRAINING_LABELS = np.array([
    "low", "low", "low", "low",
    "medium", "medium", "medium", "medium",
    "high", "high", "high", "low",
])


def build_model() -> DecisionTreeClassifier:
    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(TRAINING_FEATURES, TRAINING_LABELS)
    return model


def recommend_watering(moisture: float, temperature: float, sunlight: float) -> str:
    if not 0 <= moisture <= 100 or temperature < -50 or sunlight < 0:
        raise ValueError("Moisture must be 0-100; temperature and sunlight must be valid")
    return str(build_model().predict([[moisture, temperature, sunlight]])[0])


def main() -> None:
    parser = argparse.ArgumentParser(description="Recommend a plant watering level.")
    parser.add_argument("--moisture", type=float, required=True)
    parser.add_argument("--temperature", type=float, required=True)
    parser.add_argument("--sunlight", type=float, required=True)
    args = parser.parse_args()
    print(f"Recommended watering: {recommend_watering(args.moisture, args.temperature, args.sunlight)}")


if __name__ == "__main__":
    main()
