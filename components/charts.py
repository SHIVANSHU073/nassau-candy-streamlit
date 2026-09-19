import plotly.express as px
def bar(df,x,y,title,**kwargs): return px.bar(df,x=x,y=y,title=title,**kwargs)
def line(df,x,y,title,**kwargs): return px.line(df,x=x,y=y,title=title,**kwargs)
