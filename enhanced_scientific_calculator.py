import tkinter as tk
from math import sin, cos, tan, log, sqrt, radians, degrees, factorial, gcd
from sympy import lcm  # For LCM calculation
import tkinter.messagebox as msgbox

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Scientific Calculator")
        self.root.geometry("400x700")
        self.root.resizable(False, False)
        self.expression = ""
        self.input_text = tk.StringVar()

        # Display screen
        self.input_frame = tk.Frame(self.root, width=400, height=50)
        self.input_frame.pack(side=tk.TOP)
        self.input_field = tk.Entry(self.input_frame, font=('Arial', 18), textvariable=self.input_text, width=25, bg="#eee", bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        # Button frame
        self.btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        self.btns_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        # Button layout
        button_layout = [
            ["7", "8", "9", "/", "sin", "cos"],
            ["4", "5", "6", "*", "tan", "log"],
            ["1", "2", "3", "-", "sqrt", "^"],
            ["C", "0", ".", "+", "(", ")"],
            ["deg", "rad", "π", "=", "DEL", "Ans"],
            ["fact", "prime", "GCD", "LCM", "bin", "hex"],
            ["C->F", "F->C", "m->km", "kg->lb", "m->ft", "km->mi"]
        ]

        # Create buttons
        for i, row in enumerate(button_layout):
            for j, btn_text in enumerate(row):
                if btn_text == "=":
                    btn = tk.Button(self.btns_frame, text=btn_text, width=6, height=2, bg="#32a852", fg="white", command=self.calculate)
                elif btn_text in ["C", "DEL"]:
                    cmd = self.clear if btn_text == "C" else self.delete
                    btn = tk.Button(self.btns_frame, text=btn_text, width=6, height=2, bg="#ff6666" if btn_text == "C" else "#ffcc66", fg="white", command=cmd)
                else:
                    btn = tk.Button(self.btns_frame, text=btn_text, width=6, height=2, bg="#f2f2f2", command=lambda x=btn_text: self.special_features(x))
                btn.grid(row=i, column=j, padx=1, pady=1)

    def special_features(self, value):
        try:
            if value == "π":
                self.expression += str(3.141592653589793)
            elif value == "^":
                self.expression += "**"
            elif value in ["sin", "cos", "tan", "sqrt", "log"]:
                self.expression += value + "("
            elif value == "deg":
                self.expression = str(degrees(float(self.expression)))
            elif value == "rad":
                self.expression = str(radians(float(self.expression)))
            elif value == "fact":
                self.expression = str(factorial(int(self.expression)))
            elif value == "prime":
                num = int(self.expression)
                self.expression = "Prime" if all(num % i != 0 for i in range(2, int(sqrt(num)) + 1)) else "Not Prime"
            elif value == "GCD":
                self.expression += ","
            elif value == "LCM":
                nums = list(map(int, self.expression.split(",")))
                self.expression = str(lcm(*nums))
            elif value in ["bin", "hex"]:
                num = int(self.expression)
                self.expression = bin(num)[2:] if value == "bin" else hex(num)[2:]
            elif value in ["C->F", "F->C", "m->km", "kg->lb", "m->ft", "km->mi"]:
                self.unit_conversion(value)
            self.input_text.set(self.expression)
        except Exception as e:
            msgbox.showerror("Error", "Invalid Operation")
            self.expression = ""

    def unit_conversion(self, value):
        try:
            num = float(self.expression)
            conversions = {
                "C->F": (num * 9/5) + 32,
                "F->C": (num - 32) * 5/9,
                "m->km": num / 1000,
                "kg->lb": num * 2.20462,
                "m->ft": num * 3.28084,
                "km->mi": num * 0.621371,
            }
            self.expression = str(conversions[value])
        except Exception as e:
            msgbox.showerror("Error", "Invalid Conversion")

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def delete(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression.replace("sin", "sin(radians(")
                                           .replace("cos", "cos(radians(")
                                           .replace("tan", "tan(radians(")
                                           .replace("sqrt", "sqrt")
                                           .replace("log", "log"))
            self.input_text.set(str(result))
            self.expression = str(result)
        except Exception as e:
            msgbox.showerror("Error", "Invalid Calculation")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
