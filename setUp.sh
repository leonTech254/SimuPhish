#!/bin/bash

# Function to activate virtual environment
activate_virtualenv() {
    if [ "$(uname)" == "Darwin" ]; then
        activate_script="$1/bin/activate"
    elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
        activate_script="$1/bin/activate"
    elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
        activate_script="$1/Scripts/activate"
    elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
        activate_script="$1/Scripts/activate"
    fi

    source "$activate_script"
}

# Output function
output() {
    echo -e "\e[91m$1\e[0m"  # Use ANSI color codes for red text
}

# Check virtual environment
output "Checking virtual environment"
foldername=".venv"

# Create virtual environment if it doesn't exist
if [ ! -d "$foldername" ]; then
    python3 -m venv "$foldername"
fi

# Activate virtual environment
activate_virtualenv "$foldername"

# Check operating system
system_platform=$(uname)
if [ "$system_platform" == "Linux" ]; then
    activate_command="source $foldername/bin/activate"
else
    activate_command="\"$foldername/Scripts/activate\""
fi

source "$activate_command"

# Install modules
packageRequirements=('flask' 'flask_cors' 'flask_Alchemy' 'tabulate')

for package in "${packageRequirements[@]}"; do
    pip install "$package"
done

# Clear the terminal
clear

python run.py
