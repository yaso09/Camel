# Camel
> Script manager

## Installation
For Windows use WSL
Need Python 3.10.x
```bash
git clone https://github.com/yaso09/camel.git
cd camel
```
Build code
```bash
sh build.sh
```
Now you can remove clone
```bash
cd ..
rm -rf camel
```

## Example Usage
Create example script
```bash
echo "echo Hello World!">>test.sh
```
Package this script
```bash
camel -b
```
Answer questions
```
Script file (please use formats like `main.py`) (script.sh): test.sh
Script name (your folder name): test
Command (write `exit` to stop): sh test.sh
>> exit
Your script is packaging...
{'name': 'test', 'file_format': 'sh', 'commands': ['sh test.sh'], 'codes': ['echo Hello World!']}
Is this OK? (yes): yes
```
Test script
```bash
camel -t test
```
Script will return `Hello World!`.

## Repository Config
For use another repositories open config page
```bash
camel -c
```
It will returns:
```
CONFIGURE CAMEL

Repository: https://github.com/yaso09/camel

Do you want to change repository? (no): yes
Enter Github repository (user/repo): YOUR GITHUB REPO
```

