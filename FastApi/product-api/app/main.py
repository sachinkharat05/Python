from fastapi import FastAPI

from app.api.routes.product_routes import router as product_router
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService


app = FastAPI(
    title="Product API",
    description="Product Management REST API",
    version="1.0"
)


# Create shared application dependencies
repository = ProductRepository()

app.state.product_service = ProductService(repository)


# Register API routes
app.include_router(product_router)


@app.get("/")
def home():
    return {
        "application": "Product API",
        "message": "Welcome to Product REST API",
        "docs": "/docs"
    }


#__pycache__ stores compiled Python bytecode
#to help Python run/import files faster.