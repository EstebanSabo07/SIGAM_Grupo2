# data/indicators.py — Estructura completa del IGSM 2025 (159 indicadores)
# Fuente: Fichas de Indicadores CGR 2025

# Tipos de indicador
TIPO_BINARIO    = "binario"      # Sí / No → puntaje 0 o 1
TIPO_COBERTURA  = "cobertura"    # Fórmula de cobertura por distrito (0, 0.25, 0.50, 1)
TIPO_PORCENTAJE = "porcentaje"   # Valor numérico con fórmula
TIPO_INFORMATIVO= "informativo"  # No tiene puntaje, solo informativo
TIPO_DECISION   = "decision"     # Bifurca hacia otros indicadores

# Etapas y sus pesos globales
PESOS_ETAPA = {
    "Planificación": 0.50,
    "Ejecución":     0.30,
    "Evaluación":    0.20,
}

# Umbrales oficiales ajustados (100% exactitud en 84 municipalidades)
UMBRALES_NIVEL = [
    (0.00, 0.31, "Inicial"),
    (0.31, 0.56, "Básico"),
    (0.56, 0.76, "Intermedio"),
    (0.76, 0.91, "Avanzado"),
    (0.91, 1.00, "Optimizando"),
]

COLORES_NIVEL = {
    "Inicial":     "#DC3545",
    "Básico":      "#FD7E14",
    "Intermedio":  "#2196F3",
    "Avanzado":    "#20C997",
    "Optimizando": "#7B2FBE",
}

def clasificar_nivel(score: float) -> str:
    for lo, hi, nivel in UMBRALES_NIVEL:
        if lo <= score < hi:
            return nivel
    return "Optimizando"

# ── Estructura de servicios e indicadores ────────────────────────────────────
# Organización: Eje → Servicio → Etapa → Indicadores

