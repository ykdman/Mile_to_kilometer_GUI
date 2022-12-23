from tkinter import *

def mile_to_kilometer():
    mile = float(entry.get())
    # convert
    km = round(mile * 1.609)
    km_output_label.config(text=f"{km}")

# Set Window Display
window = Tk()
window.title("Miles To Kilometer Converter")
window.config(padx=20, pady=20)


# Entry (1,1)
entry = Entry()
entry.grid(column=1, row=0)


# Miles Label (2,0)
mile_label = Label(text="Miles", font=("Arial", 12, "bold"))
mile_label.grid(column=2, row=0)

# is equal to Label (0,1)
equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

# KM output Label (1,1)
km_output_label = Label(text=0, font=("Arial", 12, "bold"))
km_output_label.grid(column=1, row=1)

# Km Label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

# Calculate Button (1,2)
calculate_button = Button(text="Calculate", font=("Arial", 12, "bold"), command=mile_to_kilometer)
calculate_button.grid(column=1, row=2)
























window.mainloop()