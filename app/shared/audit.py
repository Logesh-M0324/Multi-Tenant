from datetime import datetime

def build_audit_log(
    action: str,
    user_id: str,
    tenant_id: str,
    metadata: dict | None = None
):
    return {
        "action": action,
        "user_id": user_id,
        "tenant_id": tenant_id,
        "metadata": metadata or {},
        "timestamp": datetime.utcnow()
    }
