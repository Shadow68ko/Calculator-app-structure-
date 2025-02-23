from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
            ['=', '=']
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)
        
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        elif button_text == '=':
            try:
                self.result.text = str(eval(self.result.text))
            except Exception:
                self.result.text = 'Error'
        else:
            self.result.text += button_text

if __name__ == '__main__':
    CalculatorApp().run()
import kiwi
import kiwi.ui as ui

class CalculatorApp(kiwi.App):
    def build(self):
        window = ui.Window(title="Calculator", size=(400, 600))

        # Load the image
        logo = ui.Image(source="assets/calculator.png")  # Make sure the path matches where you put the image

        # Create a layout and add the image to it
        layout = ui.VerticalBox(spacing=10)
        layout.add(logo)

        # Add other UI elements of the calculator below
        # Example: Adding a button
        button = ui.Button(text="1")
        layout.add(button)

        # Set the layout for the window
        window.add(layout)
        
        return window

if __name__ == "__main__":
    CalculatorApp().run()

