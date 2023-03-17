import frontend
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import gunicorn

app = FastAPI()


@app.get('/')
def read_root():
   return RedirectResponse("/show")

frontend.init(app)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
#run with uvicorn main:app --reload
#I want to run this via Gunicorn, but I don't know how to do it.
#gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app