import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

class ContactAppUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Set black background and gold foreground colors
        self.bg_color = "#000000"  # black
        self.fg_color = "#FFD700"  # gold
        self.btn_bg_color = "#B8860B"  # dark goldenrod for buttons

        self.root.configure(bg=self.bg_color)

        self.contacts = {}  # Name: (phone, email)
        self.action_history = set()

        # Create buttons for each action with black and gold colors
        btn_add = tk.Button(root, text="Add Contact", command=self.add_contact,
                            bg=self.btn_bg_color, fg=self.bg_color, activebackground=self.fg_color, activeforeground=self.bg_color)
        btn_view = tk.Button(root, text="View All Contacts", command=self.view_contacts,
                             bg=self.btn_bg_color, fg=self.bg_color, activebackground=self.fg_color, activeforeground=self.bg_color)
        btn_search = tk.Button(root, text="Search Contact", command=self.search_contact,
                               bg=self.btn_bg_color, fg=self.bg_color, activebackground=self.fg_color, activeforeground=self.bg_color)
        btn_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact,
                               bg=self.btn_bg_color, fg=self.bg_color, activebackground=self.fg_color, activeforeground=self.bg_color)
        btn_history = tk.Button(root, text="View Action History", command=self.view_history,
                                bg=self.btn_bg_color, fg=self.bg_color, activebackground=self.fg_color, activeforeground=self.bg_color)
        btn_exit = tk.Button(root, text="Exit", command=root.quit,
                             bg=self.btn_bg_color, fg=self.bg_color, activebackground=self.fg_color, activeforeground=self.bg_color)

        btn_add.pack(fill=tk.X)
        btn_view.pack(fill=tk.X)
        btn_search.pack(fill=tk.X)
        btn_delete.pack(fill=tk.X)
        btn_history.pack(fill=tk.X)
        btn_exit.pack(fill=tk.X)

        # Text area to display contacts and history with black background and gold text
        self.text_area = scrolledtext.ScrolledText(root, width=50, height=15,
                                                   bg=self.bg_color, fg=self.fg_color, insertbackground=self.fg_color)
        self.text_area.pack()

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter name:")
        if name:
            name = name.strip()
        else:
            return
        if name in self.contacts:
            messagebox.showinfo("Info", "Contact already exists.")
            return
        phone = simpledialog.askstring("Add Contact", "Enter phone:")
        if phone:
            phone = phone.strip()
        else:
            phone = ""
        email = simpledialog.askstring("Add Contact", "Enter email:")
        if email:
            email = email.strip()
        else:
            email = ""
        self.contacts[name] = (phone, email)
        self.action_history.add("added " + name)
        messagebox.showinfo("Info", f"Contact '{name}' added.")

    def view_contacts(self):
        self.text_area.delete(1.0, tk.END)
        if not self.contacts:
            self.text_area.insert(tk.END, "No contacts found.\n")
            return
        for name, (phone, email) in self.contacts.items():
            self.text_area.insert(tk.END, f"Name: {name}, Phone: {phone}, Email: {email}\n")

    def search_contact(self):
        name = simpledialog.askstring("Search Contact", "Enter name to search:")
        if name:
            name = name.strip()
        else:
            return
        self.text_area.delete(1.0, tk.END)
        if name in self.contacts:
            phone, email = self.contacts[name]
            self.text_area.insert(tk.END, f"Name: {name}, Phone: {phone}, Email: {email}\n")
        else:
            self.text_area.insert(tk.END, "Contact not found.\n")
        self.action_history.add("searched " + name)

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter name to delete:")
        if name:
            name = name.strip()
        else:
            return
        if name in self.contacts:
            del self.contacts[name]
            self.action_history.add("deleted " + name)
            messagebox.showinfo("Info", f"Contact '{name}' deleted.")
        else:
            messagebox.showinfo("Info", "Contact not found.")

    def view_history(self):
        self.text_area.delete(1.0, tk.END)
        if not self.action_history:
            self.text_area.insert(tk.END, "No actions recorded.\n")
            return
        self.text_area.insert(tk.END, "Action History:\n")
        for action in self.action_history:
            self.text_area.insert(tk.END, action + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactAppUI(root)
    root.mainloop()
