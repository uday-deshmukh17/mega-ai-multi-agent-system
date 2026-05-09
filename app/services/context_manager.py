class ContextManager:

    def calculate_tokens(self, text: str):

        return len(text.split())

    def check_budget(
        self,
        context
    ):

        used_tokens = 0

        used_tokens += self.calculate_tokens(
            context.user_query
        )

        used_tokens += self.calculate_tokens(
            context.final_answer
        )

        remaining = (
            context.token_budget
            - used_tokens
        )

        return {
            "used_tokens": used_tokens,
            "remaining_tokens": remaining,
            "within_budget": remaining > 0
        }