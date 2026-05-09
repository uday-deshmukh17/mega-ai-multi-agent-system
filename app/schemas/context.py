from pydantic import BaseModel
from typing import List, Dict, Any

class SharedContext(BaseModel):

    job_id: str

    user_query: str

    logs: List[Dict[str, Any]] = []

    subtasks: List[Dict[str, Any]] = []

    retrieved_chunks: List[Dict[str, Any]] = []

    critiques: List[Dict[str, Any]] = []

    final_answer: str = ""

    token_budget: int = 8000