import dash_html_components as html

palettes = {"Confirmados": "teal",
            "Muertes": "red",
            "% de letalidad": "#fba",
            '% Población contagiada total':"#a0f"}

gradients = {"Confirmados": "teal",
             "Muertes": "reds",
             "% de letalidad": "greys",
             r'% Población contagiada total': 'purples'}

theme = 'plotly_dark'

colors = {'fig_bgcolor': '#28263F'}

margins = {'vertical': '20px',
           'horizontal': '30px'}

paddings = {'vertical': '5px',
            'horizontal': '10px'}

styles = {'figure':{'background-color':colors["fig_bgcolor"],
               'margin':f"{margins['vertical']} {margins['horizontal']}",
               'padding':f"{paddings['vertical']} {paddings['horizontal']}"}
          }
