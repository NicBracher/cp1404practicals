"""
CP1404 Practical 8 - Kivy GUI Application
Create a very simple app that has a list of names (strings) and dynamically creates a separate Label for each one.

Notice some things in dynamic_widgets demo that will be very similar (but not the same) in yours:

the dictionary is defined in the init function (this is the data, or model)
the widgets (Buttons in the demo, but yours will be Labels) are made with a loop in the build function
Note

Start a new blank Python program for this.
Do not copy the dynamic_widgets example, because it is too different.
Your app won't have any buttons or interactivity.
Use the example as a reference and copy small sections or ideas from it.

Here's a suggested kv file you could use. Notice how simple it is, but it does have a child BoxLayout with an id.

BoxLayout:
    BoxLayout:
        orientation: 'vertical'
        id: main
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app for dynamic label creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            from kivy.uix.label import Label
            dynamic_label = Label(text=name)
            self.root.ids.main.add_widget(dynamic_label)
            colour_value = (1.0, 0.75, 1.0, 1.0) 
            dynamic_label.color = colour_value




DynamicLabelsApp().run()
