# ai_generator.py
from transformers import pipeline
from rashi_data import rashis
from datetime import datetime

generator = pipeline('text-generation', model='gpt2')

def generate_horoscope(rashi_name):
    today = datetime.now().strftime("%B %d, %Y")
    prompt = f"Generate a short horoscope in English for {rashi_name} on {today}. Keep it positive and concise."
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']