from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None


window = Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Pomodoro")
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    #
    # work_sec = WORK_MIN
    # short_break_sec = SHORT_BREAK_MIN
    # long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        timer(long_break_sec)
        title_text.config(text="Break", fg=RED, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    elif reps % 2 == 0:
        timer(short_break_sec)
        title_text.config(text="Break", fg=PINK, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    else:
        timer(work_sec)
        title_text.config(text="Work", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)

    # start_timer()


def reset_timer():
    global time
    global reps
    window.after_cancel(time)
    title_text.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    tick.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def timer(count):
    global time
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        time = window.after(1000, timer, count-1)
    else:
        if reps % 2 == 0:
            new_txt = "✓" * (reps//2)
            tick.config(text=new_txt, fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
        start_timer()



# ---------------------------- UI SETUP -------------------------------


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title_text.grid(column=1, row=0)

b_left = Button(text="start", command=start_timer)
b_left.grid(row=2, column=0)

b_left = Button(text="reset", command=reset_timer)
b_left.grid(row=2, column=2)

tick = Label()
tick.grid(row=3, column=1)

window.mainloop()