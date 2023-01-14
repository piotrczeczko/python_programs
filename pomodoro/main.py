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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    button_start.config(state=NORMAL)
    button_reset.config(state=DISABLED)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1:
        button_start.config(state=DISABLED)
        button_reset.config(state=NORMAL)

    if reps % 2 == 0:
        timer_label.config(text='Break', bg=YELLOW, fg=PINK, font=(FONT_NAME, 28))
        count_down(short_break_sec)
    elif reps % 8 == 0:
        timer_label.config(text='Break', bg=YELLOW, fg=RED, font=(FONT_NAME, 28))
        count_down(long_break_sec)
    else:
        timer_label.config(text='Work', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28))
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count/60)
    seconds = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        num_checks = math.floor(reps/2)
        for i in range(num_checks):
            mark += '✔'
            check_mark_label.config(text=mark)

    return count


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=10, bg=YELLOW )
window.geometry("350x350")

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28))
#timer_label.pack()
timer_label.grid(column=1, row=0)
#timer_label.place(x=40, y=0)
canvas = Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)
check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
check_mark_label.grid(column=1, row=3)

button_start = Button(text="Start", bg="white", highlightthickness=0, command=start_timer )
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer, state=DISABLED)
button_reset.grid(column=2, row=2)

window.mainloop()
