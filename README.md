```markdown
# QuizAI - Interactive Quiz Generator

QuizAI is a Python application that uses Groq's AI to dynamically generate subject-specific quiz questions. It challenges users in an endless quiz mode, where one wrong answer ends the game. This README provides clear instructions to help any user set up and run the script without issues.

## Features

- Interactive endless quiz mode.
- Supports multiple subjects, including Mathematics, Science, History, and more.
- Dynamically generates quiz questions with multiple-choice answers.
- Questions are standardized with a medium difficulty level (5/10).

---

## Requirements

- Python 3.8 or newer.
- The following Python libraries:
  - dotenv
  - groq
  - logging
- A valid Groq API key for accessing the AI features.

---

## Installation Guide

### Step 1: Clone the Repository

git clone https://github.com/yourusername/quizai.git  
cd quizai  

### Step 2: Install Dependencies

Make sure you have `pip` installed and run:  

pip install -r requirements.txt  

### Step 3: Set Up the `.env` File

Create a `.env` file in the project root to store your API key. Add the following line to the file:  

GROQ_API_KEY=your_api_key_here  

Replace `your_api_key_here` with your actual API key.

---

## How to Use

### Running the Script

To start the application, execute the following command in your terminal:  

python quiz_ai.py  

### Interactive Quiz Instructions

1. **Choose a Subject**  
   After launching, you will be prompted to choose a subject. Enter one from the following list:  

   Mathematics, Science, History, Geography, English, Computer Science, Art, Music,  
   Physical Education, Health, Foreign Language, Other  

2. **Answer Questions**  
   - A multiple-choice question will be displayed.
   - Choose an answer by entering the corresponding number (1–4). For example:  

     Question: What is the capital of France?  
     Choices:  
     1. Berlin  
     2. Paris  
     3. Madrid  
     4. Rome  

     Enter the number of your answer: 2  

3. **Game Continuation**  
   - If your answer is correct, the quiz continues with a new question.
   - If your answer is incorrect, the game ends, and your score is displayed.

4. **Exiting the Game**  
   To exit the game at any time, close the terminal window or stop the script with `CTRL+C`.

---

Enjoy your quiz experience with QuizAI!
```
