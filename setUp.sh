#!/bin/bash
target_port=$(shuf -i 5001-6001 -n 1)
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

packageRequirements=('flask' 'flask_cors' 'Flask-SQLAlchemy' 'tabulate' 'pyngrok')

for package in "${packageRequirements[@]}"; do
    pip install "$package"
done

# clear

# python3 -c "$(cat <<EOF
# $(<run.py)
# EOF
# )"
 python3 -c "$(cat <<EOF
import sys
$(<run.py) 
EOF
)"

checkPortAndTerminate() {
    

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
    python3 -c "$(cat <<EOF
import sys
sys.argv = ["app.py", $target_port]
$(<app.py) 
EOF
)" > output.log 2>&1 &


else
    echo "Failed"
fi

echo "Python server running in the background"

ng="./ng/ngrok.py"


sudo -u "$(logname)" bash <<EOF

# Commands to be executed as the normal user
echo "Now I am a normal user!"
whoami

EOF

# #####################KILL NGROK SESSIONS#####################
killNgrokSessions()
{
    ngrok_pid=$(ps aux | grep ngrok | grep -v grep | awk '{print $2}')

if [ -z "$ngrok_pid" ]; then
  echo "Ngrok process not found."
else
  kill "$ngrok_pid"
  echo "Ngrok process (PID: $ngrok_pid) terminated."
fi
}
killNgrokSessions

# ngfiles="/root/.config/ngrok"
# if [ !-d "$ngfiles"];then
#     sudo rm -r $ngfiles
# fi



cd ng
file_url="https://github.com/leonTech254/SimuPhish/raw/main/Asessts/auth.txt"
output_file="auth.txt"
wget "$file_url" -O "$output_file"
auth=$(head -n 1 "$output_file")
./ngrok authtoken $auth
# ./ngrok http $target_port 




if [ $? -eq 0 ]; then
  
  port=$target_port
  auth=$auth

  python3 ngrok.py -p "$port" -a "$auth"
  
  echo "All set successfully. Running the server"

else
  echo "Error checking port or auth"
  exit 1
fi






echo "hello wordl"