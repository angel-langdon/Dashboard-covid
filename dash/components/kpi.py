import dash_html_components as html
from utils import beautify_number


def kpi(title, number, color, prefix=''):
    number = number.iloc[0]
    div = html.Div(children=[
        html.H4(children=title,
                className='kpi-title'),
        html.Div(children=[
            html.H6(children=f"{beautify_number(number)}{prefix}",
                    className='kpi-number'),
            html.Div(className='div-color',
                     style={
                         'margin-left': 30,
                         'height': 40,
                         'width': 40,
                         'background-color': color,
                     })
        ], className='kpi-number-color-container',
        style={'display':'flex'})

    ],
        className='horizontal-expanded',
        style={'margin': 10})
    return div
