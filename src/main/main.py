from tkinter import *
from tkinter.ttk import Combobox

from Plugin import get_plugins
from lj import download


def run_plugin():
    plugin = next(x for x in plugins if x.get_name() == plugin_box.get())
    user = username_field.get()
    plugin.show_ui(master)
    download(user, plugin)

plugins = get_plugins("./resources/plugins.txt")
plugins_names = list(map(lambda p: p.get_name(), plugins))

master = Tk()
Label(master, text="Journal Name:").grid(row=0)
Label(master, text="Output plugin:").grid(row=1)

username_field = Entry(master)
plugin_box = Combobox(master, state="readonly")
plugin_box['values'] = plugins_names
plugin_box.current(0)

username_field.grid(row=0, column=1)
plugin_box.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Export', command=run_plugin).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
