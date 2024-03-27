import os
from pathlib import Path
from .custom_reader import CustomPDFReader
from langchain_community.chat_models import ChatOpenAI
from llama_index.core.service_context import ServiceContext
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.indices.loading import load_index_from_storage


class ChatAgent:
    def __enter__(self):
        if os.path.exists("./storage"):
            storage_context = StorageContext.from_defaults(persist_dir="./storage")
            self.index = load_index_from_storage(storage_context)
        else:
            storage_context = StorageContext.from_defaults(persist_dir="./storage")
            index = load_index_from_storage(storage_context)

    def __exit__(self, exc_type, exc_value, traceback):
        self.index.storage_context.persist()

    def add_new_documents(self, document_paths):
        for i, path in enumerate(document_paths):
            with open(os.path.join(path), "rb") as f:
                documents = CustomPDFReader().load_data(file=Path(f.name))

                llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
                #self.service_context = ServiceContext.from_defaults(llm=llm)

                for document in documents:
                    self.index.insert(document)
                            

    def add_new_document(self, document_path):
        with open(os.path.join(document_path), "rb") as f:
            documents = CustomPDFReader().load_data(file=Path(f.name))

            llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
            #self.service_context = ServiceContext.from_defaults(llm=llm)

            for document in documents:
                self.index.insert(document)
                            

    def chat(self):
        pass