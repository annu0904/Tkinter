from tkinter import *
root = Tk()
root.title("ScrollBar")
root.geometry("444x444")
#for connecting a scrollbar to a widget
#1) widget (yscrollcommand = scrollbar.set)
#2.) scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

# listbox = Listbox(root, yscrollcommand = scrollbar.set)
# for i in range (344):
#     listbox.insert(END, f"Item{i}")
#
# listbox.pack(fill="both", padx=22 )

# We can use scrollbar by using text widget as well

text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill = BOTH)
# scrollbar.config(command= listbox .yview)
scrollbar.config(command= text .yview)
root.mainloop()