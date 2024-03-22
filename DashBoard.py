import os

while True:
    print("Welcome to your dashboard!")
    print("Select tool from menu:")
    print("-> Camera")
    print("-> Chrome")
    print("-> Codeblocks")
    print("-> Firefox")
    print("-> Jupyter Notebook")
    print("-> Mousepad")
    print("-> Notepad")
    print("-> Screenshot")
    print("-> Task Manager")
    print("-> VLC")
    print("-> VirtualBox\n")
    print("System:", end=' ')
    p = input()

    if (("do not" in p) or ("dont" in p) or ("don't" in p)):
        print("OK\n")

    elif (("open" in p) or ("start" in p) or ("run" in p) or ("execute" in p) or ("launch" in p) or ("activate" in p)):

        if (("camera" in p) or ("cheese" in p)):
            os.system("cheese")

        elif ("chrome" in p):
            os.system("google-chrome-stable")

        elif ("codeblocks" in p):
            os.system("codeblocks")

        elif (("firefox" in p) or ("mozilla" in p)):
            os.system("firefox")

        elif (("jupyter" in p) or ("notebook" in p)):
            os.system("jupyter notebook")

        elif ("mousepad" in p):
            os.system("mousepad")
            
        elif ("notepad" in p):
            os.system("notepad")

        elif ("screenshot" in p):
            os.system("xfce4-screenshooter")

        elif ("taskmanager" in p):
            os.system("xfce4-taskmanager")

        elif (("vlc" in p) or ("media player" in p)):
            os.system("vlc")

        elif (("virtualbox" in p) or ("virtual machine" in p) or ("virtual tool" in p)):
            os.system("virtualbox")

        else:
            print("Not supported.")

    elif (("quit" in p) or ("exit" in p) or ("stop" in p) or ("close" in p) or ("deactivate" in p) or ("terminate" in p)):
        print("Goodbye!")
        break

    else:
        print("Not supported.")
