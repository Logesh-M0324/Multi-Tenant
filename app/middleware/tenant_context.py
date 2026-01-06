from fastapi import Request

async def tenant_context_middleware(request: Request, call_next):
    """
    Extract tenant_id from JWT payload (if present)
    Attach it to request.state
    """
    user = getattr(request.state, "user", None)
    if user:
        request.state.tenant_id = user.get("tenant_id")
    response = await call_next(request)
    return response
