import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from components.kpi import kpi


def mapa_acumulado(df, geojson, cons, df_total):
    info = {'Muertes': 'Fallecimientos',
            'Confirmados': 'Casos confirmados',
            '% de letalidad': '% de letalidad (muertes/casos)',
            '% Población contagiada total': ' % de la población contagiada'}

    def generar_mapa_acumulado(columna="Muertes"):
        custom_data=['Comunidad/Ciudad Autónoma', columna, 'Población']
        fig = px.choropleth(df,
                            geojson=geojson,
                            locations='Comunidad Autónoma',
                            color=columna,
                            featureidkey="properties.name",
                            title=info[columna],
                            template=cons.theme,
                            custom_data=custom_data,
                            color_continuous_scale=cons.gradients[columna],
                            height=600)
        fig.update_geos(fitbounds="locations", visible=False)

        porcentaje = ":.4f" if '%' in columna else ""
        fig.update_traces(hovertemplate="<br>".join([
            custom_data[0]+": %{customdata[0]}",
            custom_data[1]+": %{customdata[1]"+porcentaje+"}",
            custom_data[2] + ": %{customdata[2]}",

        ]))

        fig.update_layout({
            'plot_bgcolor': cons.colors['fig_bgcolor'],
            'paper_bgcolor': cons.colors['fig_bgcolor'],
            'geo': dict(bgcolor=cons.colors['fig_bgcolor']),
            'margin': {"b": 20}
        })

        return dcc.Graph(
            figure=fig
        )

    return html.Div(children=[
        html.H2(children="Choropleth datos acumulados", style={'text-align': 'center'}),
        html.Div(children=[
            html.Div(children=[
                kpi("Confirmados",
                    df_total.loc[df_total["Comunidad Autónoma"] == 'Total',
                                 'Confirmados'],
                    color=cons.palettes["Confirmados"]),
                kpi("% P. contagiada",
                    df_total.loc[df_total["Comunidad Autónoma"] == 'Total',
                                 '% Población contagiada total'],
                    color=cons.palettes['% Población contagiada total'],
                    prefix=' %'),
                kpi("Fallecimientos",
                    df_total.loc[df_total["Comunidad Autónoma"] == 'Total',
                                 'Muertes'],
                    color=cons.palettes["Muertes"]),
                kpi("% de letalidad",
                    df_total.loc[df_total["Comunidad Autónoma"] == 'Total',
                                 '% de letalidad'],
                    color=cons.palettes["% de letalidad"],
                    prefix=' %'),

            ], className='custom-row',
                style={'width': '98vw',
                       'margin': '0px 20px'}),
            dcc.Tabs(
                [dcc.Tab(label=col,
                         className='tab',
                         children=[generar_mapa_acumulado(col)]) for col in cons.gradients.keys()]
            )

        ], className='mapa-acumulado-container',
            style=cons.styles["figure"])])
