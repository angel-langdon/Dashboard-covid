import dash_html_components as html

def get_url(date):
    base_url = 'https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    date = date.split('-')
    date = f"{date[1]}-{date[2]}-{date[0]}"
    return f"{base_url}{date}.csv"
def footer(date):
    return html.Div(children=[
        html.Div(children=[
            f"Última actualización de los datos: ",
            html.A(children=date,
                   href=get_url(date))
        ]),
        html.Div(children=[
            "Fuente de los datos: ",
            html.A(children="John Hopkins University",
                   href='https://github.com/CSSEGISandData/COVID-19')],
            className='fuente-datos'),
    ],style={'display':'inline-block',
             'float':'right'})

