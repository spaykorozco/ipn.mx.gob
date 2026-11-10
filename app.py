
from flask import Flask, render_template, request

app = Flask(__name__)

# Registro de demostración
DOCUMENTOS = {
    "DEMO-2026-0001": {
        "nombre": "DOCUMENTO DE DEMOSTRACIÓN",
        "estatus": "VIGENTE",
        "folio": "DEMO-2026-0001",
        "fecha": "09/11/2026"
    }
}


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/consultar", methods=["POST"])
def consultar():
    folio = request.form.get("folio", "").strip()

    documento = DOCUMENTOS.get(folio)

    if documento:
        return render_template(
            "resultado.html",
            documento=documento
        )

    return render_template(
        "resultado.html",
        documento=None,
        folio=folio
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )