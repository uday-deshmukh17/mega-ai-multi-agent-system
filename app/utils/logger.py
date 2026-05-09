from datetime import datetime
import uuid

def create_log(
    agent: str,
    event: str,
    status: str,
    details: dict = {}
):

    return {
        "log_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "agent": agent,
        "event": event,
        "status": status,
        "details": details
    }