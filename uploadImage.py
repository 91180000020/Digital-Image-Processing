try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
    import tkinter.filedialog as tkfd
except ImportError:
    import Tkinter as tk
    import tkFileDialog as tkfd


if __name__ == '__main__':
    root = tk.Tk()
    entry = tk.Entry(root)
    entry.pack()
    path = tkfd.askopenfilename(initialdir = "/", title = "Select file",
                    filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    entry.insert('0', path)
    root.mainloop()