from groq import Groq

client = Groq(
    api_key="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"
)

subject = input("Enter the subject: (e.g. 'Mathematics', 'Science', 'History', 'Geography', 'English', 'Computer Science', 'Art', 'Music', 'Physical Education', 'Health', 'Foreign Language', 'Other'): ")

prompt = """
Generate a question in the subject {subject}, ensuring it is directly relevant to the subject and does not stray into other disciplines. The question should have a difficulty level of 5 (medium) on a scale from 1 to 10. Use the following guidelines for difficulty levels:

Levels 1–3: Easy — Simple, well-known facts or basic concepts. Requires minimal recall or thought.
Levels 4–6: Medium — Moderately challenging, involving less common knowledge or questions requiring some analysis or contextual understanding.
Levels 7–10: Hard — Complex, nuanced topics, requiring detailed knowledge or interpretation of events.
Return the result as a JSON object without any additional text, explanations, or formatting. The JSON object must include the following fields:

question: A well-phrased question that directly pertains to the specified subject.
choice1, choice2, choice3, choice4: Four distinct answer options as complete pieces of text.
correctAnswer: The full text of the correct answer, exactly as it appears in one of the choices (choice1, choice2, choice3, or choice4). Do not return just the label (e.g., choice3), but instead the corresponding full text, e.g., "H2A promotes chromatin condensation by binding to other histone proteins, such as H3 and H4, facilitating the formation of higher-order chromatin structures."
Ensure the question fits the specified difficulty (level 5) by requiring moderate knowledge or analysis, and that the incorrect choices are plausible but clearly distinguishable from the correct one. Focus strictly on the chosen subject and its relevant concepts. Return only the JSON object, and ensure the correctAnswer field contains the full text of the correct choice.
"""

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant specialized in writing formal documents."},
        {"role": "user", "content": prompt}
    ],
    model="llama3-8b-8192",  # Specify the model as needed
)

response = chat_completion.choices[0].message.content

print(response)