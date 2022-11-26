import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase():
    def __init__(self):
        cred = credentials.Certificate("to-do-cee45-firebase-adminsdk-1b5xd-fb1a496746.json")
        self.app = firebase_admin.initialize_app(cred)

        self.db = firestore.client()
        self.read()

    def add(self, item):
        doc_ref = self.db.collection("to-do").document("to-do")

        key = str(len(self.data.keys()))
        self.data[key] = item
        
        doc_ref.set(self.data)
    
    def remove(self, key):
        key -= 1
        doc_ref = self.db.collection("to-do").document("to-do")
        
        self.data[str(key)] = None
        
        doc_ref.set(self.data)

    def read(self):
        users_ref = self.db.collection("to-do")
        docs = users_ref.stream()
        for doc in docs:
            if doc.id == "to-do":
                self.data = doc.to_dict()
                return doc.to_dict()
