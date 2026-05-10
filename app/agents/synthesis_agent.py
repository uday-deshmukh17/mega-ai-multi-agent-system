import os

from app.utils.logger import create_log
from app.services.llm_service import LLMService

class SynthesisAgent:

    async def run(self, context):

        llm_service = LLMService()

        response = await llm_service.generate(
            context.user_query,
            context.retrieved_chunks
        )

        sources = []

        for chunk in context.retrieved_chunks:

            sources.append(chunk["topic"])

        context.final_answer = {
            "answer": response["answer"],
            "sources": sources,
            "source_type": response["source_type"]
        }

        log = create_log(
            agent="synthesis_agent",
            event="answer_synthesis",
            status="success",
            details={
                "llm_used": os.getenv("MODEL_NAME"),
                "source_type": response["source_type"],
                "sources_used": sources
            }
        )

        context.logs.append(log)

        return context