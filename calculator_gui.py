import tkinter as tk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.calculator = Calculator()

        # Display Entry
        self.display = tk.Entry(root, width=25, font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
                      command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear Button
        tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14),
                  command=self.clear_click).grid(row=5, column=0, columnspan=4)

    def button_click(self, char):
        if char == '=':
            self.calculator.calculate()
        elif char in ['+', '-', '*', '/']:
            self.calculator.append_operator(char)
        else:
            self.calculator.append_number(char)
        self.update_display()

    def clear_click(self):
        self.calculator.clear()
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.calculator.get_display())

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()