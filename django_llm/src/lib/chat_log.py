import pickle

class ChatLog:
    BASE_PATH = "./src/chat_logs/"

    def __init__(self, user:str):
        self.file_path = f"{self.BASE_PATH}{user}.pkl"
        self.threads

    def load(self):
        self.threads = pickle.load(self.file_path)

    def save(self):
        with open(self.file_path, "rb") as f:
            pickle.dump(self.threads, f)

    def add(self, thread:str, chat_content):
        if thread in self.threads:
            self.threads[thread].append(chat_content)
        else:
            self.threads[thread] = chat_content

    def clear(self, thread:str):
        self.threads[thread].clear()

    def delete(self, thread:str):
        del self.threads[thread]