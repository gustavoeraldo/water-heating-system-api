from fastapi import APIRouter

from .endpoints import measurements, users

'''
V1 endpoints:
- Users
- measurements
- Control (send something to ESP)
'''

api_router = APIRouter()
api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(measurements.router, prefix="/measurements", tags=["measurements"])
