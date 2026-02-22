from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            food TEXT,
            slot TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT slot, COUNT(*) FROM orders GROUP BY slot")
    data = c.fetchall()

    c.execute("SELECT COUNT(*) FROM orders")
    total_orders = c.fetchone()[0]

    conn.close()

    return render_template("index.html", data=data, total_orders=total_orders)

@app.route("/order", methods=["POST"])
def order():
    name = request.form["name"]
    food = request.form["food"]
    slot = request.form["slot"]

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO orders (name, food, slot) VALUES (?, ?, ?)",
              (name, food, slot))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)