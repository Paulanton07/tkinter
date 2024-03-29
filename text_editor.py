import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Paul's Editor")

text_area = tk.Text(root, width=80, height=30, font=("Arial", 20), bg="lightgreen")
text_area.pack()

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)

def new_file():
    """Function to clear text area for a new file."""
    text_area.delete(1.0, tk.END)

def increase_font_size():
    """Function to increase font size (implementation details omitted)."""
    current_size = text_area.cget("font").split()[1]
    new_size = int(current_size) + 2
    text_area.config(font=(text_area.cget("font").split()[0], new_size))

def save_file():
    """Function to save text content to a file."""
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        try:
            with open(filename, "w") as file:
                file.write(text_area.get(1.0, tk.END))
            # Display success message (optional)
        except FileNotFoundError:
            # Handle error if file cannot be created
            pass

def retrieve_file():
    """Function to retrieve text content from a file."""
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        try:
            with open(filename, "r") as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
            # Display success message (optional)
        except FileNotFoundError:
            # Handle error if file cannot be opened
            pass

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

retrieve_button = tk.Button(root, text="Retrieve", command=retrieve_file)
retrieve_button.pack()

# Implement buttons or dropdown menu for font size adjustment (refer to omitted details)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)  # Added Save option
file_menu.add_command(label="Retrieve", command=retrieve_file)  # Added Retrieve option
# Add more menu options like Open (implementation details omitted)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
