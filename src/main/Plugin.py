import importlib
from abc import ABC, abstractmethod


class AbstractPlugin(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def show_ui(self, parent):
        pass

    @abstractmethod
    def handle_entry(self, entry):
        pass

    @abstractmethod
    def handle_comment(self, comment):
        pass


def name_to_instance(l):
    longname = l.strip()
    dot_index = longname.rfind(".")
    package = longname[:dot_index]
    name = longname[dot_index + 1:]
    print(package)
    print(name)
    # Standard import

    # Load "module.submodule.MyClass"
    module = importlib.import_module(package)
    MyClass = getattr(module, name)
    # Instantiate the class (pass arguments to the constructor, if needed)
    instance = MyClass()
    return instance

def get_plugins(file):
    fp = open(file)
    lines = fp.readlines()
    fp.close()

    return list(map(name_to_instance, lines))

