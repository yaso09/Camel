import os, sys, json, uuid
from requests import get as g
from requests import post as p

print("""
Camel - Script Manager 1.0.0
Type `-h` or `help` for more information
""")

if not len(sys.argv) > 1: os._exit(0)

param = sys.argv[1]

if param == "run" or param == "-r":
    try:
        nm = sys.argv[2]
        res = g(
            f"https://raw.githubusercontent.com/yaso09/camel/scripts/{nm}.cml"
        )
        
        if res:
            nm = uuid.uuid4().hex
            f = open(f"script_{nm}.json", "w")
            f.write(res.text) and f.close()
            script = json.load(f"script_{nm}.json")
            f = open(f"script_{nm}.{script['file_format']}", "w")
            f.writelines(script["codes"])
            commands = script["commands"]
            for command in commands:
                os.system("commands")
        else: print("Script not found")
    except IndexError: print("Please enter script name")
elif param == "list" or param == "-l":
    url = "https://api.github.com/repos/yaso09/camel/contents/scripts"
    res = g(url)
    files = res.json()
    print("Script Name")
    for file in files:
        print(str(file["name"].split(".cml")[0]))
elif param == "build" or param == "-b":
    commands = []
    file = input("Script file please use formats like `main.py` (script.sh): ")
    name = input(f"Script name ({os.getcwd().split('/')[len(os.getcwd().split('/'))-1]}): ")
    command = input("Command (write `exit` for stop): ")
    while not command == "exit":
        commands.append(command)
        command = input(">> ")
    print("Your script is packaging...")
    if not file: file = "script.sh"
    if not name: name = os.getcwd().split('/')[len(os.getcwd().split('/'))-1]
    if not commands:
        print("Setted default command: `sh script.sh`")
        commands = [ "sh script.sh" ]
    try: f = open(file, "r")
    except FileNotFoundError: print("File not found") and os._exit(1)
    codes = f.readlines()
    while "\n" in codes:
        codes.remove("\n")
    build = {
        "name": name,
        "file_format": file.split(".")[len(file.split(".")) - 1],
        "commands": commands,
        "codes": codes
    }
    print(str(build))
    ok = input("Is this OK? (yes): ")
    if not ok: ok = "yes"
    if not ok == "yes": print("Packaging cancelled")
    else:
        f = open(f"{name}.cml", "w")
        f.write(str(build))
        f.close()
        print(f"Your script packaged to `{name}.cml`")
elif param == "save" or param == "-s":
    try:
        nm = sys.argv[2]
        try: os.system(f'alias {sys.argv[3]}="$HOME/bin/camel run {nm}"')
        except IndexError: os.system(f'alias {nm}="$HOME/bin/camel run {nm}"')
    except IndexError: print("Please enter script name")
elif param == "test" or param == "-t":
    try:
        print(sys.argv[2])
        f = open(f"{sys.argv[2]}.cml")
        print(f.read())
        script = json.loads(f.read())
        f.close()
        f = open(f"script_{nm}.{script['file_format']}", "w")
        f.writelines(script["codes"]) and f.close()
        commands = script["commands"]
        for command in commands:
            os.system("commands")
    except IndexError: print("Please enter script name")
elif param == "help" or param == "-h":
    print("""
COMMAND\t\tUSAGE

build  (-b)\tBuild script to Camel package
help   (-h)\tGet help
list   (-l)\tList online scripts
run    (-r)\tRun script
save   (-s)\tSave alias of script
test   (-t)\tTest script in local

Github: https://github.com/yaso09/Camel
""")

# This monolitic CLI created by Yasir Eymen KAYABAŞI
# You can see every contributors below
# --------------------------------------------------
# Write your name or nick here






