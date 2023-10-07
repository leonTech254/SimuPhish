#!/bin/bash

activate_virtualenv() {
    local activate_script

    case "$(uname)" in
        Darwin|Linux)
            checkuser
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

checkuser() {
    user=$(whoami)
    if [ "$user" != 'root' ]; then 
        echo "The script needs to be run as root"
        exit 1
    fi
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

checkPortAndTerminate() {
    target_port=8080

    pid=$(sudo lsof -t -i:$target_port)

    if [ -n "$pid" ]; then
        echo "Process using port $target_port found (PID: $pid). Terminating..."
        sudo kill -9 $pid
        echo "Process terminated."
    else
        echo "No process found using port $target_port."
    fi
}

if [ $? -eq 0 ]; then 
    checkPortAndTerminate
    echo "All set successfully. Running the server"
    # running my flask application script
    python3 app.py > /dev/null 2>&1 &
else
    echo "Failed"
fi

echo "Python Flask running"
