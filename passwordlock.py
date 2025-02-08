from tkinter import Tk, Frame, Button, StringVar, Label
import serial

# Replace 'COM3' with the correct port your Arduino is connected to
ARDUINO_PORT = 'COM4'  # Update this to the correct COM port
BAUD_RATE = 9600
INITIAL_PASSWORD = "1234"
CORRECT_PASSWORD = INITIAL_PASSWORD

class KeypadGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Lock")
        
        self.password_var = StringVar()
        self.new_password_mode = False
        self.initial_password_unlocked = False
        self.arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
        self.create_widgets()
        
    def create_widgets(self):
        self.display = Label(self.master, textvariable=self.password_var, font=("Helvetica", 24))
        self.display.grid(row=0, column=0, columnspan=3)
        
        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('*', 4, 0), ('0', 4, 1), ('#', 4, 2),
        ]
        
        for (text, row, col) in buttons:
            Button(self.master, text=text, command=lambda t=text: self.on_button_click(t), width=5, height=2).grid(row=row, column=col)
        
    def on_button_click(self, char):
        current_password = self.password_var.get()
        if len(current_password) < 4 or char in ['*', '#']:
            new_password = current_password + char
            self.password_var.set(new_password)
        
        if char == '#':
            if self.initial_password_unlocked:
                self.set_new_password(new_password)
        elif char == '*':
            self.check_password(new_password)
    
    def set_new_password(self, password):
        global CORRECT_PASSWORD
        CORRECT_PASSWORD = password[:-1]  # Remove the '#' character
        self.password_var.set("")
        self.new_password_mode = False
        print("New password set!")
    
    def check_password(self, password):
        global CORRECT_PASSWORD
        if password[:-1] == CORRECT_PASSWORD:  # Remove the '*' character
            self.unlock_door()
            self.password_var.set("")  # Clear the display after unlocking
            if CORRECT_PASSWORD == INITIAL_PASSWORD:
                self.initial_password_unlocked = True
                print("Initial password unlocked! You can now set a new password.")
        else:
            self.password_var.set("")
            print("Incorrect password!")

    def unlock_door(self):
 
        if self.arduino:
            self.arduino.write(b'1')
            print("Door unlocked!")

def main():
    root = Tk()
    app = KeypadGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()