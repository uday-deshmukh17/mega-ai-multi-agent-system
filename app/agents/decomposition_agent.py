from app.utils.logger import create_log

class DecompositionAgent:

    async def run(self, context):

        context.subtasks = [
            {
                "id": 1,
                "task": f"Research query: {context.user_query}",
                "depends_on": []
            }
        ]

        log = create_log(
            agent="decomposition_agent",
            event="task_decomposition",
            status="success",
            details={
                "query": context.user_query,
                "subtasks_created": 1
            }
        )

        context.logs.append(log)

        return context