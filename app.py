from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
from supabase import create_client
from flask_wtf.csrf import CSRFProtect

from groq import Groq
from flask_socketio import SocketIO
load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

app = Flask(__name__)
socketio = SocketIO(app)
@app.route('/')
@app.route('/haven')
def nest():
    return render_template('index.html')
@app.route('/stream')
def stream():
    return render_template('stream.html')
@app.route('/verse')
def verse():
    return render_template('verse.html')
@app.route('/origin')
def origin():
    return render_template('origin.html')
if __name__ == '__main__':
    app.run(debug=True)