from pathlib import Path
from app.models.documents import Document


class DocumentLoader:

    def __init__(self, knowledge_base_path: Path):
        self.knowledge_base_path = knowledge_base_path

    def load_documents(self) -> list[Document]:

        documents = []

        for text_file in self.knowledge_base_path.glob("*.txt"):

            content = text_file.read_text(
                encoding="utf-8"
            )

            document = Document(
                id=text_file.stem,
                source=text_file.name,
                text=content,
            )

            documents.append(document)

        return documents