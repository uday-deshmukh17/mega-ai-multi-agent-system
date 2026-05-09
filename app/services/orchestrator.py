from app.agents.decomposition_agent import DecompositionAgent
from app.agents.rag_agent import RAGAgent
from app.agents.critique_agent import CritiqueAgent
from app.agents.synthesis_agent import SynthesisAgent
from app.agents.compression_agent import CompressionAgent

from app.services.context_manager import ContextManager
from app.services.router import Router


class Orchestrator:

    async def run(self, context):

        decomposition_agent = DecompositionAgent()

        rag_agent = RAGAgent()

        critique_agent = CritiqueAgent()

        synthesis_agent = SynthesisAgent()

        compression_agent = CompressionAgent()

        context_manager = ContextManager()

        router = Router()

        selected_agents = router.determine_agents(
            context.user_query
        )

        if "decomposition" in selected_agents:

            context = await decomposition_agent.run(
                context
            )

        if "rag" in selected_agents:

            context = await rag_agent.run(
                context
            )

        if "critique" in selected_agents:

            context = await critique_agent.run(
                context
            )

        if "synthesis" in selected_agents:

            context = await synthesis_agent.run(
                context
            )

        if "compression" in selected_agents:

            context = await compression_agent.run(
                context
            )

        budget_status = context_manager.check_budget(
            context
        )

        context.logs.append({

            "agent": "context_manager",

            "event": "budget_check",

            "details": budget_status
        })

        return context