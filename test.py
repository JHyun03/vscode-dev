import tkinter as tk
from tkinter import messagebox

# 버튼 클릭 시 실행될 함수
def on_button_click():
    value = "Hello, World!"  # 출력할 값
    messagebox.showinfo("Output", value)  # 값 출력

# 메인 윈도우 설정
root = tk.Tk()
root.title("Simple App")

# 버튼 설정
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

# 메인 루프 시작
root.mainloop()