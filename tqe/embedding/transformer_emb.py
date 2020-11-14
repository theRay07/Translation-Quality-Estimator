from sentence_transformers import SentenceTransformer


class TransformerEmbedding:
    def __init__(self, emb_model):
        self.emb_model = emb_model
        self.model = SentenceTransformer(self.emb_model)

    def compute_embeddings(self, lang1, lang2):

        print("Computing embeddings for strings in list 1")
        lang1_emb = self.model.encode(
            lang1, convert_to_tensor=True, show_progress_bar=True
        )
        print("Computing embeddings for strings in list 2")
        lang2_emb = self.model.encode(
            lang2, convert_to_tensor=True, show_progress_bar=True
        )
        return lang1_emb, lang2_emb