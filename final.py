import tkinter as tk
import requests

# Set your OpenAI API key
api_key = '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'

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
root.title("BotBuddy - Your AI Assistant")

# Set background color
root.configure(bg="#f0f0f0")

# Add BotBuddy title with colored text
title_label = tk.Label(root, text="BotBuddy - Your Buddy", font=("Helvetica", 20), foreground="blue", bg="#f0f0f0")
title_label.pack()

# Create input field with colored background
entry = tk.Entry(root, width=70, bg="lightgray")
entry.pack(pady=20)

# Create button to submit query with colored background
submit_button = tk.Button(root, text="SUBMIT", command=process_query, bg="blue", fg="white")
submit_button.pack()

# Create text area to display conversation with colored background
text = tk.Text(root, width=100, height=40, bg="white")
text.pack(pady=10)

# Run the application
root.mainloop()
