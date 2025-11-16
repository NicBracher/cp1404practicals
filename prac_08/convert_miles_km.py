"""
CP1404 Practical 8 - Kivy GUI Application - Nicholas Bracher
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy App for converting miles to kilometres."""

    def build(self):
        """Build the app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """Handle calculation and result output."""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle increment change, update input and output."""
        current_value = self.get_validated_miles()
        new_value = current_value + change
        self.root.ids.input_miles.text = str(new_value)
        self.handle_calculation()

    def get_validated_miles(self):
        """Validate and return miles input as float."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

ConvertMilesToKmApp().run()
