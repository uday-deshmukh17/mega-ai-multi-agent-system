from app.utils.logger import create_log

class CompressionAgent:

    async def run(self, context):

        if len(context.final_answer.split()) > 10:

            compressed = (
                context.final_answer[:100]
                + "..."
            )

            context.final_answer = compressed

            log = create_log(
                agent="compression_agent",
                event="context_compression",
                status="success",
                details={
                    "compression_applied": True
                }
            )

            context.logs.append(log)

        return context