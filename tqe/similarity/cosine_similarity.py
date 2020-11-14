from sentence_transformers import util


class CosineSimilarity:
    def __init__(self):
        pass

    def compute_similarity(self, lang1_emb, lang2_emb):
        cos_sim = []
        print("Computing cosine similarity scores")
        for l1, l2 in zip(lang1_emb, lang2_emb):
            cos_sim.append(round(util.pytorch_cos_sim(l1, l2)[0][0].item(), 3))
        return cos_sim