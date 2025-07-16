# app.py
from flask import Flask, render_template, request
from ai_generator import generate_horoscope
from rashi_data import rashis
from database import save_prediction, get_predictions, init_db
import os

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html', rashis=rashis)

@app.route('/horoscope/<int:rashi_id>')
def horoscope(rashi_id):
    rashi = next((r for r in rashis if r['id'] == rashi_id), None)
    if not rashi:
        return "Rashi not found", 404

    # Generate and Save Daily Horoscope
    pred = generate_horoscope(rashi["name_en"])
    save_prediction(rashi_id, pred)

    # Get Monthly Predictions
    predictions = get_predictions(rashi_id)

    return render_template('horoscope.html', rashi=rashi, prediction=pred, predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
    
    