import dash_html_components as html
from dash.dependencies import Input, Output
import dash
from server import app


@app.callback(Output('information-container', 'style'),
              [Input('information-open-button', 'n_clicks', ),
               Input('information-close-button', 'n_clicks')])
def manage_information_container(n_open, n_close):
    ctx = dash.callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'information-open-button':
            return {"display": "block"}
        elif button_id == 'information-close-button':
            return {"display": "none"}

def information():
    return [  # modal div
        html.Div([  # content div
            html.Table([
                html.Tr([html.Th('Identificador'),
                         html.Th('Descripción')]),
                html.Tr([html.Td('Casos confirmados'),
                         html.Td('Nº de Casos reportados de COVID-19')]),
                html.Tr([html.Td('% Población contagiada'),
                         html.Td('% de población sobre 100 que sufrido COVID-19')]),
                html.Tr([html.Td('Fallecimientos'),
                         html.Td('Nº de personas fallecidas a causa de  COVID-19')]),
                html.Tr([html.Td('% Población fallecida'),
                         html.Td('% de población sobre 100 que fallecido a causa de  COVID-19')]),
                html.Tr([html.Td('% de letalidad'),
                         html.Td('% de personas sobre 100 que fallecen por haber sufrido COVID-19 (Fallecimientos * '
                                 '100 / Casos Confirmados)')])
            ], className='information-table'),
            html.Button('X',
                        id='information-close-button',
                        className='information-close-button')
        ],
            id='information-container',
            className='information-container',
            style={"display": "none"},
        ),
        html.Button('Información',
                    id='information-open-button',
                    className='information-open-button')
    ]
