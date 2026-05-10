from app.agents.decomposition_agent import DecompositionAgent
from app.agents.rag_agent import RAGAgent
from app.agents.critique_agent import CritiqueAgent
from app.agents.synthesis_agent import SynthesisAgent

from app.services.context_manager import ContextManager


class Orchestrator:

    def __init__(self):

        self.decomposition_agent = DecompositionAgent()

        self.rag_agent = RAGAgent()

        self.critique_agent = CritiqueAgent()

        self.synthesis_agent = SynthesisAgent()

        self.context_manager = ContextManager()

    async def run(self, context):

        # Step 1 — Task decomposition
        context = await self.decomposition_agent.run(
            context
        )

        # Step 2 — RAG retrieval
        context = await self.rag_agent.run(
            context
        )

        # Step 3 — Critique / validation
        context = await self.critique_agent.run(
            context
        )

        # Step 4 — Final synthesis
        context = await self.synthesis_agent.run(
            context
        )

        # Step 5 — Token budget management
        budget_status = self.context_manager.check_budget(
            context
        )

        context.logs.append({

            "agent": "context_manager",

            "event": "budget_check",

            "details": budget_status
        })

        return context