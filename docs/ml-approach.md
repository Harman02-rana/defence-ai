# ML Approach for defence
 AI

## Features
- fatigue (1–10)
- sleep (1–10)
- stress (1–10)
- mission_intensity (1–10)

## Labels
- LOW / MEDIUM / HIGH risk

## Model
- Random Forest Classifier (n_estimators=100)

## Dataset
- 1,000 synthetic samples generated via data_generator.py

## Notes
- HIGH risk: intervention required
- MEDIUM risk: monitor & reduce load
- LOW risk: fit for mission
