# 🧠 QuizAI: Endless Learning Quiz Generator

## 📝 Overview

QuizAI is an innovative and interactive quiz application designed to challenge and expand your knowledge across a wide range of subjects. Whether you're a student, a professional, or just curious, QuizAI offers a personalized quiz experience that dynamically generates questions tailored to your chosen discipline.

With a library of subjects ranging from Mathematics and Science to Art and Music, QuizAI adapts to your preferences, creating endless opportunities for learning and self-improvement. Each question is thoughtfully crafted with varying levels of difficulty to keep you engaged, whether you're brushing up on basics or diving into more advanced topics.

Take on the Endless Quiz Challenge, where the goal is simple: keep answering correctly to advance and see how far your knowledge can take you! Packed with features like score tracking, progress feedback, and interactive question formats, QuizAI is perfect for both casual users and competitive learners looking to test their limits.

Dive in and make learning exciting—one question at a time!

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


## 📜 Changelog
Nothing here yet! As more changes come to the python script, then you can see what changes have been made here

## 📄 Future Features:
##### Priorities are as following: HIGH, MEDIUM, LOW:
- (HIGH) Add the ability to use OpenAI API, Claude AI API etc. instead of only Groq API
~~- (HIGH) Add a difficulty to prompt, so the user can select what kind of difficulty they want the questions to be.~~
- (HIGH) Add the ability for user profiles, where you can get:
  - Achievements
  - Stats tracking (Total questions answered, right/wrong ratio etc.)
- (MEDIUM) Time-challenges (Choose between Easy, Medium og Hard)
- (MEDIUM) Track how many questions you've answered correctly in a game

## 🐛 BUGS
##### Priorities are as following: HIGH, MEDIUM, LOW
- (LOW) When answering correct on a question in a given subject, you should not continously select a new subject, but continue on the first chosen subject.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
