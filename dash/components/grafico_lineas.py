import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px


def grafico_lineas(df, cons, app):
    FIG_HEIGHT = 350

    def generar(value, x_value, y_value):
        if y_value == "Confirmados":
            text = '% Población contagiada total'
            title = 'Casos confirmados'
        elif y_value == 'Muertes':
            text = '% Población fallecida total'
            title = 'Fallecimientos'
        elif y_value == '% Población contagiada total':
            text = 'Confirmados'
            title = '% Población contagiada total'
        else:
            text = 'Muertes'
            title = '% Población fallecida total'


        df_com = df[df["Comunidad Autónoma"] == value].copy()
        fig = px.line(df_com.sort_values(by=['Día']),
                      x=x_value,
                      y=y_value,
                      title=title,
                      hover_data=[y_value, text],
                      template=cons.theme,
                      color_discrete_sequence=[cons.palettes[y_value]],
                      height=FIG_HEIGHT)
        fig.update_layout({'plot_bgcolor': cons.colors['fig_bgcolor'],
                           'paper_bgcolor': cons.colors['fig_bgcolor'], })
        return fig

    @app.callback(
        [Output('grafico-lineas-com-confirmados', 'figure'),
         Output('grafico-lineas-com-muertes', 'figure'),
         Output('grafico-lineas-com-porc-confirmados', 'figure'),
         Output('grafico-lineas-com-porc-fallecidos', 'figure')],
        [Input('seleccionador-comunidad', 'value')])
    def grafico(value, x_value="Día"):
        if value == None:
            value = 'Total'
        return (generar(value, x_value, "Confirmados"),
                generar(value, x_value, "Muertes"),
                generar(value, x_value, "% Población contagiada total"),
                generar(value, x_value, "% Población fallecida total"))

    return html.Div(children=[
        html.H2(children="Evolución según comunidad autónoma", style={'text-align':'center'}),
        dcc.Dropdown(
        id='seleccionador-comunidad',
        options=[{'label': com, 'value': com} for com in sorted(df['Comunidad Autónoma'].unique())],
        value='Madrid',
        className='dropdown-selector',
        style={'background-color': '#232323',
               'color': '#f1f1f1',
               'padding': 5}),
        html.Div(children=[
            dcc.Graph(
                id=f'grafico-lineas-com-confirmados',
                className="horizontal-expanded",
                style=cons.styles['figure']
            ),
            dcc.Graph(
                id=f'grafico-lineas-com-muertes',
                className="horizontal-expanded",
                style=cons.styles['figure']
            )
        ], className="custom-row"),
        html.Div(children=[
            dcc.Graph(
                id=f'grafico-lineas-com-porc-confirmados',
                className="horizontal-expanded",
                style=cons.styles['figure']
            ),
            dcc.Graph(
                id=f'grafico-lineas-com-porc-fallecidos',
                className="horizontal-expanded",
                style=cons.styles['figure']
            )
        ], className="custom-row"),

    ])
