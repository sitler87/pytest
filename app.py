from flask import Flask
import os
app = Flask(__name__)

@app.route("/metrics")
def metrics():
    file_count = len(os.listdir("/tmp"))
    return f"# HELP tmp_file_count Number of files in /tmp\n# TYPE tmp_file_count gauge\ntmp_file_count {file_count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)