from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.api.api_v1.api import api_router # Use this line for dev
from app.api.api_v1.api import api_router # Use this line for deployment

'''
run the project using : uvicorn app.main:app --reload
http://localhost:8000/redoc - redoc 
http://localhost:8000/docs- documentation JSON
'''

app = FastAPI()

origins = [
  'http://localhost:8080',
  'http://localhost',
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(api_router, prefix='/thermocouple_api/v1')

@app.get('/')
def home_page():
  """
  Init endpoint
  """

  return {
    "message": "backend is working!!" 
  }