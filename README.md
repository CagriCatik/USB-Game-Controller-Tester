# USB Game Controller Tester

This Python script creates a graphical user interface using Tkinter to test USB game controllers. It allows users to view the states of buttons and axes on connected game controllers and execute custom actions based on button presses.

## Installation

Install Tkinter and Pygame using pip:

```bash
pip install tk pygame
```

## Usage

1. Connect your USB game controller to your computer.
2. Run the script by executing the following command:
   ```bash
   python main.py
   ```
3. The graphical user interface will display information about the connected game controllers.
4. Press buttons on the controller to see their states and execute custom actions based on button presses.

## Functionality

- The script initializes Pygame to interact with game controllers.
- It creates a Tkinter window with sections for each connected game controller.
- Each section displays the states of buttons and axes on the controller.
- Button states are updated in real-time, and custom actions can be executed based on button presses.

## Customization

- You can customize the script by adding more actions for specific buttons in the `execute_action_` methods.
- Modify the `BUTTON_LABELS_INFO` dictionary to assign labels to different buttons on your controller.

## Troubleshooting

- If no joystick is found, an error message will be displayed, and the script will exit.
