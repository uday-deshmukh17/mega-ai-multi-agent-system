from app.utils.logger import create_log

class MetaAgent:

    async def run(self, evaluation_results):

        failed_tests = []

        for result in evaluation_results:

            if not result["passed"]:

                failed_tests.append({

                    "test_id": result["test_id"],

                    "query": result["query"],

                    "suggestion":
                    "Improve retrieval quality"
                })

        log = create_log(
            agent="meta_agent",
            event="self_improvement_review",
            status="success",
            details={
                "failed_tests": len(failed_tests)
            }
        )

        return {
            "failures": failed_tests,
            "log": log
        }