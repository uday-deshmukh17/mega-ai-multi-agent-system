from pydantic import BaseModel
from typing import Any

class ToolResponse(BaseModel):

    success: bool

    tool_name: str

    result: Any = None

    error: str = ""

    retry_count: int = 0