import tkinter as tk

def process_query():
    # Placeholder function to process user query and generate response
    user_input = entry.get()
    response = "You said: " + user_input
    text.insert(tk.END, response + "\n")

# Create the main window
root = tk.Tk()
root.title("Chatbot App")

# Create input field
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create button to submit query
submit_button = tk.Button(root, text="Submit", command=process_query)
submit_button.pack()

# Create text area to display responses
text = tk.Text(root, width=50, height=10)
text.pack(pady=10)

# Run the application
root.mainloop()
