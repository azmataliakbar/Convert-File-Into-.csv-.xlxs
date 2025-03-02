class Calculator:
    def __init__(self):
        self.current_input = ""
        self.result = None

    def append_number(self, number):
        self.current_input += str(number)

    def append_operator(self, operator):
        self.current_input += operator

    def clear(self):
        self.current_input = ""
        self.result = None

    def calculate(self):
        try:
            self.result = eval(self.current_input)
            self.current_input = str(self.result)
        except (SyntaxError, ZeroDivisionError):
            self.current_input = "Error"
            self.result = None

    def get_display(self):
        return self.current_input