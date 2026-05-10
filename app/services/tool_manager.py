from app.tools.web_search_tool import WebSearchTool
from app.tools.python_tool import PythonExecutionTool

class ToolManager:

    def __init__(self):

        self.web_tool = WebSearchTool()

        self.python_tool = PythonExecutionTool()

    def select_tool(
        self,
        query
    ):

        query = query.lower()

        # Web-search style queries
        if (
            "latest" in query
            or "news" in query
            or "today" in query
            or "current" in query
        ):

            return "web_search"

        # Python/calculation style queries
        elif (
            "calculate" in query
            or "python" in query
            or "code" in query
            or "sum" in query
        ):

            return "python"

        # Default knowledge-base retrieval
        else:

            return "knowledge_base"

    async def execute_tool(
        self,
        tool_name,
        input_data
    ):

        retries = 2

        for attempt in range(retries):

            try:

                if tool_name == "web_search":

                    response = await self.web_tool.run(
                        input_data
                    )

                elif tool_name == "python":

                    response = await self.python_tool.run(
                        input_data
                    )

                else:

                    return {
                        "success": False,
                        "error": "Unknown tool"
                    }

                response.retry_count = attempt

                if response.success:

                    return response

            except Exception as e:

                if attempt == retries - 1:

                    return {
                        "success": False,
                        "error": str(e)
                    }