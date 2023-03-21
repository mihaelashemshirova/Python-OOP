from typing import List
from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [c for c in self.categories if c.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, file_name: str):
        document = self.get_document(document_id)
        document.edit(file_name)

    def delete_category(self, category_id: int):
        self.categories.remove([c for c in self.categories if c.id == category_id][0])

    def delete_topic(self, topic_id: int):
        self.topics.remove([t for t in self.topics if t.id == topic_id][0])

    def delete_document(self, document_id: int):
        self.documents.remove(self.get_document(document_id))

    def get_document(self, document_id):
        return [t for t in self.documents if t.id == document_id][0]

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)
