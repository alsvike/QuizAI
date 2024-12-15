import json
import os
import logging
from typing import Dict, Optional
from dotenv import load_dotenv
from groq import Groq

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Subjects list for QuizAI
VALID_SUBJECTS = [
    'Mathematics', 'Science', 'History', 'Geography', 'English', 
    'Computer Science', 'Art', 'Music', 'Physical Education', 
    'Health', 'Foreign Language', 'Other'
]

# Difficulty levels
DIFFICULTY_LEVELS = {
    1: "Very Easy (Levels 1-3)",
    2: "Easy (Levels 1-3)",
    3: "Medium-Easy (Levels 3-4)",
    4: "Medium (Levels 4-6)",
    5: "Medium-Hard (Levels 6-7)",
    6: "Hard (Levels 7-9)",
    7: "Very Hard (Levels 8-10)"
}

class QuizAI:
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize QuizAI with optional API key.
        Attempts to load API key from environment variables if not provided.
        """
        # Load environment variables
        load_dotenv()
        
        # Use provided API key or load from environment
        self.api_key = api_key or os.getenv('GROQ_API_KEY')
        
        if not self.api_key:
            raise ValueError("No API key found for QuizAI. Please provide an API key or set GROQ_API_KEY environment variable.")
        
        # Initialize Groq client
        self.client = Groq(api_key=self.api_key)
    
    def generate_quiz_prompt(self, subject: str, difficulty: int) -> str:
        """
        Generate a standardized prompt for QuizAI question generation.
        
        Args:
            subject (str): The subject for the QuizAI question
            difficulty (int): Difficulty level from 1 to 7
        
        Returns:
            str: Formatted prompt for question generation
        """
        # Map difficulty to actual difficulty ranges
        difficulty_mapping = {
            1: "1-3",   # Very Easy
            2: "1-3",   # Easy
            3: "3-4",   # Medium-Easy
            4: "4-6",   # Medium
            5: "6-7",   # Medium-Hard
            6: "7-9",   # Hard
            7: "8-10"   # Very Hard
        }
        
        return f"""
Generate a question in the subject {subject}, ensuring it is directly relevant to the subject and does not stray into other disciplines. The question should have a difficulty level in the range {difficulty_mapping[difficulty]} on a scale from 1 to 10. Use the following guidelines for difficulty levels:

Levels 1–3: Easy — Simple, well-known facts or basic concepts. Requires minimal recall or thought.
Levels 4–6: Medium — Moderately challenging, involving less common knowledge or questions requiring some analysis or contextual understanding.
Levels 7–10: Hard — Complex, nuanced topics, requiring detailed knowledge or interpretation of events.
Return the result as a JSON object without any additional text, explanations, or formatting. The JSON object must include the following fields:

question: A well-phrased question that directly pertains to the specified subject.
choice1, choice2, choice3, choice4: Four distinct answer options as complete pieces of text.
correctAnswer: The exact text of the correct answer, not the label (e.g., choice2), but the full text of the correct answer.
Ensure that the question fits the specified difficulty level by requiring knowledge or analysis appropriate to the difficulty range. The incorrect choices should be plausible but clearly distinguishable from the correct one. Focus strictly on the chosen subject and its relevant concepts. Return only the JSON object.
"""
    
    def get_quiz_question(self, subject: str, difficulty: int) -> Dict:
        """
        Retrieve a quiz question for the given subject in QuizAI.
        
        Args:
            subject (str): The subject for the quiz question
            difficulty (int): Difficulty level from 1 to 7
        
        Returns:
            Dict: Parsed quiz question data
        """
        try:
            # Create chat completion
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant specialized in writing formal documents."},
                    {"role": "user", "content": self.generate_quiz_prompt(subject, difficulty)}
                ],
                model="llama3-8b-8192",
            )
            
            response = chat_completion.choices[0].message.content
            
            # Extract JSON from response
            json_start = response.find("{")
            json_end = response.rfind("}") + 1
            cleaned_response = response[json_start:json_end]
            
            return json.loads(cleaned_response)
        
        except json.JSONDecodeError as e:
            logger.error(f"JSON Decoding Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Error generating QuizAI question: {e}")
            raise
    
    def run_quiz(self):
        """
        Main method to run the interactive QuizAI generator in endless mode.
        The quiz continues until the user answers a question incorrectly.
        """
        print("🧠 Welcome to QuizAI - Endless Quiz Challenge! 🚀")
        print("Keep answering correctly to continue. One wrong answer ends the game!\n")
        
        score = 0
        try:
            while True:
                # Get subject input with validation
                while True:
                    subject = input(f"Enter the subject (Choose from {', '.join(VALID_SUBJECTS)}): ").strip().title()
                    if subject in VALID_SUBJECTS:
                        break
                    print("Invalid subject. Please choose from the list.")
                
                # Get difficulty input with validation
                while True:
                    print("\nSelect Difficulty Level:")
                    for key, value in DIFFICULTY_LEVELS.items():
                        print(f"{key}. {value}")
                    
                    try:
                        difficulty = int(input("\nEnter the number of your chosen difficulty: "))
                        if difficulty in DIFFICULTY_LEVELS:
                            break
                        print("Invalid difficulty. Please select a number between 1 and 7.")
                    except ValueError:
                        print("Please enter a numeric value between 1 and 7.")
                
                # Generate and display quiz question
                quiz_data = self.get_quiz_question(subject, difficulty)
                
                print(f"\nQuestion: {quiz_data['question']}\n")
                print("Choices:")
                for i in range(1, 5):
                    print(f"{i}. {quiz_data[f'choice{i}']}")
                
                # Get and validate user answer
                while True:
                    try:
                        user_answer = int(input("\nEnter the number of your answer: "))
                        if 1 <= user_answer <= 4:
                            break
                        print("Invalid input. Please select a number between 1 and 4.")
                    except ValueError:
                        print("Please enter a numeric value between 1 and 4.")
                
                # Check answer
                selected_choice = quiz_data[f'choice{user_answer}']
                if selected_choice == quiz_data['correctAnswer']:
                    score += 1
                    print(f"\n✅ Correct! Current Score: {score}")
                else:
                    print(f"\n❌ Incorrect. The correct answer is: {quiz_data['correctAnswer']}")
                    print(f"\n🏁 Game Over! Your final score is: {score}")
                    break
            retry = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if retry == "yes":
                self.run_quiz()
            elif retry == "y":
                self.run_quiz()
            else:
                print("Thank you for playing QuizAI!")
        
        
        except KeyboardInterrupt:
            print(f"\n\nQuizAI terminated by user. Final Score: {score}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            print(f"An error occurred. Final Score: {score}")

def main():
    """
    Entry point for the QuizAI application.
    """
    try:
        quiz_ai = QuizAI()
        quiz_ai.run_quiz()
    except ValueError as e:
        logger.error(str(e))
        print("QuizAI Configuration Error: ", str(e))
    except Exception as e:
        logger.error(f"QuizAI unhandled error: {e}")
        print("An unexpected error occurred in QuizAI.")

if __name__ == "__main__":
    main()