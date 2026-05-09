class Router:

    def determine_agents(
        self,
        query: str
    ):

        query = query.lower()

        agents = [

            "decomposition",
            "rag",
            "synthesis"
        ]

        if (
            "compare" in query
            or "analyze" in query
            or "critique" in query
        ):

            agents.append("critique")

        if (
            "long" in query
            or "detailed" in query
        ):

            agents.append("compression")

        return agents