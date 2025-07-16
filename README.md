# AI-Horoscope 🔮

An AI-powered horoscope generator web application that provides personalized daily horoscope predictions for all 12 zodiac signs using machine learning and natural language processing.

## Features ✨

- **AI-Generated Horoscopes**: Utilizes GPT-2 model for generating unique, personalized horoscope predictions
- **Multi-language Support**: Displays zodiac signs in both English and Hindi
- **Daily Predictions**: Get fresh horoscope predictions every day
- **Monthly History**: View your past 30 days of horoscope predictions
- **Responsive Design**: Clean and modern web interface
- **Database Storage**: Persistent storage of predictions using SQLite

## Tech Stack 🛠️

- **Backend**: Python, Flask
- **AI/ML**: Transformers (Hugging Face), GPT-2, PyTorch
- **Database**: SQLite
- **Frontend**: HTML, CSS (with Jinja2 templating)
- **Version Control**: Git

## Installation 🚀

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/jineshsingatkar/AI-Horoscope.git
   cd AI-Horoscope
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and go to `http://localhost:5000`

## Usage 📖

1. **Homepage**: Visit the main page to see all 12 zodiac signs
2. **Select Your Sign**: Click on your zodiac sign to get your horoscope
3. **Daily Prediction**: View your AI-generated daily horoscope
4. **History**: Check your previous predictions from the past month

## Project Structure 📁

```
AI-Horoscope/
├── app.py                 # Main Flask application
├── ai_generator.py        # AI horoscope generation logic
├── database.py           # Database operations
├── rashi_data.py         # Zodiac sign data
├── requirements.txt      # Python dependencies
├── templates/
│   ├── index.html        # Homepage template
│   └── horoscope.html    # Horoscope display template
└── README.md            # Project documentation
```

## API Endpoints 🔌

- `GET /` - Homepage displaying all zodiac signs
- `GET /horoscope/<int:rashi_id>` - Get horoscope for specific zodiac sign

## Dependencies 📦

- **Flask (2.3.3)**: Web framework for Python
- **Transformers (4.35.2)**: Hugging Face library for AI models
- **PyTorch (2.1.0)**: Deep learning framework (required by transformers)

## Database Schema 🗄️

```sql
CREATE TABLE horoscope (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rashi_id INTEGER,
    date TEXT,
    prediction TEXT
);
```

## Zodiac Signs Supported 🌟

| English | Hindi | ID |
|---------|-------|-----|
| Aries | मेष | 1 |
| Taurus | वृषभ | 2 |
| Gemini | मिथुन | 3 |
| Cancer | कर्क | 4 |
| Leo | सिंह | 5 |
| Virgo | कन्या | 6 |
| Libra | तुला | 7 |
| Scorpio | वृश्चिक | 8 |
| Sagittarius | धनु | 9 |
| Capricorn | मकर | 10 |
| Aquarius | कुंभ | 11 |
| Pisces | मीन | 12 |

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements 🚀

- [ ] Add user authentication and profiles
- [ ] Implement multiple AI models for variety
- [ ] Add weekly and monthly horoscope predictions
- [ ] Include compatibility matching between signs
- [ ] Add email notifications for daily horoscopes
- [ ] Implement caching for better performance
- [ ] Add REST API for mobile app integration
- [ ] Multi-language support for predictions



## Author 👨‍💻

**Jinesh Singatkar**
- GitHub: [@jineshsingatkar](https://github.com/jineshsingatkar)
- Email: jineshsingatkar@gmail.com

## Acknowledgments 🙏

- Hugging Face for the Transformers library
- OpenAI for the GPT-2 model
- Flask community for the excellent web framework
- All contributors and users of this project

---

⭐ **If you found this project helpful, please give it a star!** ⭐
