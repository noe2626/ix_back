from flask import Flask, request
import pyodbc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def connection():
    s = 'localhost'
    d = 'ix_prueba' 
    u = 'sa'
    p = '645978312Pc.'
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    return conn

@app.route('/add', methods = ['POST'])
def insert():
    try:
        data = request.get_json()
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("insert into catalogo(articulo,precio) values(?,?)",data['articulo'],data['precio'])
        conn.commit()
        conn.close()
        return {'success': True}
    except Exception as e:
        print("*********",e)
        return {'success': False}
    

@app.route('/list', methods = ['GET'])
def get():
    try:
        articulos = []
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("select * from catalogo")
        for row in cursor.fetchall():
            articulos.append({"id": row[0], "articulo": row[1], "precio": row[2]})
        conn.close()
        return {'success': True, 'articulos': articulos}
    except Exception as e:
        print("*********",e)
        return {'success': False}

@app.route('/delete/<id>', methods = ['GET'])
def delete(id):
    try:
        articulos = []
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("delete from catalogo where id = ?", id)
        conn.commit()
        conn.close()
        return {'success': True}
    except Exception as e:
        print("*********",e)
        return {'success': False}

@app.route('/update', methods = ['POST'])
def update():
    try:
        data = request.get_json()
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("update catalogo set articulo = ?, precio = ? where id = ?",data['articulo'],data['precio'],data['id'])
        conn.commit()
        conn.close()
        return {'success': True}
    except Exception as e:
        print("*********",e)
        return {'success': False}