import os
from dotenv import load_dotenv
import basilica

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")

def basilica_connection():
    connection = basilica.Connection(BASILICA_API_KEY)
    print(connection)
    return connection

if __name__ == "__main__":

    sentences = [
        "This is a sentence.",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all.",
    ]

    connection = basilica_connection()

    embeddings = list(connection.embed_sentences(sentences))

    for emb in embeddings:
        print(type(emb))
        print(len(emb))
        print(emb)
        print("------------")

    result = connection.embed_sentence("Hello World", model="twitter")
    print(type(result))
    print(len(result))
    print(result)