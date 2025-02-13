from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
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

if __name__ == "__main__":
    app.run(debug=True, port=3000)
