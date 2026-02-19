from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app) 

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="bd_final_pi"
    )

# Ruta GET: 
@app.route('/desarrolladores', methods=['GET'])
def get_desarrolladores():
    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True) 
        cursor.execute("SELECT * FROM developer") 
        lista = cursor.fetchall()
        return jsonify(lista)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexion' in locals():
            conexion.close()

# Ruta PUT: 
@app.route('/desarrolladores/<int:id>', methods=['PUT'])
def update_desarrollador(id):
    try:
        data = request.get_json() 
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        sql = "UPDATE developer SET name = %s, skills = %s, salary = %s, avatar = %s WHERE id = %s"
        valores = (data['name'], data['skills'], data['salary'], data['avatar'], id)
        
        cursor.execute(sql, valores)
        conexion.commit() 
        
        if cursor.rowcount > 0:
            return jsonify({"mensaje": "Desarrollador actualizado"})
        else:
            return jsonify({"error": "Desarrollador no encontrado"}), 404
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexion' in locals():
            conexion.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)