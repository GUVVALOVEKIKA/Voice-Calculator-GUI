import tkinter as tk
import speech_recognition as sr
import pyttsx3
import math

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to make the calculator speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and process calculation
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...", fg="yellow")
        root.update()
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)  # Faster response time
            command = recognizer.recognize_google(audio).lower()
            status_label.config(text="Processing...", fg="orange")
            current_operation_label.config(text=f"Performing: {command}")  # Show current operation

            # Calculate result
            result = calculate(command)
            output_label.config(text=f"Result: {result}", fg="white", bg="blue")

            # Display current calculation below Speak button
            calculation_label.config(text=f"Calculation: {command}")

            # Speak the result
            speak(f"The result is {result}")

        except sr.UnknownValueError:
            output_label.config(text="Could not understand. Try again.", fg="red")
            speak("Could not understand. Try again.")
        except sr.RequestError:
            output_label.config(text="Could not connect to the service.", fg="red")
            speak("Could not connect to the service.")

# Function to process mathematical expressions
def calculate(expression):
    try:
        # Replace words with mathematical symbols
        expression = expression.replace("plus", "+").replace("minus", "-")
        expression = expression.replace("times", "").replace("multiplied by", "")
        expression = expression.replace("divided by", "/").replace("over", "/")
        expression = expression.replace("x", "").replace("power", "*")

        # Advanced calculations
        if "square root of" in expression:
            num = float(expression.split("square root of")[1])
            return round(math.sqrt(num), 4)

        if "log" in expression:
            num = float(expression.split("log")[1])
            return round(math.log(num), 4)

        if "sin" in expression:
            num = float(expression.split("sin")[1])
            return round(math.sin(math.radians(num)), 4)

        if "cos" in expression:
            num = float(expression.split("cos")[1])
            return round(math.cos(math.radians(num)), 4)

        if "tan" in expression:
            num = float(expression.split("tan")[1])
            return round(math.tan(math.radians(num)), 4)

        # Evaluate the final expression
        return round(eval(expression), 4)

    except Exception:
        return "Error"

# GUI Setup
root = tk.Tk()
root.title("Advanced Voice Calculator")
root.geometry("600x400")  # Adjusted size without image
root.configure(bg="#1E1E2E")  # Dark-themed background

# Title Label
title_label = tk.Label(root, text="🎤 Advanced Voice Calculator", font=("Verdana", 20, "bold"), fg="cyan", bg="#1E1E2E")
title_label.pack(pady=10)

# Main content frame
main_frame = tk.Frame(root, bg="#1E1E2E")
main_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Left side: Operations Guide
operations_frame = tk.Frame(main_frame, bg="#252538", padx=15, pady=15)
operations_frame.pack(side="left", padx=10, pady=10, fill="y")

tk.Label(operations_frame, text="How to Speak:", font=("Verdana", 14, "bold"), bg="#252538", fg="white").pack(anchor="w", pady=5)
tk.Label(operations_frame, text="Addition: 'plus'", font=("Verdana", 12), bg="#252538", fg="lightgray").pack(anchor="w", pady=2)
tk.Label(operations_frame, text="Subtraction: 'minus'", font=("Verdana", 12), bg="#252538", fg="lightgray").pack(anchor="w", pady=2)
tk.Label(operations_frame, text="Multiplication: 'times' or 'multiplied by'", font=("Verdana", 12), bg="#252538", fg="lightgray").pack(anchor="w", pady=2)
tk.Label(operations_frame, text="Division: 'divided by' or 'over'", font=("Verdana", 12), bg="#252538", fg="lightgray").pack(anchor="w", pady=2)
tk.Label(operations_frame, text="Square Root: 'square root of 9'", font=("Verdana", 12), bg="#252538", fg="lightgray").pack(anchor="w", pady=2)
tk.Label(operations_frame, text="Power: 'two power three'", font=("Verdana", 12), bg="#252538", fg="lightgray").pack(anchor="w", pady=2)
tk.Label(operations_frame, text="Logarithm: 'log 100'", font=("Verdana", 12), bg="#252538", fg="lightgray").pack(anchor="w", pady=2)
tk.Label(operations_frame, text="Trigonometry: 'sin 30', 'cos 45', 'tan 60'", font=("Verdana", 12), bg="#252538", fg="lightgray").pack(anchor="w", pady=2)

# Center panel: Output and Controls
center_frame = tk.Frame(main_frame, bg="#1E1E2E")
center_frame.pack(expand=True)

# Listening Status Label
status_label = tk.Label(center_frame, text="Waiting for input...", font=("Verdana", 12, "italic"), bg="#1E1E2E", fg="yellow")
status_label.pack(pady=5)

# Output Label
output_label = tk.Label(center_frame, text="", font=("Verdana", 18, "bold"), fg="white", bg="blue", width=25, height=2)
output_label.pack(pady=20)

# Current Operation Label
current_operation_label = tk.Label(center_frame, text="", font=("Verdana", 12, "bold"), fg="white", bg="#252538")
current_operation_label.pack(pady=5)

# Speak Button
button = tk.Button(center_frame, text="🎤 Speak", command=recognize_speech, font=("Verdana", 14, "bold"), bg="green", fg="white", padx=10, pady=5)
button.pack(pady=5, padx=50, anchor="w")  # Move left

# Current Calculation Label
calculation_label = tk.Label(center_frame, text="", font=("Verdana", 12, "italic"), fg="lightgray", bg="#1E1E2E")
calculation_label.pack(pady=5)

# Footer Label
footer_label = tk.Label(root, text="Created by My Bangaram ❤", font=("Verdana", 10, "italic"), fg="gray", bg="#1E1E2E")
footer_label.pack(side="bottom", pady=5)

# Run the GUI
root.mainloop()