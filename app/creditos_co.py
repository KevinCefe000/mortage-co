import mortgage

TASA_USURA = {
    (2025, 1): 0.2489, (2025, 2): 0.2630, (2025, 3): 0.2492, (2025, 4): 0.2562,
    (2025, 5): 0.2597, (2025, 6): 0.2555, (2025, 7): 0.2478, (2025, 8): 0.2517,
    (2025, 9): 0.2501, (2025, 10): 0.2436, (2025, 11): 0.2499, (2025, 12): 0.2502,
    (2026, 1): 0.2436, (2026, 2): 0.2523, (2026, 3): 0.2552, (2026, 4): 0.2676,
    (2026, 5): 0.2817, (2026, 6): 0.2879, (2026, 7): 0.2879, (2026, 8): 0.2966,
    (2026, 9): 0.2924,
}


def tasa_usura_vigente(anio, mes):
    clave = (anio, mes)
    if clave not in TASA_USURA:
        raise KeyError("No hay tasa de usura registrada para %s-%02d" % (anio, mes))
    return TASA_USURA[clave]


def clasificar_credito(monto):
    if monto <= 0:
        raise ValueError("El monto debe ser mayor a cero")
    if monto <= 6_000_000:
        return "microcredito"
    if monto <= 100_000_000:
        return "consumo"
    return "comercial"


def validar_tasa_usura(tasa_ea, tasa_usura):
    if tasa_ea < 0 or tasa_usura < 0:
        raise ValueError("Las tasas no pueden ser negativas")
    return tasa_ea <= tasa_usura


def calcular_interes_mora(saldo, dias_mora, tasa_mora_ea):
    if saldo < 0 or dias_mora < 0 or tasa_mora_ea < 0:
        raise ValueError("Los valores no pueden ser negativos")
    tasa_diaria = tasa_mora_ea / 360
    return round(saldo * tasa_diaria * dias_mora, 2)


def cuota_francesa(monto, tasa_ea, meses):
    if monto <= 0 or meses <= 0 or tasa_ea < 0:
        raise ValueError("Parametros invalidos")
    i = tasa_ea / 12
    if i == 0:
        return round(monto / meses, 2)
    cuota = monto * i / (1 - (1 + i) ** (-meses))
    return round(cuota, 2)


def tabla_amortizacion_francesa(monto, tasa_ea, meses):
    cuota = cuota_francesa(monto, tasa_ea, meses)
    i = tasa_ea / 12
    saldo = monto
    tabla = []
    for mes in range(1, meses + 1):
        interes = round(saldo * i, 2)
        abono = round(cuota - interes, 2)
        saldo = round(saldo - abono, 2)
        if mes == meses:
            abono = round(abono + saldo, 2)
            saldo = 0.0
        tabla.append({
            "mes": mes,
            "cuota": cuota,
            "interes": interes,
            "abono_capital": abono,
            "saldo": saldo,
        })
    return tabla


def simular_credito(monto, tasa_ea, meses, anio, mes):
    usura = tasa_usura_vigente(anio, mes)
    return {
        "monto": monto,
        "clasificacion": clasificar_credito(monto),
        "cuota_mensual": cuota_francesa(monto, tasa_ea, meses),
        "tasa_usura_periodo": usura,
        "es_legal": validar_tasa_usura(tasa_ea, usura),
    }
