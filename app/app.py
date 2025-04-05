from flask import Flask, Response
import getpass
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route("/htop")
def htop():
    full_name = "Abhishek Agarwal"

    username = getpass.getuser()

    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -20")
    except Exception as e:
        top_output = f"Error running top: {str(e)}"

    output = f"""Name: {full_name}
user: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}
"""
    return Response(output, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)