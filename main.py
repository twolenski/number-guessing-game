import random, tkinter as tk

window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("500x200")
window.resizable(False, False)

title_label = tk.Label(window, text="Welcome to my Number Guessing Game!",
                       font=("Arial",16),
                        fg="blue",
                        width=35,
                        height=0
                       )
                       
guess_status = tk.Label(window, text="Your objective is to guess a number between 1 and 100.",
                        font=("Arial",12),
                        fg="Red",
                        width=50,
                        height=0
                       )

number_entry = tk.Entry(window)

def generateRandomNumber():
    generatedNumber = random.randint(1,100)
    return generatedNumber

randomNumber = generateRandomNumber()
print(randomNumber)


def on_enter(_):
    user_input = number_entry.get()
    try:
        user_input = int(user_input)
        print("Check 2")
        if user_input > randomNumber:
            guess_status.config(text="Incorrect: Guess too high.")
        elif user_input < randomNumber:
            guess_status.config(text="Incorrect: Guess too low.")
        else:
            guess_status.config(text="Your guess was correct!", fg = "Green")
            title_label.config(text="You win!", fg = "Green")
    except ValueError:
        guess_status.config(text="Invalid input: not a number")
        return



number_entry.bind("<Return>", on_enter)
title_label.pack(pady=10)
guess_status.pack(pady=5)
number_entry.pack(pady=10)


window.mainloop()

