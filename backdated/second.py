import tkinter as tk
from transformers import TFAutoModelForCausalLM, AutoTokenizer

# Initialize DialoGPT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = TFAutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Function to process user input and generate response
def process_query():
    user_input = entry.get()
    response = generate_response(user_input)
    text.insert(tk.END, "User: " + user_input + "\n")
    text.insert(tk.END, "Bot: " + response + "\n")
    entry.delete(0, tk.END)

# Function to generate response using DialoGPT model
def generate_response(user_input):
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="tf")
    response_ids = model.generate(input_ids, max_length=100, num_return_sequences=1)
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response_text

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot App")

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
