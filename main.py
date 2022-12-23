import tkinter


def button_clicked():
    print("i got clicked")
    my_label.config(text="Button Got Clicked")


window = tkinter.Tk()
window.title("My First GUI Program")  # 화면 제목 정의
window.minsize(width=500, height=300)  # 화면 크기 정의

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button
button = tkinter.Button(text="Click me", command=button_clicked)  # 버튼이 눌렸을때 하는 동작을 command로 명령할수 있다.
button.grid(column=1, row=1)


# Entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=2, row=2)  # grid 와 pack 은 같은 코드 내에서 쓸 수 없다.

# Tkinter 윈도우가 계속 실행되게 하는 명령
window.mainloop()