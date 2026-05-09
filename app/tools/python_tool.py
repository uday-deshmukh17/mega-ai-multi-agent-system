from app.schemas.tool_response import ToolResponse

class PythonExecutionTool:

    async def run(self, code: str):

        try:

            local_scope = {}

            exec(code, {}, local_scope)

            return ToolResponse(
                success=True,
                tool_name="python_execution_tool",
                result=local_scope
            )

        except Exception as e:

            return ToolResponse(
                success=False,
                tool_name="python_execution_tool",
                error=str(e)
            )