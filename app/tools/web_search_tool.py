from app.schemas.tool_response import ToolResponse

class WebSearchTool:

    async def run(self, query):

        return ToolResponse(

            success=True,

            tool_name="web_search_tool",

            result=(
                f"Simulated web search results "
                f"for query: {query}"
            ),

            error="",

            retry_count=0
        )