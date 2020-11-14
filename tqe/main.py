from tqe.embedding.transformer_emb import TransformerEmbedding
from tqe.similarity.cosine_similarity import CosineSimilarity


class TQE:
    def __init__(self, emb_model="LaBSE"):
        self.emb_model = emb_model

    def fit(self, lang1, lang2):

        if len(lang1) != len(lang2):
            raise Exception("The lengths of both the lists of strings must be equal")

        lang1_emb, lang2_emb = TransformerEmbedding(self.emb_model).compute_embeddings(
            lang1, lang2
        )
        cos_sim = CosineSimilarity().compute_similarity(lang1_emb, lang2_emb)
        return cos_sim
