import tkinter as tk
from tkinter import messagebox
import random

def calculate_variable_compound_interest():
    try:
        P = float(entry_principal.get())
        base_rate = float(entry_rate.get()) / 100
        risk_factor = float(entry_risk.get()) / 100
        t = float(entry_years.get())
        n = int(entry_frequency.get())

        total_periods = int(n * t)
        current_value = P
        history = []

        for _ in range(total_periods):
            random_risk = random.uniform(-risk_factor, risk_factor)
            actual_rate = base_rate + random_risk
            current_value *= (1 + actual_rate / n)
            history.append(current_value)

        result_label.config(text=f"最終金額：{current_value:,.2f} 元\n（共 {total_periods} 期隨機波動）")
    except ValueError:
        messagebox.showerror("輸入錯誤", "請輸入正確的數值！")

window = tk.Tk()
window.title("隨機風險複利計算機")
window.geometry("320x370")

tk.Label(window, text="本金 (元)：").pack()
entry_principal = tk.Entry(window)
entry_principal.pack()

tk.Label(window, text="平均年利率 (%)：").pack()
entry_rate = tk.Entry(window)
entry_rate.pack()

tk.Label(window, text="風險波動範圍 (%)：").pack()
entry_risk = tk.Entry(window)
entry_risk.pack()

tk.Label(window, text="投資年數：").pack()
entry_years = tk.Entry(window)
entry_years.pack()

tk.Label(window, text="每年複利次數：").pack()
entry_frequency = tk.Entry(window)
entry_frequency.pack()

tk.Button(window, text="計算", command=calculate_variable_compound_interest).pack(pady=10)

result_label = tk.Label(window, text="最終金額：")
result_label.pack()

window.mainloop()