from flask import Flask, render_template, request

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

@app.route("/cinepolis")
def cine():
    return render_template("Cinepolis.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)