import tkinter as tk
from tkinter import messagebox

def validate_cpf():
    try:
        text = entry.get()

        if not text.isdigit():
            raise ValueError("CPF must contain only numbers")

        cpf = list(text)
        final = len(cpf) - 2

        # ---------- 1st digit ----------
        n = 10
        sum1 = 0
        for i in cpf[0:final]:
            result = int(i) * n
            sum1 += result
            n -= 1
        remainder1 = sum1 % 11
        if remainder1 == 0 or remainder1 == 1:
            d1 = 0
        else:
            d1 = 11 - remainder1

        # ---------- 2nd digit ----------
        n = 11
        sum2 = 0
        for i in cpf[0:final] + [str(d1)]:
            result = int(i) * n
            sum2 += result
            n -= 1
        remainder2 = sum2 % 11
        if remainder2 == 0 or remainder2 == 1:
            d2 = 0
        else:
            d2 = 11 - remainder2

        # ---------- Verification ----------
        if int(cpf[9]) == d1 and int(cpf[10]) == d2:
            messagebox.showinfo("Result", "This CPF is true")
        else:
            messagebox.showwarning("Result", "This CPF is false")

    except ValueError as e:
        messagebox.showerror("Error", f"Incorrect: {e}")

## ---------- GUI ----------
root = tk.Tk()
root.title("CPF Validator")
root.geometry("420x250")
root.resizable(False, False)
root.configure(bg="#2e2e2e")  # cinza escuro

# ---------- Widgets ----------
label = tk.Label(root, text="Enter CPF (numbers only):",
                 font=("Ubuntu", 13, "bold"),
                 bg="#2e2e2e", fg="#ffaa00")
label.pack(pady=15)

entry = tk.Entry(root, font=("Ubuntu", 14), justify="center",
                 bg="#4d4d4d", fg="#ffffff", bd=2, relief="groove")
entry.pack(pady=10, ipady=5, ipadx=5)

canvas = tk.Canvas(root, width=150, height=50, bg="#2e2e2e", highlightthickness=0)
canvas.pack(pady=20)

def on_click(event):
    validate_cpf()

def create_rounded_rect(x1, y1, x2, y2, r=20, **kwargs):
    points = [x1+r, y1,
              x1+r, y1,
              x2-r, y1,
              x2-r, y1,
              x2, y1,
              x2, y1+r,
              x2, y1+r,
              x2, y2-r,
              x2, y2-r,
              x2, y2,
              x2-r, y2,
              x2-r, y2,
              x1+r, y2,
              x1+r, y2,
              x1, y2,
              x1, y2-r,
              x1, y2-r,
              x1, y1+r,
              x1, y1+r,
              x1, y1]
    return canvas.create_polygon(points, smooth=True, **kwargs)

button_bg = create_rounded_rect(0, 0, 150, 50, r=20, fill="#1a1a1a")
button_text = canvas.create_text(75, 25, text="Validate", fill="#ffaa00",
                                 font=("Ubuntu", 12, "bold"))

canvas.tag_bind(button_bg, "<Button-1>", on_click)
canvas.tag_bind(button_text, "<Button-1>", on_click)

root.mainloop()