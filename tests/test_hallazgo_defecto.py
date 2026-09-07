import mortgage


def test_dollar_deberia_redondear_correctamente():
    assert str(mortgage.dollar(3.14159)) == "3.14"
