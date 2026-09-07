import mortgage


def test_cuota_mensual_credito_hipotecario():
    m = mortgage.Mortgage(interest=0.0375, amount=350000, months=360)
    assert float(m.monthly_payment()) == 1620.91


def test_pago_total_igual_cuota_por_meses():
    m = mortgage.Mortgage(interest=0.0375, amount=350000, months=360)
    assert float(m.total_payout()) == 583527.60


def test_crecimiento_mensual():
    m = mortgage.Mortgage(interest=0.24, amount=2000000, months=12)
    assert m.month_growth() == 1.02


def test_redondeo_dollar_siempre_hacia_arriba():
    assert str(mortgage.dollar(3.14159)) == "3.15"
