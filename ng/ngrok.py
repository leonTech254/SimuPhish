from pyngrok import ngrok,conf
import time
import sys
import os

download_directory = './'

os.makedirs(download_directory, exist_ok=True)

ngrok_download_path = os.path.join(download_directory, 'ngrok')

conf.get_default().ngrok_path = ngrok_download_path
port= sys.argv[1]
def run_ngrok(port):
    public_url = ngrok.connect(port)

    try:
        print(f"Ngrok Tunnel is live at: {public_url}")


    except KeyboardInterrupt:
        ngrok.disconnect(public_url)
        ngrok.kill()

if __name__ == "__main__":
    run_ngrok(5191)
