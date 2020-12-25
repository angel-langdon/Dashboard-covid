import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

def grafico_barras_verticales(df, y_value, cons,  x_value="Comunidad Autónoma"):
    return px.bar(df.sort_values(by=[y_value]),
                  x=x_value,
                  y=y_value,
                  color_discrete_sequence=[cons.palettes[y_value]])


def confirmados_muertes_letalidad_barras_verticales(df, cons):
    return html.Div(children=[

        html.Div(children=[
            dcc.Graph(
                id='grafico-confirmados',
                figure=grafico_barras_verticales(df,
                                                 "Confirmados", cons),
                className="six columns"

            ),
            dcc.Graph(
                id='grafico-muertes',
                figure=grafico_barras_verticales(df,
                                                 "Muertes", cons),
                className="six columns"
            )], className="row"),
        dcc.Graph(
            id='tasa-mortalidad',
            figure=grafico_barras_verticales(df,
                                             "% de letalidad", cons))

    ])
