# Simulador de Crédito con Validación Legal Colombiana

Proyecto de la asignatura **Calidad del Software** (CUN) — Actividad de Construcción Aplicada (ACA).
Diseño y ejecución de pruebas unitarias sobre un software de cálculo de créditos.

## Descripción

Se parte de un software base de código abierto:

- **Software base:** [github.com/jbmohler/mortgage](https://github.com/jbmohler/mortgage) — calculadora de amortización de créditos por el sistema francés (cuota fija) en Python.

Sobre él, el grupo desarrolló el módulo **`app/creditos_co.py`**, que agrega reglas de la
legislación colombiana:

- Amortización francesa detallada (cuota fija y tabla de amortización).
- Tabla real de **tasas de usura** certificadas por la Superintendencia Financiera de Colombia (ene 2025 – sep 2026).
- Validación de la tasa de usura (detecta tasas por encima del máximo legal).
- Cálculo de intereses de mora por días de atraso.
- Clasificación del crédito (microcrédito, consumo o comercial).

## Estructura del proyecto

```
proyecto-calidad/
├── app/                 # Software a evaluar
│   ├── mortgage.py      # Software base (amortización francesa)
│   └── creditos_co.py   # Modificaciones del grupo (validación legal)
├── tests/               # Pruebas unitarias
│   ├── test_mortgage.py
│   ├── test_creditos_co.py
│   └── test_hallazgo_defecto.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Requisitos

- Docker y Docker Compose instalados.

## Cómo levantar el ambiente (Docker)

Desde la carpeta del proyecto:

```bash
docker compose up -d --build      # construye e inicia el contenedor
docker compose exec calidad bash  # entra al contenedor
```

Comprobación rápida (dentro del contenedor):

```bash
python -c "import mortgage; print(mortgage.Mortgage(0.0375, 360, 350000).monthly_payment())"
# Debe imprimir: 1620.91
```

## Cómo ejecutar las pruebas

Dentro del contenedor:

```bash
pytest tests/ -v
```

Resultado esperado: **13 passed, 1 failed**.

> La prueba que falla (`test_hallazgo_defecto.py`) es **intencional**: documenta un defecto
> real del software base — la función `dollar()` redondea siempre hacia arriba
> (`ROUND_CEILING`), por lo que 3.14159 da 3.15 en lugar de 3.14.

Para detener el contenedor:

```bash
docker compose down
```

## Autores

- Olierse José Atencia Herrera
- Kevin Uriel Ceferino Orozco
- Ronaldo Luis Florez Julio

Docente: Alexander Calderón Martínez — Programa de Ingeniería de Sistemas, CUN.
