# 🧠 QuizAI: Endless Learning Quiz Generator

## 📝 Overview

QuizAI is an interactive, subject-based quiz application that generates dynamic questions across various disciplines. Test and expand your knowledge with an endless quiz challenge that adapts to your chosen subject!

## ✨ Features

- **Multiple Subjects**: Quiz across 12 different academic subjects
- **Adaptive Difficulty**: Medium-level questions (difficulty level 5)
- **Endless Mode**: Continue answering questions until you get one wrong
- **Real-time Scoring**: Track your quiz performance
- **Error Handling**: Robust input validation and error management

## 🚀 Supported Subjects

- Mathematics
- Science
- History
- Geography
- English
- Computer Science
- Art
- Music
- Physical Education
- Health
- Foreign Language
- Other

## 🔧 Prerequisites

- Python 3.8+
- Groq API Key
- `python-dotenv`
- `groq` library

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/QuizAI.git
   cd QuizAI
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Configuration

1. Obtain a Groq API Key from the [Groq Platform](https://console.groq.com/)
2. Set up your API key:
   - Create a `.env` file in the project root
   - Add your API key: `GROQ_API_KEY=your_groq_api_key_here`

## 🎮 How to Run

```bash
python quiz_ai.py
```

## 🎲 Game Instructions

- Choose a subject from the provided list
- Answer multiple-choice questions
- Keep answering correctly to increase your score
- One wrong answer ends the game

## 🛠️ Error Handling

- Invalid subject selection will prompt you to choose again
- Numeric input validation for answer selection
- Graceful error handling and logging

## 📄 License

[Specify your license here, e.g., MIT License]

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
