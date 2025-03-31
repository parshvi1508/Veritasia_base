from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
from supabase import create_client


load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

app = Flask(__name__)
@app.route('/')
@app.route('/haven')
def nest():
    stream_data = supabase.table('stream').select('*').order('published_at', desc=True).limit(1).execute()
    verse_data = supabase.table('verse').select('*').order('published_at', desc=True).limit(1).execute()
    veristasia_intro = "Welcome to Veristasia – A Riot of Chaos. Where words explode and thoughts roam free."

    return render_template('index.html', 
                           veristasia_intro=veristasia_intro, 
                           stream_post=stream_data.data[0] if stream_data.data else None, 
                           verse_post=verse_data.data[0] if verse_data.data else None)
@app.route('/stream')
def stream():
    stream_posts = supabase.table('stream').select('*').order('published_at', desc=True).execute()
    return render_template('stream.html', stream_posts=stream_posts.data)
@app.route('/verse')
def verse():
    verse_posts = supabase.table('verse').select('*').order('published_at', desc=True).execute()
    return render_template('verse.html', verse_posts=verse_posts.data)
@app.route('/origin')
def origin():
    return render_template('origin.html')
if __name__ == '__main__':
    app.run(debug=True)