import dash_html_components as html


def title():
    return html.Div(children=[
        html.H1(children=['Dashboard COVID-19 España'],
                className="title"),
        html.H4(children=['by ',
            html.A(children="Angel",
                   href='https://www.linkedin.com/in/%C3%A1ngel-langdon-villamayor-a44b49187/'),
            ' and ',
            html.A(children="Ignacio",
                   href='https://www.linkedin.com/in/ignacio-cano/'),
        ], className='autores')
    ], className='title-container')
