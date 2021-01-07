from components.title import title
from components.confirmados_muertes_letalidad_barras_verticales import confirmados_muertes_letalidad_barras_verticales
from components.mapa_acumulado import mapa_acumulado
from components.grafico_lineas import grafico_lineas
from components.information import information
from components.footer import footer
from components.divider import divider
import constants as cons
import dash_html_components as html
import dash_core_components as dcc
from datasets import diario_acumulado_ultimo_sin_total
from datasets import diario_acumulado_ultimo
from datasets import geojson_comunidades
from datasets import diario_acumulado

DATA_FOLDER = "./data/final_data"


def layout():
    diario_acumulado
    return html.Div(children=[
        dcc.Store(id='diario-acumulado'),
        title(),
        divider,
        mapa_acumulado(diario_acumulado_ultimo_sin_total(),
                       geojson_comunidades,
                       cons,
                       diario_acumulado_ultimo()),
        html.Br(),
        divider,
        confirmados_muertes_letalidad_barras_verticales(diario_acumulado_ultimo_sin_total(), cons),
        divider,
        grafico_lineas(),
        html.Br(),
        *information(),
        footer(list(diario_acumulado_ultimo_sin_total()['Día'])[0])
    ])
