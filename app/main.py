from fastapi import FastAPI
from app.routes import router
from app.utils import ensure_data_file_exists

app = FastAPI()

'''
Ensure the data file exists before the application starts.
'''
ensure_data_file_exists()

'''
Include the routes defined in the router.
'''
app.include_router(router)