# SIGAM - Sistema Integrado de Gestion y Analisis Municipal

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red)](https://streamlit.io)
[![Docker](https://img.shields.io/badge/Docker-Cloud_Run-blue)](https://cloud.google.com/run)

Plataforma web para la digitalizacion y automatizacion del **Indice de Gestion de Servicios Municipales (IGSM)** de la Contraloria General de la Republica de Costa Rica.

---

## Informacion academica

| Campo | Detalle |
|-------|---------|
| **Curso** | BBCD0001 - Analisis de Datos |
| **Profesor** | Dagoberto Jose Herrera Murillo |
| **Institucion** | LEAD University |
| **Equipo** | Esteban Gutierrez Saborio, Jason Corrau Madrigal, Robson Sthiffen Calvo Ortega |
| **Periodo** | 2026 |

---

## Instalacion y ejecucion local

### Requisitos

- Python 3.11+
- pip

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/EstebanSabo07/Proyecto-An-lisis-de-datos---Grupo-2-.git
cd Proyecto-An-lisis-de-datos---Grupo-2-

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
streamlit run main.py
```

La aplicacion abre en `http://localhost:8501`.

### Credenciales de demo

| Rol | Acceso |
|-----|--------|
| Municipalidad | Seleccionar municipio + codigo `1234` |
| Contraloria | Usuario `contraloria` / contrasena `cgr2025` |

---

## Estructura del proyecto

```text
SIGAM/
├── main.py                  <- Punto de entrada y enrutador
├── requirements.txt
├── Dockerfile               <- Google Cloud Run
├── assets/
│   ├── style.css
│   ├── logo_cgr.svg
│   └── logo_lead.png
├── data/
│   ├── municipalities.py    <- 84 municipalidades con coordenadas
│   ├── indicators.py        <- Estructura IGSM completa (163 indicadores)
│   ├── calculation.py       <- Formula oficial CGR
│   └── mock_data.py         <- Datos simulados
├── database/
│   ├── models.py            <- Modelos ORM SQLAlchemy
│   ├── repositories.py      <- API publica de acceso a datos
│   ├── seed.py              <- Carga de datos de referencia
│   └── source/              <- CSV fuente del baseline IGSM 2025
├── components/
│   ├── ui.py                <- Componentes reutilizables
│   └── charts.py            <- Visualizaciones Plotly
├── notebooks/
│   └── ejemplo_uso_orm.ipynb
└── views/
    ├── landing.py           <- Pagina publica
    ├── login.py             <- Autenticacion
    ├── muni_home.py         <- Portal municipalidad
    ├── muni_form.py         <- Formulario IGSM
    ├── muni_results.py      <- Resultados municipales
    ├── admin_dashboard.py   <- Dashboard Contraloria
    ├── admin_municipalities.py
    ├── admin_analysis.py    <- Geo, clusteres, SEM y correlacion
    ├── admin_weights.py     <- Gestion de pesos
    └── admin_export.py      <- Exportacion y publicacion
```

---

## Funcionalidades principales

- 163 preguntas en el formulario (159 indicadores oficiales CGR mas 4 subpreguntas desglosadas para mayor claridad).
- Calculo automatico del indice con formula oficial.
- 5 niveles de madurez: Inicial, Basico, Intermedio, Avanzado y Optimizando.
- Validacion de consistencia en tiempo real.
- Deteccion de anomalias historicas (>15% de variacion).
- Carga de evidencias por indicador.
- Dashboard nacional con ranking de 84 municipalidades.
- Analisis geoespacial con mapa interactivo.
- Analisis de clusteres con K-Means y PCA.
- Modelo de Ecuaciones Estructurales (SEM).
- Analisis de correlaciones por servicio.
- Exportacion CSV y Excel multihoja.
- Simulador de pesos del indice.
- Capa ORM con SQLAlchemy para datos dimensionales `dm_*` y hechos `fact_*`.

---

## Notebook de ejemplo del ORM

El notebook [`notebooks/ejemplo_uso_orm.ipynb`](notebooks/ejemplo_uso_orm.ipynb) muestra como usar la API publica del ORM con una base SQLite temporal. Sirve como guia para que el equipo consulte municipalidades, servicios, indicadores, pesos, umbrales, respuestas, ranking y estadisticas sin modificar la base local de desarrollo.

---

## Despliegue en Google Cloud Run

```bash
# Build y deploy
gcloud run deploy sigam \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080
```

---

## Integracion futura

| Componente | Tecnologia | Estado |
|------------|------------|--------|
| Autenticacion | Firebase Authentication | Pendiente |
| Base de datos | Firestore o PostgreSQL | Pendiente |
| Analitica | BigQuery | Pendiente |
| Archivos | Cloud Storage | Pendiente |

---

## Licencia

Proyecto academico - LEAD University / CGR Costa Rica - 2026.