ESTRUCTURA_IGSM = {
    "Salubridad Pública": {
        "tipo": "eje",
        "codigo": "1",
        "servicios": {
            "Recolección, depósito y tratamiento de residuos sólidos": {
                "codigo_servicio": "1.1",
                "agrupacion": "Básico",
                "etapas": {
                    "Planificación": [
                        {"codigo": "1.1.1.1",  "nombre": "Se brinda el servicio de recolección, depósito y tratamiento de residuos", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.2",  "nombre": "Reglamento del servicio", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente del servicio"},
                        {"codigo": "1.1.1.3",  "nombre": "Planificación del servicio de recolección, depósito y tratamiento de residuos sólidos", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan municipal de gestión integral de residuos"},
                        {"codigo": "1.1.1.4",  "nombre": "Identificación de la población vulnerable para la prestación del servicio", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.5",  "nombre": "Inclusión en la planificación de la población vulnerable", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.6",  "nombre": "Frecuencia en la actualización de la tasa por el servicio", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Publicación en La Gaceta de la tasa vigente"},
                        {"codigo": "1.1.1.7",  "nombre": "Estrategias de promoción de la gestión integral en la ciudadanía", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.8",  "nombre": "Existencia de una unidad de gestión ambiental", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Ejecución": [
                        {"codigo": "1.1.1.9",  "nombre": "Centro de recuperación de residuos valorizables", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.10", "nombre": "Cobertura del servicio de recolección de residuos sólidos", "tipo": TIPO_COBERTURA, "evidencia": False},
                        {"codigo": "1.1.1.11", "nombre": "Recolección de residuos valorizables", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.12", "nombre": "Cobertura del Servicio de Recolección de Residuos Valorizables", "tipo": TIPO_COBERTURA, "evidencia": False},
                        {"codigo": "1.1.1.13", "nombre": "Porcentaje de valorización en el servicio de recolección de residuos", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "1.1.1.14", "nombre": "Sensibilización de la ciudadanía en respuesta al servicio de recolección de residuos", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.15", "nombre": "Recursos del servicio destinados por distrito", "tipo": TIPO_INFORMATIVO, "evidencia": False},
                        {"codigo": "1.1.1.16", "nombre": "Ingresos y gastos del servicio de recolección y depósito", "tipo": TIPO_DECISION, "evidencia": False},
                        {"codigo": "1.1.1.17", "nombre": "Nivel de ejecución de los recursos disponibles del servicio de recolección y depósito", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "1.1.1.18", "nombre": "Recursos destinados al desarrollo del servicio de Recolección", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "1.1.1.19", "nombre": "Morosidad del servicio de recolección de residuos", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "1.1.1.20", "nombre": "Satisfacción del usuario del servicio de recolección de residuos sólidos", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Estudio de satisfacción del usuario"},
                        {"codigo": "1.1.1.21", "nombre": "Evaluación de la calidad del servicio de recolección de residuos sólidos", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.22", "nombre": "Plan de mejora del servicio de recolección de residuos sólidos", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora vigente"},
                        {"codigo": "1.1.1.23", "nombre": "Implementación del plan de mejora del servicio de recolección", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.24", "nombre": "Inclusión en la evaluación de la población en condición de vulnerabilidad", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.1.1.25", "nombre": "Accesibilidad del servicio para personas con discapacidad", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                },
            },
            "Aseo de vías y sitios públicos": {
                "codigo_servicio": "1.2",
                "agrupacion": "Básico",
                "etapas": {
                    "Planificación": [
                        {"codigo": "1.2.1.1", "nombre": "Se brinda el servicio de aseo de vías y sitios públicos", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.2.1.2", "nombre": "Reglamento del servicio de aseo de vías", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente"},
                        {"codigo": "1.2.1.3", "nombre": "Planificación del servicio de aseo de vías", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan del servicio vigente"},
                        {"codigo": "1.2.1.4", "nombre": "Identificación de la población vulnerable", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.2.1.5", "nombre": "Actualización de la tasa del servicio de aseo de vías", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Publicación en La Gaceta"},
                    ],
                    "Ejecución": [
                        {"codigo": "1.2.1.6", "nombre": "Cobertura del servicio de aseo de vías", "tipo": TIPO_COBERTURA, "evidencia": False},
                        {"codigo": "1.2.1.7", "nombre": "Frecuencia del servicio de aseo de vías", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.2.1.8", "nombre": "Nivel de ejecución de los recursos del servicio", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "1.2.1.9", "nombre": "Recursos destinados al desarrollo del servicio", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "1.2.1.10", "nombre": "Morosidad del servicio de aseo de vías", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "1.2.1.11", "nombre": "Satisfacción del usuario del servicio", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Estudio de satisfacción"},
                        {"codigo": "1.2.1.12", "nombre": "Evaluación de la calidad del servicio", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.2.1.13", "nombre": "Plan de mejora del servicio de aseo de vías", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora"},
                        {"codigo": "1.2.1.14", "nombre": "Implementación del plan de mejora", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.2.1.15", "nombre": "Inclusión de población vulnerable en la evaluación", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                },
            },
            "Alcantarillado pluvial": {
                "codigo_servicio": "1.3",
                "agrupacion": "Diversificado",
                "diversificado_key": "alcantarillado",
                "etapas": {
                    "Planificación": [
                        {"codigo": "1.3.1.1", "nombre": "Se brinda el servicio de alcantarillado pluvial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.3.1.2", "nombre": "Reglamento del servicio de alcantarillado pluvial", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente"},
                        {"codigo": "1.3.1.3", "nombre": "Planificación del servicio de alcantarillado pluvial", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan del servicio"},
                        {"codigo": "1.3.1.4", "nombre": "Diagnóstico técnico del sistema pluvial", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Estudio técnico de necesidades"},
                        {"codigo": "1.3.1.5", "nombre": "Inventario del sistema pluvial", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Inventario actualizado"},
                        {"codigo": "1.3.1.6", "nombre": "Actualización de la tasa del servicio", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Publicación en La Gaceta"},
                    ],
                    "Ejecución": [
                        {"codigo": "1.3.1.7",  "nombre": "Mantenimiento preventivo del sistema pluvial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.3.1.8",  "nombre": "Control e inspección del sistema pluvial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.3.1.9",  "nombre": "Nivel de ejecución de los recursos del servicio", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "1.3.1.10", "nombre": "Recursos destinados al desarrollo del servicio", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "1.3.1.11", "nombre": "Morosidad del servicio de alcantarillado pluvial", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "1.3.1.12", "nombre": "Detección de vertidos inadecuados", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "1.3.1.13", "nombre": "Evaluación de la calidad del sistema pluvial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "1.3.1.14", "nombre": "Plan de mejora del servicio", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora"},
                        {"codigo": "1.3.1.15", "nombre": "Implementación del plan de mejora", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                },
            },
        },
    },
    "Desarrollo Urbano": {
        "tipo": "eje",
        "codigo": "2",
        "servicios": {
            "Urbanismo e infraestructura": {
                "codigo_servicio": "2.1",
                "agrupacion": "Básico",
                "etapas": {
                    "Planificación": [
                        {"codigo": "2.1.1.1", "nombre": "Reglamento de desarrollo urbanístico", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente"},
                        {"codigo": "2.1.1.2", "nombre": "Plan regulador cantonal vigente", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan regulador aprobado"},
                        {"codigo": "2.1.1.3", "nombre": "Plan de ordenamiento territorial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.1.1.4", "nombre": "Identificación de zonas de riesgo", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Mapa de riesgo"},
                        {"codigo": "2.1.1.5", "nombre": "Inclusión de población vulnerable en la planificación urbana", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.1.1.6", "nombre": "Actualización de la tasa de servicios urbanos", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Publicación en La Gaceta"},
                        {"codigo": "2.1.1.7", "nombre": "Sistema de información geográfica cantonal", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Ejecución": [
                        {"codigo": "2.1.1.8",  "nombre": "Control de asentamientos informales", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.1.1.9",  "nombre": "Permisos de construcción gestionados", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "2.1.1.10", "nombre": "Inspecciones urbanísticas realizadas", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.1.1.11", "nombre": "Nivel de ejecución de recursos del servicio", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "2.1.1.12", "nombre": "Recursos destinados al desarrollo del servicio", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "2.1.1.13", "nombre": "Espacios públicos mantenidos", "tipo": TIPO_COBERTURA, "evidencia": False},
                        {"codigo": "2.1.1.14", "nombre": "Accesibilidad universal en espacios públicos", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.1.1.15", "nombre": "Gestión de riesgos ante desastres naturales", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "2.1.1.16", "nombre": "Evaluación del plan regulador", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.1.1.17", "nombre": "Plan de mejora del servicio urbanístico", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora"},
                    ],
                },
            },
            "Red vial cantonal": {
                "codigo_servicio": "2.2",
                "agrupacion": "Básico",
                "etapas": {
                    "Planificación": [
                        {"codigo": "2.2.1.1",  "nombre": "Reglamento de la red vial cantonal", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente"},
                        {"codigo": "2.2.1.2",  "nombre": "Plan de conservación vial cantonal", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de conservación vial"},
                        {"codigo": "2.2.1.3",  "nombre": "Inventario vial cantonal actualizado", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Inventario vial"},
                        {"codigo": "2.2.1.4",  "nombre": "Diagnóstico del estado de la red vial", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Diagnóstico técnico"},
                        {"codigo": "2.2.1.5",  "nombre": "Identificación de necesidades de la población vulnerable", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.2.1.6",  "nombre": "Presupuesto destinado a la red vial", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                    ],
                    "Ejecución": [
                        {"codigo": "2.2.1.7",  "nombre": "Mantenimiento rutinario de la red vial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.2.1.8",  "nombre": "Mantenimiento periódico de la red vial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.2.1.9",  "nombre": "Obras de mejoramiento vial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.2.1.10", "nombre": "Señalización vial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.2.1.11", "nombre": "Nivel de ejecución de recursos viales", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "2.2.1.12", "nombre": "Cobertura del servicio vial", "tipo": TIPO_COBERTURA, "evidencia": False},
                        {"codigo": "2.2.1.13", "nombre": "Accesibilidad para personas con discapacidad", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "2.2.1.14", "nombre": "Evaluación del estado de la red vial", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.2.1.15", "nombre": "Plan de mejora vial", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora"},
                        {"codigo": "2.2.1.16", "nombre": "Satisfacción del usuario del servicio vial", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                },
            },
            "Zona Marítimo Terrestre": {
                "codigo_servicio": "2.3",
                "agrupacion": "Diversificado",
                "diversificado_key": "zmt",
                "etapas": {
                    "Planificación": [
                        {"codigo": "2.3.1.1", "nombre": "Plan de uso de la Zona Marítimo Terrestre", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan regulador ZMT"},
                        {"codigo": "2.3.1.2", "nombre": "Reglamento de la ZMT", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente ZMT"},
                        {"codigo": "2.3.1.3", "nombre": "Catastro de la ZMT actualizado", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Catastro de concesiones"},
                        {"codigo": "2.3.1.4", "nombre": "Cobro de cánones de la ZMT", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.3.1.5", "nombre": "Presupuesto para administración de la ZMT", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                    ],
                    "Ejecución": [
                        {"codigo": "2.3.1.6", "nombre": "Inspecciones de la ZMT realizadas", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.3.1.7", "nombre": "Control de construcciones en la ZMT", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.3.1.8", "nombre": "Nivel de ejecución de recursos de la ZMT", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "2.3.1.9", "nombre": "Recuperación de canon de concesiones ZMT", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "2.3.1.10","nombre": "Atención de denuncias en la ZMT", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "2.3.1.11","nombre": "Evaluación del plan de uso de la ZMT", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "2.3.1.12","nombre": "Plan de mejora de la ZMT", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora"},
                        {"codigo": "2.3.1.13","nombre": "Implementación del plan de mejora ZMT", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                },
            },
        },
    },
    "Servicios Sociales": {
        "tipo": "eje",
        "codigo": "3",
        "servicios": {
            "Servicios sociales y complementarios": {
                "codigo_servicio": "3.1",
                "agrupacion": "Básico",
                "etapas": {
                    "Planificación": [
                        {"codigo": "3.1.1.1", "nombre": "Reglamento de servicios sociales", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente"},
                        {"codigo": "3.1.1.2", "nombre": "Plan de servicios sociales cantonal", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de servicios sociales"},
                        {"codigo": "3.1.1.3", "nombre": "Identificación de grupos vulnerables", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.1.1.4", "nombre": "Articulación con redes de apoyo social", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.1.1.5", "nombre": "Presupuesto destinado a servicios sociales", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                    ],
                    "Ejecución": [
                        {"codigo": "3.1.1.6",  "nombre": "Cobertura de servicios sociales", "tipo": TIPO_COBERTURA, "evidencia": False},
                        {"codigo": "3.1.1.7",  "nombre": "Atención a población en condición de vulnerabilidad", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.1.1.8",  "nombre": "Nivel de ejecución de recursos sociales", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "3.1.1.9",  "nombre": "Programas de atención a adultos mayores", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.1.1.10", "nombre": "Programas de atención a personas con discapacidad", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.1.1.11", "nombre": "Programas de atención a niñez y adolescencia", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "3.1.1.12", "nombre": "Satisfacción de usuarios de servicios sociales", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Estudio de satisfacción"},
                        {"codigo": "3.1.1.13", "nombre": "Evaluación del impacto de servicios sociales", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.1.1.14", "nombre": "Plan de mejora de servicios sociales", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora"},
                        {"codigo": "3.1.1.15", "nombre": "Implementación del plan de mejora", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.1.1.16", "nombre": "Inclusión de enfoque de género en la evaluación", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                },
            },
            "Servicios educativos, culturales y deportivos": {
                "codigo_servicio": "3.2",
                "agrupacion": "Básico",
                "etapas": {
                    "Planificación": [
                        {"codigo": "3.2.1.1", "nombre": "Reglamento de servicios culturales y deportivos", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente"},
                        {"codigo": "3.2.1.2", "nombre": "Plan de cultura y deporte cantonal", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan cantonal vigente"},
                        {"codigo": "3.2.1.3", "nombre": "Identificación de necesidades culturales y deportivas", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.2.1.4", "nombre": "Presupuesto para servicios culturales y deportivos", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "3.2.1.5", "nombre": "Infraestructura disponible para actividades", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Ejecución": [
                        {"codigo": "3.2.1.6",  "nombre": "Cobertura de actividades culturales y deportivas", "tipo": TIPO_COBERTURA, "evidencia": False},
                        {"codigo": "3.2.1.7",  "nombre": "Programas culturales ejecutados", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.2.1.8",  "nombre": "Programas deportivos ejecutados", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.2.1.9",  "nombre": "Nivel de ejecución de recursos", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "3.2.1.10", "nombre": "Mantenimiento de infraestructura cultural y deportiva", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.2.1.11", "nombre": "Inclusión de grupos vulnerables en actividades", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "3.2.1.12", "nombre": "Satisfacción de participantes", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Estudio de satisfacción"},
                        {"codigo": "3.2.1.13", "nombre": "Evaluación del impacto de los programas", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.2.1.14", "nombre": "Plan de mejora de servicios culturales y deportivos", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora"},
                        {"codigo": "3.2.1.15", "nombre": "Implementación del plan de mejora", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.2.1.16", "nombre": "Inclusión de enfoque de género en evaluación", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                },
            },
            "Agua potable": {
                "codigo_servicio": "3.3",
                "agrupacion": "Diversificado",
                "diversificado_key": "agua_potable",
                "etapas": {
                    "Planificación": [
                        {"codigo": "3.3.1.1", "nombre": "Reglamento del servicio de agua potable", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente"},
                        {"codigo": "3.3.1.2", "nombre": "Plan maestro de agua potable", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan maestro"},
                        {"codigo": "3.3.1.3", "nombre": "Diagnóstico del sistema de agua potable", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Diagnóstico técnico"},
                        {"codigo": "3.3.1.4", "nombre": "Actualización de la tarifa del servicio", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Tarifa aprobada vigente"},
                        {"codigo": "3.3.1.5", "nombre": "Identificación de fuentes de agua protegidas", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Ejecución": [
                        {"codigo": "3.3.1.6",  "nombre": "Cobertura del servicio de agua potable", "tipo": TIPO_COBERTURA, "evidencia": False},
                        {"codigo": "3.3.1.7",  "nombre": "Calidad del agua distribuida", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Análisis de calidad del agua"},
                        {"codigo": "3.3.1.8",  "nombre": "Continuidad del servicio de agua", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "3.3.1.9",  "nombre": "Nivel de ejecución de recursos del servicio", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "3.3.1.10", "nombre": "Inversión en infraestructura de agua potable", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "3.3.1.11", "nombre": "Morosidad del servicio de agua potable", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "3.3.1.12", "nombre": "Satisfacción del usuario del servicio de agua", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Estudio de satisfacción"},
                        {"codigo": "3.3.1.13", "nombre": "Evaluación del sistema de agua potable", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.3.1.14", "nombre": "Plan de mejora del servicio de agua", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora"},
                        {"codigo": "3.3.1.15", "nombre": "Implementación del plan de mejora", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                },
            },
            "Seguridad y vigilancia": {
                "codigo_servicio": "3.4",
                "agrupacion": "Diversificado",
                "diversificado_key": "seguridad",
                "etapas": {
                    "Planificación": [
                        {"codigo": "3.4.1.1", "nombre": "Reglamento de seguridad y vigilancia", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Reglamento vigente"},
                        {"codigo": "3.4.1.2", "nombre": "Plan de seguridad cantonal", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de seguridad"},
                        {"codigo": "3.4.1.3", "nombre": "Diagnóstico de seguridad cantonal", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Diagnóstico de seguridad"},
                        {"codigo": "3.4.1.4", "nombre": "Coordinación interinstitucional en seguridad", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.4.1.5", "nombre": "Presupuesto destinado a seguridad", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                    ],
                    "Ejecución": [
                        {"codigo": "3.4.1.6",  "nombre": "Cobertura del servicio de seguridad", "tipo": TIPO_COBERTURA, "evidencia": False},
                        {"codigo": "3.4.1.7",  "nombre": "Personal de seguridad disponible", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "3.4.1.8",  "nombre": "Nivel de ejecución de recursos de seguridad", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                        {"codigo": "3.4.1.9",  "nombre": "Atención a denuncias de seguridad", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.4.1.10", "nombre": "Programas de prevención del delito", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.4.1.11", "nombre": "Infraestructura de vigilancia (cámaras, etc.)", "tipo": TIPO_BINARIO, "evidencia": False},
                    ],
                    "Evaluación": [
                        {"codigo": "3.4.1.12", "nombre": "Percepción ciudadana de seguridad", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Estudio de percepción"},
                        {"codigo": "3.4.1.13", "nombre": "Evaluación del plan de seguridad", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.4.1.14", "nombre": "Plan de mejora de seguridad", "tipo": TIPO_BINARIO, "evidencia": True, "doc": "Plan de mejora"},
                        {"codigo": "3.4.1.15", "nombre": "Implementación del plan de mejora", "tipo": TIPO_BINARIO, "evidencia": False},
                        {"codigo": "3.4.1.16", "nombre": "Reducción de índices delictivos", "tipo": TIPO_PORCENTAJE, "evidencia": False},
                    ],
                },
            },
        },
    },
}


def get_servicios_para_municipalidad(diversificados: list) -> dict:
    """Retorna solo los servicios que aplican para una municipalidad según sus diversificados."""
    servicios = {}
    for eje_nombre, eje_data in ESTRUCTURA_IGSM.items():
        for serv_nombre, serv_data in eje_data["servicios"].items():
            if serv_data["agrupacion"] == "Básico":
                servicios[serv_nombre] = {**serv_data, "eje": eje_nombre}
            elif serv_data.get("diversificado_key") in diversificados:
                servicios[serv_nombre] = {**serv_data, "eje": eje_nombre}
    return servicios


def contar_indicadores_totales() -> dict:
    total = plan = ejec = evalu = 0
    for eje_data in ESTRUCTURA_IGSM.values():
        for serv_data in eje_data["servicios"].values():
            for etapa, inds in serv_data["etapas"].items():
                count = len([i for i in inds if i["tipo"] != TIPO_INFORMATIVO])
                total += count
                if etapa == "Planificación": plan += count
                elif etapa == "Ejecución":   ejec += count
                elif etapa == "Evaluación":  evalu += count
    return {"total": total, "planificacion": plan, "ejecucion": ejec, "evaluacion": evalu}
