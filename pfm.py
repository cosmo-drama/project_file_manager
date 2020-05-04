from tkinter import *
from tkinter import filedialog, Text, messagebox
import os

# commands / functions

def create_web_fs():
    selected_path = filedialog.askdirectory()
    basedir = selected_path
    print(basedir)

    with open(os.path.join(basedir, 'index.html'), 'w') as f:
        pass
    scripts_folder = basedir + "/scripts"
    try:
        os.mkdir(scripts_folder)
    except OSError:
        print("Creation of the directory %s failed" % scripts_folder)
        # display_dir_label.config(text="Creation of the directory has failed.")
        messagebox.showinfo('failure :(', 'Creation of the directory has failed.')
    else:
        print("Successfully created the directory %s" % scripts_folder)
        # display_dir_label.config(text="successfully created directory under: %s " % basedir )
        messagebox.showinfo('success!', 'successfully created directory under:\n %s'% basedir)

    #create an empty javascript file
    with open(os.path.join(scripts_folder, 'script.js'), 'w') as f:
        pass

    images_folder = basedir + "/images"
    try:
        os.mkdir(images_folder)
    except OSError:
        print("Creation of the directory %s failed" % images_folder)
    else:
        print("Successfully created the directory %s" % images_folder)


    styles_folder = basedir + "/styles"
    try:
        os.mkdir(styles_folder)
    except OSError:
        print("Creation of the directory %s failed" % styles_folder)
    else:
        print("Successfully created the directory %s" % styles_folder)

    #create an empty  style.css file
    with open(os.path.join(styles_folder, 'style.css'), 'w') as f:
        pass

def create_py_fs():
    selected_path = filedialog.askdirectory()
    basedir = selected_path
    print(basedir)

    # try:
    #     os.mkdir(basedir)
    # except OSError:
    #     print("Creation of the directory %s has failed." % basedir)
    #     messagebox.showinfo('failure :(', 'Creation of the directory has failed.')
    # else:
    #     print("Successfully created the directory %s" % basedir)
    #     messagebox.showinfo('success!', 'successfully created directory under:\n %s'% basedir)


    with open(os.path.join(basedir, 'py.py'), 'w') as f:
        pass
    messagebox.showinfo('success!', 'successfully created empty .py file under:\n %s'% basedir)

def create_flask_fs():
    selected_path = filedialog.askdirectory()
    basedir = selected_path
    print(basedir)

    templates_folder = basedir + "/templates"
    try: os.mkdir(templates_folder)
    except OSError:
        print("Creation of the directory %s has failed." % templates_folder)
        messagebox.showinfo('failure :(', 'Creation of the directory has failed.')
    else:
        print("Successfully created the directory %s" % templates_folder)
        messagebox.showinfo('success!', 'successfully created directory under:\n %s'% basedir)
    with open(os.path.join(templates_folder, 'index.html'), 'w') as f:
        pass
    with open(os.path.join(templates_folder, 'layout.html'), 'w') as f:
        pass

    static_folder = basedir + "/static"
    try:
        os.mkdir(static_folder)
    except OSError:
        print("Creation of the directory %s has failed." % static_folder)
    else:
        print("Successfully created the directory %s" % static_folder)
    with open(os.path.join(static_folder, 'main.css'), 'w') as f:
        pass


# create window object
app = Tk()
app.title('project file manager-lite')
app.geometry('600x350')


# widget
# display_dir_text = StringVar()
# display_dir_label = Label(app, text='success or failure', font=('bold', 14))
# display_dir_label.grid(row=0, column=1)


# buttons



website_btn = Button(app, text='website', width=12, command=create_web_fs)
website_btn.grid(row=0, column=1, pady=40)

python_btn = Button(app, text='python-project', width=12, command=create_py_fs)
python_btn.grid(row=1, column=1)

flask_btn = Button(app, text='flask-project', width=12, command=create_flask_fs)
flask_btn.grid(row=2, column=1, pady=40)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

app.mainloop()