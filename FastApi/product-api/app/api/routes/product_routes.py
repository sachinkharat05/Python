from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status
)

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from app.services.product_service import ProductService


router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)


def get_product_service(request: Request) -> ProductService:
    return request.app.state.product_service


# --------------------------------
# GET ALL PRODUCTS
# --------------------------------

@router.get("/")
def get_all_products(
    service: ProductService = Depends(get_product_service)
):

    products = service.get_all_products()

    return {
        "message": "Products retrieved successfully",
        "count": len(products),
        "data": products
    }


# --------------------------------
# GET PRODUCT BY ID
# --------------------------------

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):

    product = service.get_product(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# --------------------------------
# CREATE PRODUCT
# --------------------------------

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductResponse
)
def create_product(
    product: ProductCreate,
    service: ProductService = Depends(get_product_service)
):

    return service.create_product(
        product.model_dump()
    )


# --------------------------------
# UPDATE PRODUCT
# --------------------------------

@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    product: ProductUpdate,
    service: ProductService = Depends(get_product_service)
):

    updated = service.update_product(
        product_id,
        product.model_dump()
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return updated


# --------------------------------
# DELETE PRODUCT
# --------------------------------

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):

    deleted = service.delete_product(product_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully",
        "deleted_product": deleted
    }
    
    