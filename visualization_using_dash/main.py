import makedf as md
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html
import math

path=input('Welcome to Holoplot QA Results Visualization,\n ********Please Enter the path where the Data Files are and Enter upcoming link in Browser********\n')

##TODO:Get the cleaned df
df=md.getDataframe(path)

##TODO:Visualization based initializations
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True


##TODO:Initial page layouts and URLs
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

##TODO:Layout for Menu page
index_page = html.Div([
    html.H1('Visualization of QA Results',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '33px','fontColor': 'black','textAlign': 'center'}),
    html.Div([html.Img(
            src='static/holoplot2.png',
            style={
                'height': '50%',
                'width': '50%'
            })], 
    style={"float":"right",'textAlign': 'right'}),
    html.H4('Menu',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '28px','fontColor': 'black'}),
    dcc.Link('1.Visualize based on date', href='/visualize_basedon_date',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    dcc.Link('2.Visualize based on Serial Number', href='/visualize_basedon_serial_number',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    dcc.Link('3.Visualize the Summary date', href='/visualize_summary_data',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
])


##TODO:Layout for Date picker page
visualize_basedon_date = html.Div([
    html.H1('Visualization of QA Results',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '33px','fontColor': 'black','textAlign': 'center'}),
    html.Div([html.Img(
            src='static/holoplot2.png',
            style={
                'height': '50%',
                'width': '50%'
            })], 
    style={"float":"right",'textAlign': 'right'}),
    html.H4('Menu',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '28px','fontColor': 'black'}),
    dcc.Link('1.Visualize based on Serial Number', href='/visualize_basedon_serial_number',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    dcc.Link('2.Visualize the Summary date', href='/visualize_summary_data',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    dcc.Link('Go back to Menu page', href='/',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    html.Div([html.P('Choose a date ..',style={'font-family': 'Arial', 'font-style': 'italic','font-size': '15px','margin-left': '150px'}),
    dcc.DatePickerSingle(id='my-date-picker-single',min_date_allowed=dt(2018, 8, 15),max_date_allowed=dt(2019, 10, 20),initial_visible_month=dt(2018, 8, 21),date=str(dt(2018, 8, 21, 23, 59, 59)),style={'font-family': 'Arial','width':'75%','display': 'block', 'cursor': 'pointer', 'margin-right': '40px','margin-left': '150px'})]),
    dcc.Graph(id='availability_graph'),
])


##TODO:Layout for dropdown page
visualize_basedon_serial_number= html.Div([
    html.H1('Visualization of QA Results',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '33px','fontColor': 'black','textAlign': 'center'}),
    html.Div([html.Img(
            src='static/holoplot2.png',
            style={
                'height': '50%',
                'width': '50%'
            })], 
    style={"float":"right",'textAlign': 'right'}),
    html.H4('Menu',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '28px','fontColor': 'black'}),
    dcc.Link('1.Visualize based on date', href='/visualize_basedon_date',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    dcc.Link('2.Visualize the Summary date', href='/visualize_summary_data',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    dcc.Link('Go back to Menu page', href='/',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.P('Specify a Serial Number..',style={'font-family': 'Arial', 'font-style': 'italic','font-size': '15px','margin-left': '150px'}),
    dcc.Dropdown(id='availability-dropdown2',options=[{'label': i, 'value': i} for i in df.Unit_Id.unique()],placeholder='Select Serial Number',style={'font-family': 'Arial','width':'50%', 'margin-right': '40px','margin-left': '75px','display': 'inline-block'}),
    dcc.Graph(id='availability_graph2'),
])

##TODO:Layout for date picker range page
visualize_summary_data = html.Div([
    html.H1('Visualization of QA Results',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '33px','fontColor': 'black','textAlign': 'center'}),
    html.Div([html.Img(
            src='static/holoplot2.png',
            style={
                'height': '50%',
                'width': '50%'
            })], 
    style={"float":"right",'textAlign': 'right'}),
    html.H4('Menu',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '28px','fontColor': 'black'}),
    dcc.Link('1.Visualize based on date', href='/visualize_basedon_date',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    dcc.Link('2.Visualize based on Serial Number', href='/visualize_basedon_serial_number',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    dcc.Link('Go back to Menu page', href='/',style={'font-family': 'Arial', 'font-weight': 'bold','font-size': '20px'}),
    html.Br(),
    html.P('Specify the Date range..',style={'font-family': 'Arial', 'font-style': 'italic','font-size': '15px','margin-right': '40px','margin-left': '150px'}),
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt(2018, 8, 5),
        max_date_allowed=dt(2019, 8, 5),
        initial_visible_month=dt(2018, 8, 21),
        end_date=dt(2019, 8, 5)
    ,style={'font-family': 'Arial','width':'50%', 'margin-right': '40px','margin-left': '100px','display': 'inline-block'}),
    html.Center(),
    dcc.Graph(id='availability_graph3'),
])


##TODO:Pass the selected data and generate the graph for date picker
@app.callback(dash.dependencies.Output('availability_graph', 'figure'),[dash.dependencies.Input('my-date-picker-single', 'date')])


def update_output(date1):
    
    print(date1)
    if(date1):
        df=md.getDataframe(path)
        strng=pd.to_datetime(date1,format='%Y-%m-%d')
        dff=df[df['Timestamp']==strng.date()]
        xvalues=['Overall','Response','RUB+BUZZ','Polarity','THD']
        trace1 = go.Bar(
                x=xvalues,
                y=[dff['Overall'].count(), dff['Response'].count(), dff['rub+buzz'].count(),dff['Polarity'].count(),dff['thd'].count()],
                name='Total Count',
                
        )
                
        trace2 = go.Bar(
                x=xvalues,
                y=[dff['Overall'].sum(), dff['Response'].sum(), dff['rub+buzz'].sum(),dff['Polarity'].sum(),dff['thd'].sum()],
                name='GOOD')
        trace3 = go.Bar(
                x=xvalues,
                y=[dff['Overall'].count()-dff['Overall'].sum(), dff['Response'].count()-dff['Response'].sum(), 
                   dff['rub+buzz'].count()-dff['rub+buzz'].sum(),dff['Polarity'].count()-dff['Polarity'].sum(),
                   dff['thd'].count()-dff['thd'].sum()],
                   name='BAD')
        data=[trace1,trace2,trace3]

    
              
        layout=go.Layout(autosize=False,width=900,height=400,barmode='group',xaxis=dict(tickvals=xvalues))  
        fig = go.Figure(data=data, layout=layout)
        print(type(fig))
        return fig
    else:
        
        data=None
        layout=go.Layout(autosize=False,width=900,height=400)  
        fig = go.Figure(data=data, layout=layout) 
        
        return fig



##TODO: Pass the selected data and generate the graph for dropdown
@app.callback(dash.dependencies.Output('availability_graph2', 'figure'),[dash.dependencies.Input('availability-dropdown2', 'value')])

def g1(selected_dropdown_value):
    print(selected_dropdown_value)
    if(selected_dropdown_value):
        df=md.getDataframe(path)
        dff=df[df['Unit_Id']==selected_dropdown_value]
        xvalues=['Overall','Response','RUB+BUZZ','Polarity','THD']
        trace1 = go.Bar(
                x=xvalues,
                y=[dff['Overall'].count(), dff['Response'].count(), dff['rub+buzz'].count(),dff['Polarity'].count(),dff['thd'].count()],
                name='Total Count')
        trace2 = go.Bar(
                x=xvalues,
                y=[dff['Overall'].sum(), dff['Response'].sum(), dff['rub+buzz'].sum(),dff['Polarity'].sum(),dff['thd'].sum()],
                name='GOOD')
        trace3 = go.Bar(
                x=xvalues,
                y=[dff['Overall'].count()-dff['Overall'].sum(), dff['Response'].count()-dff['Response'].sum(), 
                   dff['rub+buzz'].count()-dff['rub+buzz'].sum(),dff['Polarity'].count()-dff['Polarity'].sum(),
                   dff['thd'].count()-dff['thd'].sum()],
                   name='BAD')
        data=[trace1,trace2,trace3]
        layout=go.Layout(autosize=False,width=900,height=400,barmode='group',xaxis=dict(tickvals=xvalues))  
        fig = go.Figure(data=data, layout=layout)
        print(fig)
        return fig
    else:
        data=None
        layout=go.Layout(autosize=False,width=900,height=400)  
        fig = go.Figure(data=data, layout=layout) 
        return fig


#Pass the selected data and generate the graph for date picker range
@app.callback(dash.dependencies.Output('availability_graph3', 'figure'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_graph_scatter3(start_date,end_date):   
    
    if((start_date)):
        df=md.getDataframe(path)
        dff=pd.DataFrame()
        strng1=pd.to_datetime(start_date,format='%Y-%m-%d')
        strng2=pd.to_datetime(end_date,format='%Y-%m-%d')
        
        
        dff=df[(df['Timestamp'] > strng1.date()) & (df['Timestamp'] < strng2.date())]
        
        goodSpeakers=dff['Overall'].sum()
        badSpeakers=dff['Overall'].count()-goodSpeakers
        averageBadspeakers=(badSpeakers/dff['Overall'].count()) 
        print(type(averageBadspeakers* 100))
        if(math.isnan((averageBadspeakers* 100))):
            averageBadspeakers1=0
            standardDeviation=0
        else:
            averageBadspeakers1=(averageBadspeakers* 100)
            standardDeviation=(math.sqrt((dff['Overall'].count())*averageBadspeakers * (1-averageBadspeakers)))
            
        xvalues_=['Number of Good Speakers','Number of Bad Speakers','Average Failure Rate','Standard Deviation of Failure Rate']
        trace1 = go.Bar(
                x=xvalues_,
                y=[goodSpeakers,badSpeakers,averageBadspeakers1, standardDeviation])
        
        layout=go.Layout(autosize=False,width=900,height=400,xaxis=dict(tickvals=xvalues_))  
        fig = go.Figure(data=[trace1], layout=layout)
        print(fig)
        return fig
    
    else:
        data=None
        layout=go.Layout(autosize=False,width=900,height=400)  
        fig = go.Figure(data=data, layout=layout) 
        return fig
    
    
#Link all the layouts
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/visualize_basedon_date':
        return visualize_basedon_date
    elif pathname == '/visualize_basedon_serial_number':
        return visualize_basedon_serial_number
    elif pathname == '/visualize_summary_data':
        return visualize_summary_data
        
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

#main server
if __name__ == '__main__':
    app.run_server(debug=False,port=503)
