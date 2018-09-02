import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2016,1,1)
end = datetime.datetime(2018,6,9)


app = dash.Dash()

app.layout = html.Div(children=[html.Div('Symbol to graph'),
            dcc.Input(id ='input',value='',type='text'),
            html.Div(id = 'output-graph')]      
        )


@app.callback(
    Output(component_id='output-graph',component_property='children'),
    [Input (component_id='input',component_property='value')])

def update_graph(Input_data):
    start = datetime.datetime(2016,1,1)
    end = datetime.datetime(2018,6,9)


    df = web.DataReader(Input_data, 'quandl', start, end)
    #df.reset_index(inplace=True)
    #df.set_index("Date", inplace=True)
    #df = df.drop("Symbol", axis=1)

    return dcc.Graph(
        id = 'example-graph',
        figure={
            'data':[
            {'x' : df.index,'y':df.Close,'type':'line','name':Input_data},
            ],
            'layout':{
                'title': Input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)




