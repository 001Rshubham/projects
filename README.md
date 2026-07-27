# Projects

A collection of Python projects — spanning a desktop GUI application and a machine learning analysis — built while learning software development and data science.

## Contents

- [Advanced Digital Clock](#advanced-digital-clock)
- [Titanic Survival Prediction](#titanic-survival-prediction)
- [Requirements](#requirements)
- [Notes](#notes)

---

## Advanced Digital Clock

`DigitalClock.py`

A desktop clock application built with Tkinter, going beyond a basic clock with several extra tools bundled into one window.

**Features**
- Live time and date display across multiple time zones (India, UTC, US Eastern, London, Tokyo, Sydney)
- Three switchable themes (Dark, Light, Solarized) and five font options
- Alarm, stopwatch, and timer, each in their own window
- Hourly spoken time announcements via text-to-speech
- Fullscreen toggle

**Run it**
```bash
pip install pytz requests pyttsx3
python DigitalClock.py
```

---

## Titanic Survival Prediction

`taitanic.py`

A machine learning script that cleans the classic Titanic dataset, encodes categorical features, and visualizes the survival split, as a first pass at applying `scikit-learn` to a real dataset.

**What it does**
- Loads and cleans `Titanic-Dataset.csv` (drops identifier columns, fills missing age/embarked values)
- Label-encodes categorical fields (`Sex`, `Embarked`)
- Plots and saves a pie chart of survival rate (`fig1.png`)
- Sets up `RandomForestClassifier` for prediction (via `scikit-learn`)

A full write-up accompanies this project in [`report.pdf`](./report.pdf).

**Run it**
```bash
pip install pandas seaborn matplotlib scikit-learn
python taitanic.py
```

> **Note:** this script expects a `Titanic-Dataset.csv` file in the same directory. It isn't included in this repo — download it from the [Kaggle Titanic dataset](https://www.kaggle.com/c/titanic/data) and place it alongside the script before running.

---

## Requirements

- Python 3.x
- `tkinter` (usually bundled with Python)
- `pytz`, `requests`, `pyttsx3` — for the digital clock
- `pandas`, `seaborn`, `matplotlib`, `scikit-learn` — for the Titanic analysis

Install everything at once:
```bash
pip install pytz requests pyttsx3 pandas seaborn matplotlib scikit-learn
```

## Notes

- These are standalone scripts rather than a single application — each runs independently.
- More projects will be added here over time.

---

**Author:** [Shubham Landge](https://github.com/ShubhamLandge07)
