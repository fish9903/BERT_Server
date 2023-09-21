from sentence_transformers import SentenceTransformer, util
import numpy as np

class SBERT():
    def __init__(self):
        self.embedder = SentenceTransformer("jhgan/ko-sroberta-multitask")

    def analysis(self, corpus, comments):
        corpus_embeddings = self.embedder.encode(corpus, convert_to_tensor=True)

        # 댓글과 연관된 뉴스 기사의 상위 3개 문장 선택
        top_k = 3
        for query in comments:
            query_embedding = self.embedder.encode(query, convert_to_tensor=True)
            cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
            cos_scores = cos_scores.cpu()

        # score 측정
        top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
        print("\n\n======================\n\n")
        print("Comment:", query)
        print("\nTop {} most similar sentences in corpus:".format(top_k))

        result = {'text':[], 'score':[]}
        for idx in top_results[0:top_k]:
            result['text'].append(corpus[idx].strip())
            result['score'].append(round(float(cos_scores[idx]), 4))
            print(corpus[idx].strip(), "(Score: %.4f)" % (cos_scores[idx]))
        
        return result