from tkinter import *


def miles_to_km():
    #nb_kilometers = round(float(miles_input.get()) * 1.609)
    nb_kilometers = float(miles_input.get()) * 1.609
    # label_3.config(text=f"{input.get()}")
    kilometer_result_label.config(text=f"{nb_kilometers}")


window = Tk()
window.title("Miles to km converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

nb_kilometers = 0

miles_input = Entry(width=10)
#input.pack()
#print(input.get())
miles_input.grid(column=1, row=0)
miles_input.insert(END, string=f"{nb_kilometers}")

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=0, row=1)
kilometer_result_label = Label(text=f"{nb_kilometers}", font=("Arial", 12))
kilometer_result_label.grid(column=1, row=1)
kilometer_label = Label(text="Km", font=("Arial", 12))
kilometer_label.grid(column=2, row=1)



calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)



window.mainloop()