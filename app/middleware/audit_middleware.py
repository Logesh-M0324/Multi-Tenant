from fastapi import Request
from datetime import datetime

async def audit_middleware(request: Request, call_next):
    response = await call_next(request)

    # Placeholder for async audit logging
    audit_event = {
        "path": request.url.path,
        "method": request.method,
        "timestamp": datetime.utcnow()
    }

    # Later → push to DB / Kafka
    return response
