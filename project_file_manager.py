
import os


def create_web_file_system():
    basedir = "/Users/hadiya/web-proj-test/"
    folder = input("please enter the name for the website folder: ")
    path = basedir + folder
    print(path)
    # sub_dirs = "/styles/scripts/images"
    # full_path = path + sub_dirs
    # print(full_path)

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)
    #check that folder was created

    print(os.path.isdir(path))

    nested_base_dir = path
    print(nested_base_dir)

    scripts_folder = nested_base_dir + "/scripts"
    try:
        os.mkdir(scripts_folder)
    except OSError:
        print("Creation of the directory %s failed" % scripts_folder)
    else:
        print("Successfully created the directory %s" % scripts_folder)

    #create an empty javascript file
    with open(os.path.join(scripts_folder, 'script.js'), 'w') as f:
        pass

    images_folder = nested_base_dir + "/images"
    try:
        os.mkdir(images_folder)
    except OSError:
        print("Creation of the directory %s failed" % images_folder)
    else:
        print("Successfully created the directory %s" % images_folder)

    styles_folder = nested_base_dir + "/styles"
    try:
        os.mkdir(styles_folder)
    except OSError:
        print("Creation of the directory %s failed" % styles_folder)
    else:
        print("Successfully created the directory %s" % styles_folder)

    #create an empty  style.css file
    with open(os.path.join(styles_folder, 'style.css'), 'w') as f:
        pass


def create_flask_system():
    basedir = "/Users/hadiya/flask-test/"
    folder = input("Please enter the name of your flask project: ")
    path = basedir + folder

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s has failed." % path)
    else:
        print("Successfully created the directory %s" % path)

    templates_folder = path + "/templates"
    try: os.mkdir(templates_folder)
    except OSError:
        print("Creation of the directory %s has failed." % templates_folder)
    else:
        print("Successfully created the directory %s" % templates_folder)

    with open(os.path.join(templates_folder, 'index.html'), 'w') as f:
        pass
    with open(os.path.join(templates_folder, 'layout.html'), 'w') as f:
        pass

    static_folder = path + "/static"
    try:
        os.mkdir(static_folder)
    except OSError:
        print("Creation of the directory %s has failed." % static_folder)
    else:
        print("Successfully created the directory %s" % static_folder)
    with open(os.path.join(static_folder, 'main.css'), 'w') as f:
        pass


def create_python_project():
    basedir = "/Users/hadiya/Desktop/python_scripts/"
    folder = input("Please enter the name of the python project you'll be creating: ")
    path = basedir + folder

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s has failed." % path)
    else:
        print("Successfully created the directory %s" % path)

    with open(os.path.join(path, 'py.py'), 'w') as f:
        pass


# create_web_file_system()
# create_flask_system()
# create_python_project()




