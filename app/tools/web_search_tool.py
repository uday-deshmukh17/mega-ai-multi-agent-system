from app.schemas.tool_response import ToolResponse
from app.core.knowledge_base import KNOWLEDGE_BASE

class WebSearchTool:

    async def run(self, query: str):

        try:

            results = []

            query = query.lower()

            if "artificial intelligence" in query or query == "what is ai?":

                for chunk in KNOWLEDGE_BASE:

                    if "artificial intelligence" in chunk["content"].lower():

                        results.append(chunk)

            elif "machine learning" in query:

                for chunk in KNOWLEDGE_BASE:

                    if "machine learning" in chunk["content"].lower():

                        results.append(chunk)

            elif "deep learning" in query:

                for chunk in KNOWLEDGE_BASE:

                    if "deep learning" in chunk["content"].lower():

                        results.append(chunk)

            return ToolResponse(
                success=True,
                tool_name="web_search_tool",
                result=results
            )

        except Exception as e:

            return ToolResponse(
                success=False,
                tool_name="web_search_tool",
                error=str(e)
            )