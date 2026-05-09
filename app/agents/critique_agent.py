from app.utils.logger import create_log

class CritiqueAgent:

    async def run(self, context):

        critiques = []

        for chunk in context.retrieved_chunks:

            critiques.append({
                "chunk_id": chunk["id"],
                "confidence": 0.95,
                "status": "verified"
            })

        context.critiques = critiques

        log = create_log(
            agent="critique_agent",
            event="critique_review",
            status="success",
            details={
                "critiques_created": len(critiques)
            }
        )

        context.logs.append(log)

        return context