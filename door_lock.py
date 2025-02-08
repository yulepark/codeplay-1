import tkinter as tk
from tkinter import messagebox

class DoorLockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("도어 잠금 시스템")
        self.password = "1234"
        self.entered_password = ""
        self.is_unlocked = False

        self.info_label = tk.Label(root, text="기본 4자리 비밀번호 (1234)를 입력하고 '#'을 눌러 잠금을 해제하세요.")
        self.info_label.pack(pady=10)

        self.create_keypad()

    def create_keypad(self):
        self.keypad_frame = tk.Frame(self.root)
        self.keypad_frame.pack(pady=10)

        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '*', '0', '#'
        ]

        row_val = 0
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.keypad_click(x)
            tk.Button(self.keypad_frame, text=button, width=5, height=2, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

    def keypad_click(self, value):
        if value == '#':
            if not self.is_unlocked:
                self.check_default_password()
            else:
                self.check_password()
        elif value == '*':
            if self.is_unlocked:
                self.set_password()
            else:
                self.entered_password = ""
        else:
            self.entered_password += value

    def check_default_password(self):
        if self.entered_password.endswith(self.password):
            self.is_unlocked = True
            self.entered_password = ""
            self.info_label.config(text="새로운 비밀번호를 설정하려면 '*'을 누르세요.")
            messagebox.showinfo("성공", "문이 열렸습니다!")
        else:
            messagebox.showerror("오류", "기본 비밀번호가 틀렸습니다. 문이 잠긴 상태로 유지됩니다.")
        self.entered_password = ""

    def set_password(self):
        if self.entered_password.isdigit():
            self.password = self.entered_password
            self.entered_password = ""
            self.info_label.config(text="비밀번호가 설정되었습니다. 비밀번호를 입력하고 '#'을 눌러 잠금을 해제하세요.")
            messagebox.showinfo("성공", "비밀번호가 성공적으로 설정되었습니다!")
        else:
            messagebox.showerror("오류", "비밀번호는 숫자여야 합니다.")
            self.entered_password = ""

    def check_password(self):
        if self.password is None:
            self.set_password()
        elif self.entered_password.endswith(self.password):
            messagebox.showinfo("성공", "문이 열렸습니다!")
        else:
            messagebox.showerror("오류", "비밀번호가 틀렸습니다. 문이 잠긴 상태로 유지됩니다.")
        self.entered_password = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = DoorLockApp(root)
    root.mainloop()