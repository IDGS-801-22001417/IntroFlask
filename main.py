from flask import Flask, render_template, request
from datetime import datetime

app=Flask(__name__)

@app.route("/")
def index():
    titulo = "IDGS801"
    lista= ["Pedro", "Juan", "Luis"]
    return render_template("index.html", titulo = titulo, lista = lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/hola")
def hola():
    return "<h1>Hello, World! -- Hola!</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"<h1> ¡Hola, {user}!</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1> El número es: {n}!</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1> ¡Hola, {username}! Tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="Juan"):
    return f"<h1> ¡Hola, {param}!</h1>"

@app.route("/operas")
def operaciones():
    return '''
            <form>
                <label for="name">Name:</label>
                <input type="text">
            </form>
           '''

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/result", methods=["GET","POST"])
def result():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    return "La multiplicación de {} x {} es {}".format(n1,n2,str(int(n1)*int(n2)))

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    oper = request.form.get("oper")

    resultado = ""

    try:
        n1 = float(n1)
        n2 = float(n2)

        if oper == "suma":
            resultado = n1 + n2
            operacion = "suma"
        elif oper == "resta":
            resultado = n1 - n2
            operacion = "resta"
        elif oper == "multi":
            resultado = n1 * n2
            operacion = "multiplicación"
        elif oper == "division":
            if n2 != 0:
                resultado = n1 / n2
                operacion = "división"
            else:
                return "Error: No se puede dividir entre cero."

        return render_template("OperasBas.html", resultado=resultado)

    except ValueError:
        return "Error: Por favor ingrese números válidos."

@app.route("/Cinepolis")
def Cinepolis():
    return render_template("Cinepolis.html")


@app.route("/comprar", methods=["POST"])
def comprar():
    precio_entrada = 12.00
    try:
        personas = request.form.get("cantidadCompradores")
        boletos = request.form.get("cantidadBoletas")
        tarjeta = request.form.get("tarjetaCineco")

        if not personas or not personas.isdigit() or int(personas) <= 0:
            return render_template("Cinepolis.html", total="La cantidad de Compradores debe ser un número mayor a 0.")
        
        if not boletos or not boletos.isdigit() or int(boletos) <= 0:
            return render_template("Cinepolis.html", total="La cantidad de Boletas debe ser un número mayor a 0.")

        if tarjeta not in ["si", "no"]:
            return render_template("Cinepolis.html", total="Debes seleccionar una opción válida para Tarjeta Cineco.")

        personas = int(personas)
        boletos = int(boletos)

        if boletos > personas * 7:
            return render_template("Cinepolis.html", total="No puedes comprar más de 7 boletos por persona.")

        total = boletos * precio_entrada
        if 3 <= boletos <= 5:
            total *= (1 - 0.10)
        elif boletos > 5:
            total *= (1 - 0.15)
        
        if tarjeta == "si":
            total *= (1 - 0.10)
        
        return render_template("Cinepolis.html", total = str(round(total, 2)))

    except Exception as ex:
        return render_template("Cinepolis.html", total=f"Error: {str(ex)}")

@app.route("/ZodiacoChino")
def Zodiaco():
    return render_template("ZodiacoChino.html")

def calcular_edad(dia, mes, anio):
    hoy = datetime.now()
    fecha_nacimiento = datetime(anio, mes, dia)
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad

def signo_zodiacal_chino(anio):
    signos = [
        "Mono", "Gallo", "Perro", "Cerdo", "Rata", 
        "Buey", "Tigre", "Conejo", "Dragon", "Serpiente", 
        "Caballo", "Cabra"
    ]
    return signos[anio % 12]

@app.route("/imprimir", methods=["POST"])
def Imprimir():
    nombre = request.form.get("nombre")
    apaterno = request.form.get("apaterno")
    amaterno = request.form.get("amaterno")
    dia = int(request.form.get("dia"))
    mes = int(request.form.get("mes"))
    anio = int(request.form.get("anio"))
    sexo = request.form.get("sexo")

    edad = calcular_edad(dia, mes, anio)
    signo = signo_zodiacal_chino(anio)

    if sexo == "masculino":
        sexo = "Hombre"
    else:
        sexo = "Mujer"
    
    return render_template(
        "ZodiacoChino.html", 
        nombre=nombre, 
        apaterno=apaterno, 
        amaterno=amaterno, 
        edad=edad, 
        signo=signo,
        sexo=sexo
    )

if __name__ == "__main__":
    app.run(debug=True, port=3000)