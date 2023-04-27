import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def getList():
    return [1,2,3,4]

@app.get('/contact', response_class=HTMLResponse)
def getList():
    return """
    
    <h1>Hola soy una pagina</h1>
    <p>Soy un parrafo</p>
    """

def run():
    store.getCategories()

if __name__ == '__main__':
    run()