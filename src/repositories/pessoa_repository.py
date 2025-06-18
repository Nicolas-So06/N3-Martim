from src.config.database import collection

def _serialize_doc(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

def create_pessoa(pessoa_data: dict):
    collection.insert_one(pessoa_data)

def find_pessoa_by_nome(nome: str):
    resultados = list(collection.find({"nome": {"$regex": nome, "$options": "i"}}))
    return [_serialize_doc(doc) for doc in resultados]

def find_pessoa_by_rua(rua: str):
    resultados = list(collection.find({"endereco.rua": {"$regex": rua, "$options": "i"}}))
    return [_serialize_doc(doc) for doc in resultados]

def find_pessoa_by_filho(nome_filho: str):
    resultados = list(collection.find({"filhos": {"$regex": nome_filho, "$options": "i"}}))
    return [_serialize_doc(doc) for doc in resultados]
