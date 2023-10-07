#!/bin/bash

activate_virtualenv() {
    local activate_script

    case "$(uname)" in
        Darwin|Linux)
            activate_script="$1/bin/activate"
            ;;
        MINGW32_NT|MINGW64_NT)
            activate_script="$1/Scripts/activate"
            ;;
        *)
            echo "Unsupported platform: $(uname)"
            exit 1
            ;;
    esac

    source "$activate_script"
}

output() {
    echo -e "\e[91m$1\e[0m"  
}

output "Checking if Python is installed"
if ! command -v python3 &> /dev/null; then
    output "Python 3 is required but not installed. Exiting."
    exit 1
fi

output "Checking virtual environment"
foldername=".venv"

if [ ! -d "$foldername" ]; then
    python3 -m venv "$foldername"
fi

activate_virtualenv "$foldername"

packageRequirements=('flask' 'flask_cors' 'Flask-SQLAlchemy' 'tabulate')

for package in "${packageRequirements[@]}"; do
    pip install "$package"
done

clear

python3 -c "$(cat <<EOF
$(<run.py)
EOF
)"

if [ $? -eq 0 ]; then 
    echo "All set successfully Runing the server"
    python3 -c "$(cat <<EOF
$(<app.py)
EOF
)"
else
    echo "failed"
fi
