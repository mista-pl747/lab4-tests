from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

conn = sqlite3.connect(":memory:", check_same_thread=False)
conn.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
""")
conn.commit()

@app.post("/products")
def create(product: dict):
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price) VALUES (?, ?)",
                (product["name"], product["price"]))
    conn.commit()
    pid = cur.lastrowid
    return {"id": pid, **product}

@app.get("/products/{id}")
def read(id: int):
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products WHERE id = ?", (id,))
    row = cur.fetchone()
    if not row:
        raise HTTPException(404, "Not found")
    return {"id": row[0], "name": row[1], "price": row[2]}