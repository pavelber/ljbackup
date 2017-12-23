from tkinter import *

from Plugin import AbstractPlugin


class MySQLPlugin(AbstractPlugin):

    def get_name(self):
        return "MySQL"

    def show_ui(self, parent):
        self.dlg = Toplevel()
        Label(self.dlg, text="Host:").grid(row=0)
        Label(self.dlg, text="DB:").grid(row=1)
        Label(self.dlg, text="User:").grid(row=2)
        Label(self.dlg, text="Password:").grid(row=3)

        self.host_field = Entry(self.dlg)
        self.db_field = Entry(self.dlg)
        self.user_field = Entry(self.dlg)
        self.password_field = Entry(self.dlg)

        self.host_field.grid(row=0, column=1)
        self.db_field.grid(row=1, column=1)
        self.user_field.grid(row=2, column=1)
        self.password_field.grid(row=3, column=1)
        Button(self.dlg, text='Start', command=self.connect).grid(row=4, column=0, sticky=W, pady=4)
        ## Set the focus on dialog window (needed on Windows)
        self.dlg.focus_set()
        ## Make sure events only go to our dialog
        self.dlg.grab_set()
        ## Make sure dialog stays on top of its parent window (if needed)
        self.dlg.transient(parent)
        ## Display the window and wait for it to close
        self.dlg.wait_window(self.dlg)

    def handle_entry(self, entry):
        pass

    def handle_comment(self, comment):
        pass

    def connect(self):
        print(f"connecting to {self.host_field.get()}/{self.db_field.get()} as {self.user_field.get()}:{self.password_field.get()}")
        self.dlg.destroy()
