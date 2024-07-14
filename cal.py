import tkinter as tk

# Function to update the display when buttons are clicked
def on_button_click(value):
    current_text = display_var.get()
    
    if value == '=':
        try:
            result = str(eval(current_text))
            display_var.set(result)
        except:
            display_var.set("Error")
    elif value == 'C':
        display_var.set("")
    else:
        display_var.set(current_text + value)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry field to display the calculation
display_var = tk.StringVar()
display = tk.Entry(window, textvariable=display_var, font=('Helvetica', 20), justify='right')
display.grid(row=0, column=0, columnspan=4)

# Define the button layout for the calculator
button_text = [
    'C','/','*','-',
    '7','8','9','+',
    '4','5','6','=',
    '1','2','3','0'
]

row_val, col_val = 1, 0
for text in button_text:
    tk.Button(window, text=text, font=('Helvetica', 16), command=lambda t=text: on_button_click(t)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid rows and columns to expand with window size
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

window.mainloop()