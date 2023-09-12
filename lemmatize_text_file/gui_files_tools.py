from tkinter import filedialog, messagebox, Tk, Button


def select_file_via_gui():
    root = Tk()
    root.withdraw()

    choose_file = filedialog.askopenfile(initialdir="/Users/evgeniy/Downloads", title="Select file")

    if choose_file:
        return choose_file.name
    else:
        messagebox.showwarning("Warning", "You haven't chosen a file. Program terminated.")

    root.destroy()


def save_data_to_txt_file(keywords: list, my_function):
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfile(mode='w',
                                         defaultextension='.txt',
                                         initialdir="/Users/evgeniy/Documents/keywords").name
    if file_path:
        # save data to file
        my_function(keywords, file_path)  # function to save data from list

    button = Button(text='Save', command=save_data_to_txt_file)
    button.pack()



