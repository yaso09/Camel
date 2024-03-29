# Imports

import os, sys, json, uuid
from requests import get as g
from requests import post as p

# Print information text

print("""
Camel - Script Manager 1.0.0
Type `-h` or `help` for more information
""")

# Set configuration

global cfg

fpath = os.path.join(os.path.expanduser("~"), "bin", "camel_config.json")
if os.path.exists(fpath):
    f = open(fpath, "r")
    try:
        j = json.load(f)
        repo = j["repository"]
    except: repo = "yaso09/camel"
else:
    f = open(fpath, "w")
    c = {
        "repository": "yaso09/camel"
    }
    json.dump(c, f)
    repo = c["repository"]

# Get parameter

if not len(sys.argv) > 1: os._exit(0)

param = sys.argv[1]

# Define run command

if param == "run" or param == "-r":
    try:
        nm = sys.argv[2]
        res = g(
            f"https://raw.githubusercontent.com/{repo}/scripts/{nm}.cml"
        )
        
        if res:
            nm = uuid.uuid4().hex
            f = open(f"script_{nm}.json", "w")
            json.dump(res.text, f) and f.close()
            a = open(f"script_{nm}.json", "r")
            script = json.load(a)
            f = open(f"{script['name']}.{script['file_format']}", "w")
            f.writelines(script["codes"])
            commands = script["commands"]
            for command in commands:
                os.system("commands")
        else: print("Script not found")
    except IndexError: print("Please enter script name")

# Define list command

elif param == "list" or param == "-l":
    url = f"https://api.github.com/repos/{repo}/contents/scripts"
    res = g(url)
    files = res.json()
    print("Script Name")
    for file in files:
        print(str(file["name"].split(".cml")[0]))

# Define build command

elif param == "build" or param == "-b":
    commands = []
    file = input("Script file (please use formats like `main.py`) (script.sh): ")
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
    for code in codes:
        if "\n" in code:
            codes[codes.index(code)] = codes[codes.index(code)].split("\n")[0]
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
        json.dump(build, f)
        f.close()
        print(f"Your script packaged to `{name}.cml`")

# Define save command

elif param == "save" or param == "-s":
    try:
        nm = sys.argv[2]
        try: os.system(f'alias {sys.argv[3]}="$HOME/bin/camel run {nm}"')
        except IndexError: os.system(f'alias {nm}="$HOME/bin/camel run {nm}"')
    except IndexError: print("Please enter script name")

# Define test command

elif param == "test" or param == "-t":
    try:
        nm = uuid.uuid4().hex
        try:
            os.system(f"cp {sys.argv[2]}.cml {sys.argv[2]}.json")
            a = open(f"{sys.argv[2]}.json", "r")
            script = json.load(a)
            f = open(f"{script['name']}.{script['file_format']}", "w")
            f.writelines(script["codes"]) and f.close()
            commands = script["commands"]
            for command in commands:
                os.system(str(command))
            os.remove(f"{sys.argv[2]}.json")
            os.remove(f"{script['name']}.{script['file_format']}")
        except FileNotFoundError: print("Script not found")
        except json.JSONDecodeError:
            print("Can't decode script")
            os.remove(f"{sys.argv[2]}.json")
    except IndexError: print("Please enter script name")

# Define config command

elif param == "config" or param == "-c":
    print(f"""
CONFIGURE CAMEL

Repository: https://github.com/{repo}
""")
    ok = input("Do you want to change repository? (no): ")
    if not ok: ok = "no"
    if not ok == "no":
        new_repo = input("Enter Github repository (user/repo): ")
        f = open(fpath, "w")
        c = {
            "repository": new_repo
        }
        json.dump(c, f)

# Define update command

elif param == "update" or param == "-u":
    b = g("https://raw.githuusercontent.com/yaso09/camel/main/build.sh")
    cml = g("https://raw.githuusercontent.com/yaso09/camel/main/main.py")
    r = os.getcwd() and os.system("cd $HOME")
    os.mkdir("tmp") and os.system("cd tmp")
    f = open("main.py", "w") and f.write(cml.text) and f.close()
    os.system(b.text) and os.remove("main.py") and os.system(f"cd {r}")

# Define help command

elif param == "help" or param == "-h":
    print(f"""
COMMAND\t\tUSAGE

build  (-b)\tBuild script to Camel package
config (-c)\tConfigure Github repository
help   (-h)\tGet help
list   (-l)\tList online scripts
run    (-r)\tRun script
save   (-s)\tSave alias of script
test   (-t)\tTest script in local
update (-u)\tUpdate CLI

Repository: https://github.com/{repo}
Source Code: https://github.com/yaso09/Camel
""")

# This monolitic CLI created by Yasir Eymen KAYABAŞI
# You can see every contributors below
# --------------------------------------------------
# Write your name or nick here






