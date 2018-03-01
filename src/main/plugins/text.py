from Plugin import AbstractPlugin


class TextPlugin(AbstractPlugin):

    def get_name(self):
        return "Text"

    def show_ui(self, parent):
        pass

    def handle_entry(self, entry):
        print(f"Got entry:{entry}")
