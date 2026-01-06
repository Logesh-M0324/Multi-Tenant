from fastapi import HTTPException

def attach_tenant(data: dict, tenant_id: str) -> dict:
    payload = data.copy()
    payload["tenant_id"] = tenant_id
    return payload

def tenant_filter(tenant_id: str) -> dict:
    return {"tenant_id": tenant_id}

def assert_tenant(resource: dict, tenant_id: str):
    if not resource or resource.get("tenant_id") != tenant_id:
        raise HTTPException(status_code=403, detail="Tenant access denied")
