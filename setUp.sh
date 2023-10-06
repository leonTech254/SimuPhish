#!/bin/bash

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

output() {
    echo -e "\e[91m$1\e[0m"  
}

output "Checking virtual environment"
foldername=".venv"

if [ ! -d "$foldername" ]; then
    python3 -m venv "$foldername"
fi

activate_virtualenv "$foldername"

system_platform=$(uname)
if [ "$system_platform" == "Linux" ]; then
    activate_command="source $foldername/bin/activate"
else
    activate_command="\"$foldername/Scripts/activate\""
fi

source "$activate_command"

packageRequirements=('flask' 'flask_cors' 'Flask-SQLAlchemy' 'tabulate')

for package in "${packageRequirements[@]}"; do
    pip install "$package"
done

clear

python run.py
