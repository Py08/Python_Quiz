import tkinter as tk
import sys
import datetime as dt

questions = {
    1 : "Who invented Python? \n a.Guido van Rossum, b.Tom Williams, c.James Gosling, d.William Wordsworth",
    2 : "Which Language did Guido van Rossum use to develop python? \n a.Java, b.C, c.Ruby, d.Json",
    3 : "Which Function do you use to print something? \n a.write(), b.say(), c.paragraph(), d.print()",
    4 : "How many ways are there to use a formatted print? \n a.1, b.2, c.3, d.4",
    5 : "What do you use to download a package in Command Prompt / Terminal? \n a.get package, b.install, c.pip install, d.download",
    6 : "How do you use a module/package? \n a.use, b.get, c.bring, d.import",
    7 : "What is the package to use arrays? \n a.PIL, b.pandas, c.array, d.numpy",
    8 : "The simplest package for GUI: \n a.PIL, b.numpy, c.tkinter, d.pandas",
    9 : "Which of these is a loop? \n a.for, b.forever, c.be_running, d.repeat",
    10 : "How to get all items in a dictionary? \n a.dict.get(), b.dict.all(), c.dict.items(), d.dict.everything()"
    }

answers_options = {
    1 : 'a.Guido van Rossum',
    2 : 'b.C',
    3 : 'd.print()',
    4 : 'c.3',
    5 : 'c.pip install',
    6 : 'd.import',
    7 : 'd.numpy',
    8 : 'c.tkinter',
    9 : 'a.for',
    10 : 'c.dict.items()'}

score = 0
correct_ans_list = []
qs = questions.items()

for key, value in answers_options.items():
    correct_ans_list.append(value)

def next_butt():
    welcome.withdraw()
    global cont
    cont = tk.Tk()
    cont.title("Continue?")
    cont.configure(background = 'Cyan')
    contin = tk.Label(cont, text = "\nDo you want to continue?\n", font = ("Comic Sans MS", 16), bg = 'cyan', fg = 'green').pack(side = 'left')
    n = tk.Button(cont, text = "No", command = no, font = ("Comic Sans MS", 14), padx = 10, pady = 10, bd = 6, bg = 'blue', fg = 'white')
    y = tk.Button(cont, text = "Yes", command = yes, font = ("Comic Sans MS", 14), padx = 10, pady = 10, bd = 6, bg = 'blue', fg = 'white')
    y.pack(side = "left")
    n.pack(side = "left")

def yes():
    game_ended = False
    cont.withdraw()
    q_no = 1
    q_index = 0
    q_nos = list(questions.keys())

    def play():

        def submit(): 

            def stop_excecuting():
                sys.exit(0)

            def next_q():
                res.destroy()
                nonlocal q_no
                nonlocal q_index
                q_no += 1
                q_index += 1

                if q_no == 11:
                    good = tk.Tk()
                    good.title("Congrats")
                    good.configure(background = 'cyan')
                    appreceation = tk.Label(good, text = "Congrats, You have won with 10 points!!!", font = ("Comic Sans MS", 16), bg = 'cyan', fg = 'green').pack()
                    ok = tk.Button(good, text = "OK", command = stop_excecuting, padx = 14, pady = 14, bd = 6, font = ("Comic Sans MS", 16), bg = 'blue', fg = 'white').pack()

                else:
                    play()

            res = tk.Tk()
            res.configure(background = 'cyan')

            ans = enter.get()

            correct_ans = correct_ans_list[q_index]

            l = correct_ans.split('.')
            correct_option = correct_ans.split('.')

            if ans == correct_option[0]:
                res.title("Correct!")
                play_window.withdraw()
                global score
                score += 1
                correct = tk.Label(res, text = (f"Correct!\nYour Score is {score}"), font = ("Comic Sans MS", 14), fg = 'green', bg = 'cyan').pack()
                ok_button = tk.Button(res, padx = 14, pady = 10, bd = 6, command = next_q, text = "OK", font = ("Comic Sans MS", 16), fg = 'white', bg = 'blue').pack()

            else:
                res.title("Wrong!")
                play_window.withdraw()
                wrong = tk.Label(res, text = (f"Wrong\nThe Correct Answer was option {correct_ans_list[q_index]}\nYour Score is {score}"), font = ("Comic Sans MS", 14), fg = 'green', bg = 'cyan').pack()
                ok_button = tk.Button(res, padx = 14, pady = 14, bd = 6, command = stop_excecuting, text = "OK", font = ("Comic Sans MS", 16), bg = 'blue', fg = 'white').pack()

            res.mainloop()

        play_window = tk.Tk()
        play_window.title(f"Question {q_nos[q_index]}")
        play_window.configure(background = 'cyan')
        key = q_nos[q_index]
        q = tk.Label(play_window, text = (f"Q{q_nos[q_index]}. {questions.get(key)}"), bg = 'cyan', fg = 'green', font = ("Comic Sans MS", 14)).pack()
        enter = tk.Entry(play_window, width = 50, bd = 4, bg = 'tomato', fg = 'black')
        enter.pack()
        sub = tk.Button(play_window, text = "Submit", command = submit, padx = 10, pady = 10, font = ("Comic Sans MS", 14), bd = 6, bg = 'blue', fg = 'white').pack()
        play_window.mainloop()

    if game_ended == False:
        play()

    else:
        sys.exit(0)

def no():

    def out():
        sys.exit(0)

    cont.withdraw()
    thank_you = tk.Tk()
    thank_you.title("Thanks for Playing !")
    thank_you.configure(background = 'cyan')
    thanks = tk.Label(thank_you, text = (f"Thank You for playing.\nYour score is {score}"), font = ("Comic Sans MS", 16), fg = 'green', bg = 'cyan').pack()
    end = tk.Button(thank_you, text = "OK", command = out, padx = 14, pady = 14, bd = 6, bg = 'blue', fg = 'white').pack()

welcome = tk.Tk()
welcome.title("Python Quiz")
welcome.configure(background = 'cyan')
rules = tk.Label(welcome, text = "Welcome to Python Quiz.\nRULES:\n    This is a python quiz.\n    It will ask you 10 questions with 4 options.\n    Type in the correct answer in the text box.\n    If You are correct it will move on to the next one.\n    If you are wrong it will stop and tell your score.\nWARNING: If you enter an invalid input it will take the negetive one always.\nHere it goes...", font=("Comic Sans MS", 16), fg = 'green', bg = 'Cyan').pack()
next_button = tk.Button(welcome, text = "Next >>>", padx = 10, pady = 10, bg = "Blue", fg = 'white', bd = 6, font = ("Comic Sans MS", 14), command = next_butt).pack()
welcome.mainloop()
