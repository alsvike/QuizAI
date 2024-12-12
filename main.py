import json
from groq import Groq

client = Groq(
    api_key="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"
)

subject = input("Enter the subject: (e.g. 'Mathematics', 'Science', 'History', 'Geography', 'English', 'Computer Science', 'Art', 'Music', 'Physical Education', 'Health', 'Foreign Language', 'Other'): ")

prompt = """
Generate a question in the subject [insert subject here], ensuring it is directly relevant to the subject and does not stray into other disciplines. The question should have a difficulty level of 5 (medium) on a scale from 1 to 10. Use the following guidelines for difficulty levels:

Levels 1–3: Easy — Simple, well-known facts or basic concepts. Requires minimal recall or thought.
Levels 4–6: Medium — Moderately challenging, involving less common knowledge or questions requiring some analysis or contextual understanding.
Levels 7–10: Hard — Complex, nuanced topics, requiring detailed knowledge or interpretation of events.
Return the result as a JSON object without any additional text, explanations, or formatting. The JSON object must include the following fields:

question: A well-phrased question that directly pertains to the specified subject.
choice1, choice2, choice3, choice4: Four distinct answer options as complete pieces of text.
correctAnswer: The exact text of the correct answer, not the label (e.g., choice2), but the full text of the correct answer. For example: "HATs add acetyl groups to histone proteins, whereas HDACs remove these groups, allowing for chromatin compaction and/or gene regulation."
Ensure that the question fits the specified difficulty (level 5) by requiring moderate knowledge or analysis. The incorrect choices should be plausible but clearly distinguishable from the correct one. Focus strictly on the chosen subject and its relevant concepts. Return only the JSON object.
"""

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant specialized in writing formal documents."},
        {"role": "user", "content": prompt}
    ],
    model="llama3-8b-8192",  # Specify the model as needed
)

response = chat_completion.choices[0].message.content

# Debugging: Print the raw response
print("Raw API Response:")
print(response)

# Attempt to parse JSON
try:
    # Extract the JSON part of the response
    json_start = response.find("{")
    json_end = response.rfind("}") + 1
    cleaned_response = response[json_start:json_end]

    quiz_data = json.loads(cleaned_response)  # Parse the JSON string
except json.JSONDecodeError as e:
    print("\nError decoding JSON:")
    print(e)
    print("\nEnsure the API response is valid JSON.")
    exit()

# Display the question and choices
print(f"\nQuestion: {quiz_data['question']}\n")
print("Choices:")
for i in range(1, 5):
    print(f"{i}. {quiz_data[f'choice{i}']}")

# Ask the user to select an answer
user_answer = input("\nEnter the number of your answer: ")

# Validate the user's answer
try:
    user_answer = int(user_answer)
    if 1 <= user_answer <= 4:
        selected_choice = quiz_data[f'choice{user_answer}']
        if selected_choice == quiz_data['correctAnswer']:
            print("\nCorrect! Well done.")
        else:
            print(f"\nIncorrect. The correct answer is: {quiz_data['correctAnswer']}")
    else:
        print("\nInvalid input. Please select a number between 1 and 4.")
except ValueError:
    print("\nInvalid input. Please enter a numeric value between 1 and 4.")