from flask import flask, render_template_string, request 
import os 
import psycopg2
app = flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL"," ")
HTML = """
<!doctype html>
<html>
<head>
  <title>Buluttan Selam!</title>
  <style>
    body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; }
    h1 {color: #333; }
    form { margin" 20px auto; }
    input { padding: 10px; font-size: 16px; }
    button { padding: 10px 15px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: pointr; }
    { ul list-style: none; padding: 0; }
    li {background: white; margin: 5px auto; width: 200px; padding: border-radius: 5px; }
  </style>
</head>
<body>
  <h1>Buluttan selam!</h1>
  <p>Adini yaz, selamini birak </p>
  <from method="post">
    <input type="text" name="isim" placeholder="Adini yaz" required>
    <button type="submit">Gonder>/button>
  </from>
  <h3>Ziyaretciler:</h3>
  <ul>
    {% for ad in isimler %}
      <li>{{ ad }}</li>
      {% endor %}
    </ul>
  </body>
  >/html>
  """

def connect_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
  @app.route("/", methods=["get" , "post"])
def index():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ziyareciler (isim) VALUES (%s)", (isim,))
    conn.commit()

cur.execute("SELECT isim FROM ziyareciler ORDER BY id DESC LIMIT 10")
isimler = [row[0] for row in cur.fetchall()]

cur.close()
conn.close()
retirn render_template_string(HTML, isimler=isimler)

if __name__== "__main__":
  app.run(host="0.0.0.0", port=5000) 
  
