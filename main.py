import tkinter as tk
import pygame
import logging

logging.basicConfig(level=logging.INFO)

BUTTON_LABELS_INFO = {0: "Y", 1: "B", 2: "A", 3: "X", 4: "L1", 5: "R1", 6: "L2", 7: "R2", 9: "START", 8: "SELECT", 12: "HOME", 10: "LEFT", 11: "RIGHT"}

class GameControllerTester(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("USB Game Controller")
        self.geometry("400x600")   
        self.init_joysticks()

    def init_joysticks(self):
        pygame.init()
        pygame.joystick.init()
        num_joysticks = pygame.joystick.get_count()
        if num_joysticks == 0:
            logging.error("No joystick found. Exiting...")
            self.destroy()
            return

        logging.info(f"Found {num_joysticks} joystick(s)")

        for j in range(num_joysticks):
            self.create_controller_section(j)

    def create_controller_section(self, joystick_index):
        frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=2)
        frame.grid(row=0, column=joystick_index, padx=10, pady=10, sticky="nsew")
        joystick = pygame.joystick.Joystick(joystick_index)
        joystick.init()

        button_labels = []
        for i in range(joystick.get_numbuttons()):
            label_text = f"Button {i}: {BUTTON_LABELS_INFO.get(i, '')}"
            label = tk.Label(frame, text=label_text, font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            button_labels.append(label)

        axis_labels = []
        for i in range(joystick.get_numaxes()):
            label_text = f"Axis {i}:"
            label = tk.Label(frame, text=label_text, font=("Arial", 12))
            label.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            axis_labels.append(label)

        button_actions = {
            "R1": self.execute_action_r1,
            "R2": self.execute_action_r2,
            "L1": self.execute_action_l1,
            "L2": self.execute_action_l2,
            "START": self.execute_action_start
        }

        self.update_states(joystick, button_labels, axis_labels, button_actions)

    def update_states(self, joystick, button_labels, axis_labels, button_actions):
        pygame.event.pump()
        button_states = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]

        for i, state in enumerate(button_states):
            label_text = f"Button {i}: {BUTTON_LABELS_INFO.get(i, '')} - {state}"
            button_labels[i].config(text=label_text, font=("Arial", 12), fg="blue" if state else "black")
            button_name = BUTTON_LABELS_INFO.get(i, '')
            if button_name in button_actions and state == 1:
                button_actions[button_name]()

        axis_positions = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]

        for i, position in enumerate(axis_positions):
            axis_labels[i].config(text=f"Axis {i}: {position:.2f}", font=("Arial", 12), fg="red" if position else "black")

        self.after(100, self.update_states, joystick, button_labels, axis_labels, button_actions)

    def execute_action_r1(self):
        print("R1 button pressed. Executing action...")  

    def execute_action_r2(self):
        print("R2 button pressed. Executing action...")  

    def execute_action_l1(self):
        print("L1 button pressed. Executing action...")  

    def execute_action_l2(self):
        print("L2 button pressed. Executing action...")  

    def execute_action_start(self):
        print("START button pressed. Executing action...")  

if __name__ == "__main__":
    app = GameControllerTester()
    app.mainloop()
