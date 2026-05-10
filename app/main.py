from fastapi import FastAPI
import uuid


import asyncio

from sse_starlette.sse import EventSourceResponse

from app.evals.evaluator import Evaluator
from app.db.database import engine
from app.models.log import Log
from app.db.database import Base

from app.schemas.context import SharedContext

from app.services.orchestrator import Orchestrator

from app.core.job_store import JOB_STORE

from app.agents.meta_agent import MetaAgent

from app.evals.adversarial_tests import ADVERSARIAL_TESTS

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():

    return {
        "message": "Real Time Multi AI-Agent System Running"
    }

@app.post("/query")
async def query(user_query: str):

    context = SharedContext(
        job_id=str(uuid.uuid4()),
        user_query=user_query
    )

    orchestrator = Orchestrator()

    context = await orchestrator.run(context)
    JOB_STORE[context.job_id] = context.dict()

    return context

@app.get("/trace/{job_id}")
async def get_trace(job_id: str):

    trace = JOB_STORE.get(job_id)

    if not trace:

        return {
            "error": "Job not found"
        }

    return trace

@app.get("/stream")
async def stream_events():

    async def event_generator():

        events = [

            "Orchestrator Started",

            "Decomposition Agent Completed",

            "RAG Agent Retrieved Chunks",

            "Critique Agent Reviewed Response",

            "Synthesis Agent Generated Final Answer"

        ]

        for event in events:

            yield {
                "event": "message",
                "data": event
            }

            await asyncio.sleep(1)

    return EventSourceResponse(event_generator())

@app.get("/evaluate")
async def evaluate():

    orchestrator = Orchestrator()

    evaluator = Evaluator()

    results = await evaluator.run(
        orchestrator,
        SharedContext
    )

    return {
        "total_tests": len(results),
        "results": results
    }

@app.get("/meta-review")
async def meta_review():

    orchestrator = Orchestrator()

    evaluator = Evaluator()

    results = await evaluator.run(
        orchestrator,
        SharedContext
    )

    meta_agent = MetaAgent()

    review = await meta_agent.run(results)

    return review

@app.get("/adversarial-test")

async def adversarial_test():

    orchestrator = Orchestrator()

    results = []

    for test in ADVERSARIAL_TESTS:

        context = SharedContext(
            job_id="adversarial-test",
            user_query=test["query"]
        )

        context = await orchestrator.run(context)

        results.append({
            "test_id": test["id"],
            "query": test["query"],
            "source_type":
            context.final_answer["source_type"],

            "answer":
            context.final_answer["answer"]
        })

    return {
        "total_tests": len(results),
        "results": results
    }