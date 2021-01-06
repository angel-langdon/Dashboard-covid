import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

info = {'Confirmados': "Casos confirmados totales",
        'Muertes': 'Fallecimientos totales',
        '% Población contagiada total': '% de población contagiada total',
        '% de letalidad': '% de letalidad total'}


def grafico_barras_verticales(df, y_value, cons, x_value="Comunidad/Ciudad Autónoma"):
    custom_data = ['Comunidad/Ciudad Autónoma', y_value]
    fig = px.bar(df.sort_values(by=[y_value]),
                 x=x_value,
                 y=y_value,
                 template=cons.theme,
                 custom_data=custom_data,
                 color_discrete_sequence=[cons.palettes[y_value]],
                 title=info[y_value])
    fig.update_layout({'plot_bgcolor': cons.colors['fig_bgcolor'],
                       'paper_bgcolor': cons.colors['fig_bgcolor'],
                       'autosize': True})

    porcentaje_1 = ":.4f" if '%' in y_value else ""
    fig.update_traces(hovertemplate="<br>".join([
        custom_data[0] + ": %{customdata[0]}",
        custom_data[1] + ": %{customdata[1]" + porcentaje_1 + "}",
    ]))
    return fig


def confirmados_muertes_letalidad_barras_verticales(df, cons):
    return html.Div(children=[

        html.H2(children='Datos acumulados por comunidad autónoma',
                style={'text-align': 'center'}),

        html.Div(children=[
            dcc.Graph(
                id='grafico-confirmados',
                figure=grafico_barras_verticales(df,
                                                 "Confirmados", cons),
                className="horizontal-expanded",
                style=cons.styles['figure'],
                config={'responsive': True}

            ),
            dcc.Graph(
                id='grafico-muertes',
                figure=grafico_barras_verticales(df,
                                                 "Muertes", cons),
                className="horizontal-expanded",
                style=cons.styles['figure'],
                config={'responsive': True}

            )], className="custom-row"),

        html.Div(children=[
            dcc.Graph(
                id='tasa-contagios',
                figure=grafico_barras_verticales(df,
                                                 "% Población contagiada total", cons),
                className="horizontal-expanded",
                style=cons.styles['figure'],
                config={'responsive': True}

            ),
            dcc.Graph(
                id='tasa-mortalidad',
                figure=grafico_barras_verticales(df,
                                                 "% de letalidad", cons),
                className="horizontal-expanded",
                style=cons.styles['figure'],
                config={'responsive': True}
            ),
        ], className="custom-row")

    ])
