import weaviate
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self, weaviate_url: str):
        self.client = weaviate.Client(weaviate_url)
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def create_schema(self):
        schema = {
            "classes": [
                {
                    "class": "Chunk",
                    "description": "A chunk of text from a source document",
                    "vectorizer": "none",
                    "properties": [
                        {
                            "name": "content",
                            "dataType": ["text"],
                        },
                        {
                            "name": "source_id",
                            "dataType": ["int"],
                        },
                        {
                            "name": "notebook_id",
                            "dataType": ["int"],
                        },
                    ],
                }
            ]
        }
        self.client.schema.create(schema)

    def add_chunks(self, chunks: list[str], source_id: int, notebook_id: int):
        vectors = self.model.encode(chunks)
        with self.client.batch as batch:
            for i, chunk in enumerate(chunks):
                batch.add_data_object(
                    data_object={
                        "content": chunk,
                        "source_id": source_id,
                        "notebook_id": notebook_id,
                    },
                    class_name="Chunk",
                    vector=vectors[i].tolist(),
                )

    def search(self, query: str, notebook_id: int, top_k: int = 5) -> list[dict]:
        vector = self.model.encode(query).tolist()
        where_filter = {
            "path": ["notebook_id"],
            "operator": "Equal",
            "valueInt": notebook_id,
        }
        result = (
            self.client.query.get("Chunk", ["content", "source_id"])
            .with_near_vector({"vector": vector})
            .with_where(where_filter)
            .with_limit(top_k)
            .do()
        )
        return result["data"]["Get"]["Chunk"]
