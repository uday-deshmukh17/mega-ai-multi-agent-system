from app.utils.logger import create_log
from app.services.tool_manager import ToolManager

class RAGAgent:

    async def run(self, context):

        tool_manager = ToolManager()

        tool_response = await tool_manager.execute_tool(
            "web_search",
            context.user_query
        )

        retrieved = []

        if tool_response.success:

            retrieved = tool_response.result

        context.retrieved_chunks = retrieved

        log = create_log(
            agent="rag_agent",
            event="retrieval",
            status="success",
            details={
                "chunks_retrieved": len(retrieved),
                "tool_used": "web_search"
            }
        )

        context.logs.append(log)

        return context