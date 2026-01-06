async def rate_limit_middleware(request, call_next):
    """
    Placeholder for rate limiting (Redis / API Gateway later)
    """
    return await call_next(request)
