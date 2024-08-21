from fasthtml.common import *
from fasthtml.fastapp import *

app, rt = fast_app(live=True)

@rt('/')
def get(): 
    return P('Hi to be here!',H1("Hello first page"),A("Next page",href='/page'))


@rt('/page')
def get():
    return P("Welcome to Another page", H1("Another page"),A("Go back",href='/'),A("Third page",href='/page1'))

@rt('/page1')
def get():
    return P("third page",H1("Third page"),A("Go back ",href='/page'))
serve()