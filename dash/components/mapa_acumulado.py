import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px


def mapa_acumulado(df, geojson, gradients, app):
    info = {'Muertes':'Choropleth del número de muertes totales',
            'Confirmados':'Choropleth del número de casos confirmados totales',
            '% de letalidad': 'Choropleth de % de letalidad (muertes/confirmados) total'}

    @app.callback(
        Output('mapa-acumulado', "figure"),
        [Input("mapa-acumulado-selector", "value")])
    def generar_mapa_acumulado(columna="Muertes"):
        fig = px.choropleth(df,
                            geojson=geojson,
                            locations='Comunidad Autónoma',
                            color=columna,
                            featureidkey="properties.name",
                            title= info[columna],
                            color_continuous_scale=gradients[columna])
        fig.update_geos(fitbounds="locations", visible=False)
        return fig

    return html.Div(children=[
        dcc.RadioItems(
            id='mapa-acumulado-selector',
            options=[{'value': x, 'label': x}
                     for x in gradients.keys()],
            value=list(gradients.keys())[0],
            labelStyle={'display': 'inline-block'}
        ),
        dcc.Graph(
            id='mapa-acumulado',
        )
    ], className='mapa-acumulado-container')


