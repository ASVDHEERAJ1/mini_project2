# Crop Stress Detection using Deep Learning

## Project Description
This project detects crop stress from plant images using a deep learning model. 
Users can upload crop images and the system predicts the stress condition.

## Technologies Used
- Python
- Streamlit
- TensorFlow
- NumPy
- Pandas

## How to Run
1. Install requirements
   ```
   pip install -r requirements.txt
   ```

2. The model is split into `plant_disease_model_part1.bin` and `plant_disease_model_part2.bin` (each &lt;25MB for GitHub). The app joins them automatically on first run.

3. Run the Streamlit app
   ```
   streamlit run app.py
   ```

## Features
- Upload crop images
- Predict crop stress level
- Display prediction results
- Save prediction history

## Deployment
The application can be deployed using Streamlit Cloud.
