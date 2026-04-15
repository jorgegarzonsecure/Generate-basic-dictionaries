from datetime import date, timedelta

# Rango de fechas
inicio = date(1980, 1, 1)
fin = date(2026, 12, 31)

# Símbolos que quieres usar
simbolos = ["!", "@", "#", "%", "&", ".", ",", "*", "-", "+", "$", "="]

with open("fechas.rule", "w") as f:
    actual = inicio
    while actual <= fin:
        fecha = actual.strftime("%Y%m%d")
        # Variante 1: fecha al final
        regla_fecha = "".join([f"${c}" for c in fecha])
        f.write(regla_fecha + "\n")
        # Variante 2: símbolo + fecha
        for s in simbolos:
            regla_simbolo_fecha = f"${s}" + "".join([f"${c}" for c in fecha])
            f.write(regla_simbolo_fecha + "\n")
        actual += timedelta(days=1)
