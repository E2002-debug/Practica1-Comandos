from flask import Blueprint, render_template, request, redirect, jsonify
from controls.tda.stack.stackOperation import StackOperation
from flask_cors import CORS

router = Blueprint('router', __name__)

# Página de inicio
@router.route('/')
def home():
    return render_template("template.html")

# Mostrar lista de comandos
@router.route('/comando')
def lista_comandos():
    file_path = r"C:\Users\USUARIO_PC\Documents\Proyecto Estructura\Practica1\data\stack_data.json"
    pd = StackOperation.from_json(file_path)  # Cargar los datos desde JSON
    lista_comandos = list(pd)  # Convertir la instancia de StackOperation a lista
    return render_template("comando/lista.html", lista=lista_comandos)



# Ver página para guardar comando
@router.route('/comando/ver')
def ver_guardar():
    return render_template("comando/guardar.html")

# Guardar comando
@router.route('/comando/guardar', methods=["POST"])
def guardar_comando():
    file_path = r"C:\Users\USUARIO_PC\Documents\Proyecto Estructura\Practica1\data\stack_data.json"
    pd = StackOperation.from_json(file_path)  # Cargar los datos desde JSON
    data = request.form
    
    if "comando" not in data:
        return jsonify({"error": "El comando no fue proporcionado"}), 400
        
    comando = data["comando"]
    pd.push(comando)
    pd.to_json()  # Guardar los datos en JSON después de agregar el comando
    print("Comando guardado correctamente:", comando)
    return redirect("/comando", code=302)
