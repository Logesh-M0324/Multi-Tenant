from fastapi import FastAPI
from lifespan import lifespan
from core.logging import setup_logging

from domains.auth.router import router as auth_router
from domains.admin.router import router as admin_router
from domains.brand.inventory.router import router as brand_inventory_router
from domains.uhni.router import router as uhni_router
from domains.consumer.router import router as consumer_router
from domains.internal.router import router as internal_router

setup_logging()

app = FastAPI(
    title="Modaglimmora Platform",
    lifespan=lifespan
)



app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(brand_inventory_router)
app.include_router(uhni_router)
app.include_router(consumer_router)
app.include_router(internal_router)

@app.get("/health")
async def health():
    return {"status": "ok"}
