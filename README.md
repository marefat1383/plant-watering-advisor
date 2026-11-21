# Plant Watering Advisor

A small educational AI project that recommends a watering level for a plant from soil moisture, temperature, and sunlight using a Decision Tree classifier.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python plant_advisor.py --moisture 35 --temperature 24 --sunlight 6
```

## Test

```bash
python -m unittest test_plant_advisor.py
```

The training examples are synthetic and intended only for learning. They are not horticultural or agricultural advice.
