import dash_html_components as html


def title():
    return html.Div(children=[
        html.H1(children=[html.A(children="Angel",
                                 href='https://www.linkedin.com/in/%C3%A1ngel-langdon-villamayor-a44b49187/'),
                          ' & ',
                          html.A(children="Nacho",
                                 href='https://www.linkedin.com/in/ignacio-cano/'),
                          ' | Dashboard COVID-19 España'],
                className="title"),
        html.Div(children=[
            "Fuente de los datos: ",
            html.A(children="John Hopkins University",
                   href='https://github.com/CSSEGISandData/COVID-19')],
            className='fuente-datos')
    ])
