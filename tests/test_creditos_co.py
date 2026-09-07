import pytest
import creditos_co as c


def test_clasificar_microcredito():
    assert c.clasificar_credito(2_000_000) == "microcredito"


def test_clasificar_monto_invalido_lanza_error():
    with pytest.raises(ValueError):
        c.clasificar_credito(-1)


def test_tasa_usura_vigente_enero_2026():
    assert c.tasa_usura_vigente(2026, 1) == 0.2436


def test_cuota_francesa_microcredito():
    assert c.cuota_francesa(2_000_000, 0.24, 12) == 189119.19


def test_tabla_francesa_salda_en_cero():
    tabla = c.tabla_amortizacion_francesa(2_000_000, 0.24, 12)
    assert len(tabla) == 12
    assert tabla[-1]["saldo"] == 0.0


def test_credito_legal_dentro_de_usura():
    assert c.validar_tasa_usura(0.24, c.tasa_usura_vigente(2026, 9)) is True


def test_usura_extrema_es_ilegal():
    assert c.validar_tasa_usura(11.4375, 0.2924) is False


def test_interes_mora_30_dias():
    assert c.calcular_interes_mora(1_000_000, 30, 0.2879) == 23991.67


def test_interes_mora_sin_dias_es_cero():
    assert c.calcular_interes_mora(1_000_000, 0, 0.2879) == 0.0
