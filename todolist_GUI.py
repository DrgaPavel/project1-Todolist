import tkinter as tk

def pridej():
    seznam.insert("end", entry.get())
    entry.delete(0, "end")

def smaz():
    seznam.delete("anchor")

def uprav():
    index = seznam.index("anchor")
    seznam.delete("anchor")
    seznam.insert(index, entry.get())

okno = tk.Tk()
okno.title("ToDoList")
okno.geometry("200x400")

label = tk.Label(okno, text="ToDoList", font=("Arial", 14))
label.pack(pady=5)

entry = tk.Entry(okno)
entry.pack()

# Tlačítka hned pod sebou
tk.Button(okno, text="Přidat úkol", command=pridej).pack()
tk.Button(okno, text="Smazat úkol", command=smaz).pack()
tk.Button(okno, text="Upravit úkol", command=uprav).pack()

seznam = tk.Listbox(okno)
seznam.pack()

okno.mainloop()




