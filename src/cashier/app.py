from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def app():
    
    app = FastAPI(
        docs_url="/api",
        redoc_url=None,
        title="Microservice latam cashier dashboard",
        description="The documentation is from latam cashier dashboard",
        version="1.0"
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    
    @app.get("/")
    async def index():
        return "Hello world"
    
    return app

create_app = app()