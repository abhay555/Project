import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output, State
import plotly.express as px
from plotly.subplots import make_subplots

# --------------------------------------------------------------------Sector Economy--------------------------------------------------------------------

GDP_app1 = DjangoDash('SimpleExample')
df = pd.read_csv(
    'https://abhay555.github.io/plotly-plots/economy_by_sector.csv')
all_sec_df = df[(df['Sector'] == '_All') & ((df['Scenario'] == 'Shorter containment, smaller demand shock') | (
    df['Scenario'] == 'Longer containment, larger demand shock'))]


def GDP_Data1():
    fig = px.bar(all_sec_df.sort_values(by='Country 2018 GDP', ascending=False).head(100),
                 x='Economy', y='Country 2018 GDP',
                 hover_data=['Economy', 'Country 2018 GDP', 'Scenario'],
                 color='Scenario',
                 title='GDP',
                 color_discrete_sequence=['#FC0080', 'rgb(102,102,102)'], )
    fig.update_layout(
        legend=dict(
            yanchor="top",
            y=0.95,
            xanchor="left",
            x=0.20
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            size=13,
            color="#d6c6b2"
        ),

    )
    fig.update_yaxes(showgrid=False)
    return fig


GDP_app1.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='GDP graph1',
            figure=GDP_Data1()
        )
    ])
])


# --------------------------------------------------------------------Sector Education--------------------------------------------------------------------

EDU_app1 = DjangoDash('EDU_app1')
edu_impact = pd.read_csv(
    'https://abhay555.github.io/plotly-plots/covid_impact_education.csv')


def education_impact_global():
    Globe = px.choropleth(edu_impact,
                          locations='Country',
                          color='Status',
                          locationmode="country names",
                          projection='equirectangular',
                          animation_frame="Date",
                          hover_data=['Country'],
                          color_discrete_sequence=px.colors.qualitative.G10,
                          basemap_visible=False,
                          )
    Globe.update_layout(
        title='Global Education Sector',
        legend_title="Status",
        font=dict(
            size=15,
            color="#d6c6b2"
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    Globe.layout.template = 'plotly_dark'
    return Globe


EDU_app1.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='EDU_app1',
            figure=education_impact_global()
        )
    ])
])


# --------------------------------------------------------------------Sector Film_Industry--------------------------------------------------------------------
FILM_app1 = DjangoDash('FILM_app1')
film_df = pd.read_html('https://en.wikipedia.org/wiki/List_of_films_impacted_by_the_COVID-19_pandemic')[4].dropna(
    how='all', axis=1)
film_df.columns = ['Film', 'Original date', 'New date']
film_df = film_df.head(150)
film_df['New date'] = film_df['New date'].apply(lambda x: x.split('[')[0])
film_df['Original date'] = film_df['Original date'].apply(
    lambda x: x.split('[')[0])

film_df = film_df[(film_df['New date'].str.len() > 12) & (film_df['New date'].str.len() < 20) & (
    ~film_df['New date'].str.contains('Delayed' or 'Summer'))]

film_df['Original date'] = pd.to_datetime(
    film_df['Original date'], format='%B %d, %Y')
film_df['New date'] = pd.to_datetime(film_df['New date'], format='%B %d, %Y')

film_df['Date diff'] = film_df['New date'] - film_df['Original date']


def film_impact():
    fig = make_subplots(rows=2, cols=1,
                        subplot_titles=('Original Release date',
                                        'New Release date',),
                        shared_xaxes=True,
                        vertical_spacing=0.04,
                        )

    fig.add_trace(go.Scatter(
        x=film_df['Film'],
        y=film_df['Original date'],
        mode='markers+lines',
        name='Original Release Date'
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=film_df['Film'],
        y=film_df['New date'],
        mode='markers+lines',
        name='New Release Date'
    ), row=2, col=1)

    fig.update_layout(
        height=1000, width=1800,
        title_text="Impact on release dates of movies",
        legend=dict(
            yanchor="top",
            y=0.85,
            xanchor="left",
            x=0.30
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            size=13,
            color="#d6c6b2"
        ),
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    return fig


FILM_app1.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='FILM_app1',
            figure=film_impact()
        )
    ])
])

# --------------------------------------------------------------------Sector AQI--------------------------------------------------------------------

AQI_app1 = DjangoDash('AQI_app1')
aqi_impact = pd.read_csv('https://abhay555.github.io/plotly-plots/AQI.csv')


def aqi_impact1():
    fig = px.area(aqi_impact,
                  y='Air Quality Index',
                  x='State',
                  animation_frame='Date',
                  hover_data=['State', 'Station Name',
                              'Air Quality Index', 'Date'],
                  color_discrete_sequence=['crimson'],
                  title='Impact on Air Quality',
                  )
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1500
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            size=13,
            color="#d6c6b2"
        ),
    )
    fig.update_yaxes(showgrid=False)
    fig.update_xaxes(showgrid=False)
    return fig


AQI_app1.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='AQI_app1',
            figure=aqi_impact1()
        )
    ])
])


# --------------------------------------------------------------------Sector SABARMATI RIVER--------------------------------------------------------------------
River_app = DjangoDash('river_app')
riv_impact = pd.read_csv('static/sabarmati_river.csv')
riv_impact.drop(['Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5'],
                axis=1, inplace=True)
riv_impact.rename(columns={'Unnamed: 0': 'Condition', 'Unnamed: 1': 'Date of Acquisition',
                           'Unnamed: 2': 'Turbidity (mg/l)'}, inplace=True)
riv_impact.drop(index=0, inplace=True)
riv_impact.drop(index=1, inplace=True)


def riv_impact1():
    fig = px.bar(riv_impact,
                 x='Date of Acquisition',
                 y='Turbidity (mg/l)',
                 color='Condition',
                 title='SPM concentrations of the Sabarmati River for different periods',
                 color_discrete_sequence=['#007bff', '#ff0000']
                 )
    fig.update_yaxes(showgrid=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)',
                      legend=dict(
                          yanchor="top",
                          y=0.85,
                          xanchor="left",
                          x=0.40
                      ),
                      font=dict(
                          size=13,
                          color="#d6c6b2"
                      ),
                      ),
    fig.update_yaxes(showgrid=False)
    fig.update_traces(
        texttemplate=riv_impact['Turbidity (mg/l)'], textposition='outside')
    return fig


River_app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='River_app',
            figure=riv_impact1()
        )
    ])
])
