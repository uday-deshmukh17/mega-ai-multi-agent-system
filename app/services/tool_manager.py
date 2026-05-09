from app.tools.web_search_tool import WebSearchTool
from app.tools.python_tool import PythonExecutionTool

class ToolManager:

    def __init__(self):

        self.web_tool = WebSearchTool()

        self.python_tool = PythonExecutionTool()

    async def execute_tool(
        self,
        tool_name,
        input_data
    ):

        retries = 2

        for attempt in range(retries):

            try:

                if tool_name == "web_search":

                    response = await self.web_tool.run(input_data)

                elif tool_name == "python":

                    response = await self.python_tool.run(input_data)

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