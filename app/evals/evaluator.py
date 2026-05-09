from app.evals.test_cases import TEST_CASES

class Evaluator:

    async def run(self, orchestrator, context_class):

        results = []

        for test in TEST_CASES:

            context = context_class(
                job_id=f"eval-{test['id']}",
                user_query=test["query"]
            )

            context = await orchestrator.run(context)

            passed = (
                test["expected_keyword"].lower()
                in context.final_answer.lower()
            )

            results.append({

                "test_id": test["id"],

                "query": test["query"],

                "passed": passed,

                "final_answer": context.final_answer
            })

        return results