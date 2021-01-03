import dash_html_components as html

palettes = {"Confirmados": "teal",
            "Muertes": "red",
            "% de letalidad": "#fba",
            '% Población contagiada total': "#a0f",
            '% Población fallecida total':'#faa'}

gradients = {"Confirmados": "teal",
             '% Población contagiada total': 'Purp',
             "Muertes": "reds",
             "% de letalidad": "Peach"}

theme = 'plotly_dark'

colors = {'fig_bgcolor': '#28263F'}

margins = {'vertical': '10px',
           'horizontal': '10px'}


paddings = {'vertical': '10px',
            'horizontal': '10px'}

styles = {'figure': {'background-color': colors["fig_bgcolor"],
                     'margin': f"{margins['vertical']} {margins['horizontal']}",
                     'padding': f"{paddings['vertical']} {paddings['horizontal']}"}
          }
