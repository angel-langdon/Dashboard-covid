import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px


def mapa_acumulado(df, geojson, cons, app):
    info = {'Muertes':'Choropleth del número de muertes totales',
            'Confirmados':'Choropleth del número de casos confirmados totales',
            '% de letalidad': 'Choropleth de % de letalidad (muertes/casos) total',
            '% Población contagiada total':'Choropleth del % de la población contagiada total'}


    def generar_mapa_acumulado(columna="Muertes"):
        fig = px.choropleth(df,
                            geojson=geojson,
                            locations='Comunidad Autónoma',
                            color=columna,
                            featureidkey="properties.name",
                            title=info[columna],
                            template=cons.theme,
                            color_continuous_scale=cons.gradients[columna],
                            height=600)
        fig.update_geos(fitbounds="locations", visible=False)

        fig.update_layout({
            'plot_bgcolor': cons.colors['fig_bgcolor'],
            'paper_bgcolor': cons.colors['fig_bgcolor'],
            'geo': dict(bgcolor=cons.colors['fig_bgcolor']),
            'margin' : {"b": 20}
        })

        return dcc.Graph(
            figure=fig

        )

    return html.Div(children=[
        dcc.Tabs(
            [dcc.Tab(label=col, className='tab',
                     children=[generar_mapa_acumulado(col)]) for col in cons.gradients.keys()]
            )

    ], className='mapa-acumulado-container',
        style=cons.styles["figure"])


