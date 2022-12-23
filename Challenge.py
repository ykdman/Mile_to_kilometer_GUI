from tkinter import *

window = Tk()
window.title("Challenge")  # 화면 제목 정의
window.minsize(width=500, height=300)  # 화면 크기 정의
window.config(padx=100, pady=200)  # 여백 추가

# Label (0,0)
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button (1,1)
button = Button(text="Button")
button.grid(column=1, row=1)

# New Button (2,0)
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry (3,2)
entry = Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()