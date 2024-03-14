import tkinter as tk
import requests

# Set your OpenAI API key
api_key = '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'

# Function to generate response using OpenAI API
# Function to generate response using OpenAI API
def generate_response(prompt):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo-instruct",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.7
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    # Check for successful response
    if response.status_code == 200:
        response_data = response.json()
        
        # Check for 'choices' field in response
        if "choices" in response_data:
            return response_data["choices"][0]["text"].strip()
        else:
            print("Response does not contain 'choices' field:", response_data)
            return "Error: Unexpected response format."
    
    # Handle failed API request
    else:
        print("Failed to make API request. Status code:", response.status_code)
        print("Response content:", response.content)
        return "Error: Failed to generate response. Please try again later."



# Function to handle button click and generate response
def process_query():
    user_input = entry.get()
    response = generate_response(user_input)
    text.insert(tk.END, "User: " + user_input + "\n")
    text.insert(tk.END, "Bot: " + response + "\n")
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("BotBuddy - An AI ChatBot")

title_label = tk.Label(root, text="BotBuddy - Your Buddy", font=("Helvetica", 20))
title_label.pack()

# Create input field
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create button to submit query
submit_button = tk.Button(root, text="Submit", command=process_query)
submit_button.pack()

# Create text area to display conversation
text = tk.Text(root, width=80, height=20)
text.pack(pady=10)

# Run the application
root.mainloop()

