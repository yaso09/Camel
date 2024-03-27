# Install dependencies
python -m pip install pyinstaller requests json
# Build Python script
pyinstaller -F main.py
# Move build to bin
mv dist/main dist/camel
mv dist/camel $HOME/bin
# Delete other files
rm -rf build
rm -rf dist
rm -rf main.spec
# Save aliases
alias cml=$HOME/bin/camel
alias camel=$HOME/bin/camel

