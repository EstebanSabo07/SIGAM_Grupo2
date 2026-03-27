<<<<<<< HEAD
# SIGAM — Sistema Integrado de Gestión y Análisis Municipal

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red)](https://streamlit.io)
[![Docker](https://img.shields.io/badge/Docker-Cloud_Run-blue)](https://cloud.google.com/run)

Plataforma web para la digitalización y automatización del **Índice de Gestión de Servicios Municipales (IGSM)** de la Contraloría General de la República de Costa Rica.

---

## 📋 Información académica

| Campo | Detalle |
|-------|---------|
| **Curso** | BBCD0001 – Análisis de Datos |
| **Profesor** | Dagoberto José Herrera Murillo |
| **Institución** | LEAD University |
| **Equipo** | Esteban Gutiérrez Saborío · Jason Corrau Madrigal · Robson Sthiffen Calvo Ortega |
| **Período** | 2025 |

---

## 🚀 Instalación y ejecución local

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

La aplicación abre en `http://localhost:8501`

### Credenciales de demo

| Rol | Acceso |
|-----|--------|
| Municipalidad | Seleccionar municipio + código `1234` |
| Contraloría | Usuario `contraloria` / contraseña `cgr2025` |

---

## 🏗️ Estructura del proyecto

```
SIGAM/
├── main.py                  ← Punto de entrada y enrutador
├── requirements.txt
├── Dockerfile               ← Google Cloud Run
├── assets/
│   ├── style.css
│   ├── logo_cgr.svg
│   └── logo_lead.png
├── data/
│   ├── municipalities.py    ← 84 municipalidades con coordenadas
│   ├── indicators.py        ← Estructura IGSM completa (163 indicadores)
│   ├── calculation.py       ← Fórmula oficial CGR (100% exactitud)
│   └── mock_data.py         ← Datos simulados (proporciones reales 2025)
├── components/
│   ├── ui.py                ← Componentes reutilizables
│   └── charts.py            ← Visualizaciones Plotly
└── views/
    ├── landing.py           ← Página pública
    ├── login.py             ← Autenticación
    ├── muni_home.py         ← Portal municipalidad
    ├── muni_form.py         ← Formulario IGSM
    ├── muni_results.py      ← Resultados municipales
    ├── admin_dashboard.py   ← Dashboard Contraloría
    ├── admin_municipalities.py
    ├── admin_analysis.py    ← Geo · Clústeres · SEM · Correlación
    ├── admin_weights.py     ← Gestión de pesos
    └── admin_export.py      ← Exportación y publicación
```

---

## 📊 Funcionalidades principales

- ✅ Formulario IGSM digital con 163 indicadores (replicación exacta CGR 2025)
- ✅ Cálculo automático del índice con fórmula oficial
- ✅ 5 niveles de madurez: Inicial · Básico · Intermedio · Avanzado · Optimizando
- ✅ Validación de consistencia en tiempo real
- ✅ Detección de anomalías históricas (>15% variación)
- ✅ Carga de evidencias por indicador
- ✅ Dashboard nacional con ranking de 84 municipalidades
- ✅ Análisis geoespacial (mapa interactivo)
- ✅ Análisis de clústeres (K-Means + PCA)
- ✅ Modelo de Ecuaciones Estructurales (SEM)
- ✅ Análisis de correlaciones por servicio
- ✅ Exportación CSV y Excel multi-hoja
- ✅ Simulador de pesos del índice

---

## 🐳 Despliegue en Google Cloud Run

```bash
# Build y deploy
gcloud run deploy sigam \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080
```

---

## 🔮 Integración futura (backend)

| Componente | Tecnología | Estado |
|------------|-----------|--------|
| Autenticación | Firebase Authentication | 🔜 Pendiente |
| Base de datos | Firestore | 🔜 Pendiente |
| Analítica | BigQuery | 🔜 Pendiente |
| Archivos | Cloud Storage | 🔜 Pendiente |

---

## 📄 Licencia

Proyecto académico — LEAD University / CGR Costa Rica · 2025
=======
# Proyecto-An-lisis-de-datos---Grupo-2-
Análisis y replicación del Índice de Gestión de Servicios Municipales (IGSM) 2025 - Contraloría General de la República de Costa Rica. BBCD001 Análisis de Datos, Lead University.
>>>>>>> f415e5a3843e9347c04782b735c8a43b0b3d76a3
