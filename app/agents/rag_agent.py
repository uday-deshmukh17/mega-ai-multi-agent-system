import re

from app.core.knowledge_base import KNOWLEDGE_BASE
from app.utils.logger import create_log

class RAGAgent:

    async def run(self, context):

        query = re.sub(
            r'[^a-zA-Z0-9\s]',
            '',
            context.user_query.lower()
        )

        synonym_map = {
            "artificial intelligence": "ai",
            "ml": "machine learning",
            "dl": "deep learning",
            "llm": "large language model",
            "nlp": "natural language processing",
            "cv": "computer vision",
            "gen ai": "generative ai"
        }

        for key, value in synonym_map.items():

            query = query.replace(key, value)

        stop_words = {
            "is",
            "the",
            "a",
            "an",
            "can",
            "like",
            "what",
            "how",
            "and",
            "of",
            "to",
            "in",
            "on",
            "for",
            "with",
            "does",
            "do",
            "tell",
            "me",
            "about",
            "explain"
        }

        query_words = set(
            word for word in query.split()
            if word not in stop_words
        )

        retrieved_chunks = []

        for chunk in KNOWLEDGE_BASE:

            cleaned_content = re.sub(
                r'[^a-zA-Z0-9\s]',
                '',
                chunk["content"].lower()
            )

            cleaned_topic = re.sub(
                r'[^a-zA-Z0-9\s]',
                '',
                chunk["topic"].lower()
            )

            content_words = set(
                word for word in
                cleaned_content.split()
                if word not in stop_words
            )

            topic_words = set(
                word for word in
                cleaned_topic.split()
                if word not in stop_words
            )

            content_matches = query_words.intersection(
                content_words
            )

            topic_matches = query_words.intersection(
                topic_words
            )

            score = 0

            # Topic match gets higher priority
            score += (
                len(topic_matches) * 3
            )

            # Content match normal priority
            score += len(content_matches)

            total_matches = len(
                content_matches.union(topic_matches)
            )

            # Dynamic retrieval logic
            should_retrieve = False

            # Strong topic match
            if len(topic_matches) >= 1:

                should_retrieve = True

            # Multiple meaningful content matches
            elif score >= 3 and total_matches >= 2:

                should_retrieve = True

            if should_retrieve:

                retrieved_chunks.append({
                    "id": chunk["id"],
                    "topic": chunk["topic"],
                    "content": chunk["content"],
                    "score": score,
                    "matched_terms": list(
                        content_matches.union(topic_matches)
                    )
                })

        retrieved_chunks = sorted(
            retrieved_chunks,
            key=lambda x: x["score"],
            reverse=True
        )

        context.retrieved_chunks = retrieved_chunks[:3]

        log = create_log(
            agent="rag_agent",
            event="retrieval",
            status="success",
            details={
                "chunks_retrieved":
                len(context.retrieved_chunks),

                "tool_used":
                "advanced_keyword_overlap_retrieval"
            }
        )

        context.logs.append(log)

        return context