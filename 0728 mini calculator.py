import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "錯誤")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

window = tk.Tk()
window.title("簡易計算機")
window.geometry("300x400")

entry = tk.Entry(window, font=("Arial", 24), justify="right", bd=10, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row = 1
col = 0
for button in buttons:
    action = lambda x=button: on_click(x)
    b = tk.Button(window, text=button, width=5, height=2, font=("Arial", 18), command=action)
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()