import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import constants as cons
from server import app
import pandas as pd


app.config.suppress_callback_exceptions = True

@app.callback(
    [Output('grafico-lineas-com-confirmados', 'figure'),
     Output('grafico-lineas-com-muertes', 'figure'),
     Output('grafico-lineas-com-porc-confirmados', 'figure'),
     Output('grafico-lineas-com-porc-fallecidos', 'figure')],
    [Input('seleccionador-comunidad', 'value'),
     State('diario-acumulado', 'data')])
def grafico(comunidad, df):
    if df is not None:
        df = pd.read_json(df)
        if comunidad is None:
            comunidad = 'Total'
        x_value = "Día"
        return (generar(comunidad, x_value, "Confirmados", df),
                generar(comunidad, x_value, "Muertes", df),
                generar(comunidad, x_value, "% Población contagiada total", df),
                generar(comunidad, x_value, "% Población fallecida total", df))


def generar(value, x_value, y_value, df):
    FIG_HEIGHT = 350
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
    custom_data = ['Comunidad/Ciudad Autónoma', x_value, y_value, text, 'Población']
    fig = px.line(df_com.sort_values(by=['Día']),
                  x=x_value,
                  y=y_value,
                  title=title,
                  hover_data=[y_value, text],
                  custom_data=custom_data,
                  template=cons.theme,
                  color_discrete_sequence=[cons.palettes[y_value]],
                  height=FIG_HEIGHT)
    porcentaje_1 = ":.4f" if '%' in y_value else ""
    porcentaje_2 = ":.4f" if '%' in text else ""
    fig.update_traces(hovertemplate="<br>".join([
        custom_data[0] + ": %{customdata[0]}",
        custom_data[1] + ": %{customdata[1]}",
        custom_data[2] + ": %{customdata[2]" + porcentaje_1 + "}",
        custom_data[3] + ": %{customdata[3]" + porcentaje_2 + "}",
        custom_data[4] + ": %{customdata[4]}",

    ]))
    fig.update_layout({'plot_bgcolor': cons.colors['fig_bgcolor'],
                       'paper_bgcolor': cons.colors['fig_bgcolor'], })
    return fig


def grafico_lineas():
    return html.Div('', id='grafico-lineas-')


@app.callback(Output('grafico-lineas-', 'children'),
              [Input('diario-acumulado', 'modified_timestamp'),
               State('diario-acumulado', 'data')])
def grafico_lineas_generador(ts, df):
    if df is None:
        return ''
    else:
        df = pd.read_json(df)
        return html.Div(children=[
            html.H2(children="Evolución acumulada según comunidad autónoma", style={'text-align': 'center'}),
            dcc.Dropdown(
                id='seleccionador-comunidad',
                options=[
                    {'label': com,
                     'value': df.loc[df['Comunidad/Ciudad Autónoma'] == com, 'Comunidad Autónoma'].iloc[1]}
                    for com in
                    sorted(df['Comunidad/Ciudad Autónoma'].unique())],
                value='Madrid',
                className='dropdown-selector',
                style={'background-color': '#232323',
                       'color': '#f1f1f1',
                       'padding': 5}),
            html.Div(children=[
                dcc.Graph(
                    id=f'grafico-lineas-com-confirmados',
                    className="horizontal-expanded",
                    style=cons.styles['figure'],
                    config={'responsive': True}
                ),
                dcc.Graph(
                    id=f'grafico-lineas-com-muertes',
                    className="horizontal-expanded",
                    style=cons.styles['figure'],
                    config={'responsive': True}
                )
            ], className="custom-row"),
            html.Div(children=[
                dcc.Graph(
                    id=f'grafico-lineas-com-porc-confirmados',
                    className="horizontal-expanded",
                    style=cons.styles['figure'],
                    config={'responsive': True}
                ),
                dcc.Graph(
                    id=f'grafico-lineas-com-porc-fallecidos',
                    className="horizontal-expanded",
                    style=cons.styles['figure'],
                    config={'responsive': True}
                )
            ], className="custom-row"),
        ])
