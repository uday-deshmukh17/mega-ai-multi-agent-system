import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

class LLMService:

    async def generate(
        self,
        query,
        retrieved_chunks
    ):

        if not retrieved_chunks:

            context_text = (
                "No internal knowledge base context available. "
                "Answer using general LLM knowledge."
            )

            source_type = "general_llm"

        else:

            context_text = ""

            for chunk in retrieved_chunks:

                context_text += chunk["content"] + "\n"

            source_type = "knowledge_base"

        prompt = f"""
        You are an AI assistant.

        If retrieved context exists,
        prioritize it strongly.

        If no retrieved context exists,
        answer using general knowledge
        but clearly mention that the answer
        is generated from general LLM knowledge
        and not from internal KB retrieval.

        Query:
        {query}

        Context:
        {context_text}
        """

        response = client.chat.completions.create(

            model=os.getenv("MODEL_NAME"),

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        final_answer = response.choices[0].message.content

        return {
            "answer": final_answer,
            "source_type": source_type
        }