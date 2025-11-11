from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"  # for session handling

DB_FILE = "prompts.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            sample_output TEXT NOT NULL,
            author TEXT NOT NULL
        )
        """)
        conn.commit()

init_db()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            session['username'] = username
            return redirect(url_for('upload'))
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        sample_output = request.form.get('sample_output')

        if title and description and sample_output:
            with sqlite3.connect(DB_FILE) as conn:
                c = conn.cursor()
                c.execute(
                    "INSERT INTO prompts (title, description, sample_output, author) VALUES (?, ?, ?, ?)",
                    (title, description, sample_output, session['username'])
                )
                conn.commit()
            return redirect(url_for('prompts'))

    return render_template('upload.html', username=session['username'])

@app.route('/prompts')
def prompts():
    with sqlite3.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT title, description, sample_output, author FROM prompts ORDER BY id DESC")
        data = c.fetchall()
    return render_template('prompts.html', prompts=data)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
