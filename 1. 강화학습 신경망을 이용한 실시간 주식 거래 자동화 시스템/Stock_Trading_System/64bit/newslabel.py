from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

class newslabel:
    def __init__(self, newsDf):
        self.newsDf = newsDf
        self.score = 0

    def labeling(self):
        if self.newsDf.shape[0] == 0:
            return self.score
        else:
            list_text = self.newsDf['내용'].tolist()
            newsSentences = []
            for item in list_text:
                newsSentences.extend(item.split('. '))

            tokenizer = AutoTokenizer.from_pretrained('snunlp/KR-FinBert-SC')
            model = AutoModelForSequenceClassification.from_pretrained('snunlp/KR-FinBert-SC')
            senti_classifier = pipeline(task='text-classification', model=model, tokenizer=tokenizer)

            # neutral 중립, positive 긍정, negative 부정

            for text in newsSentences:
                if senti_classifier(text)[0]['label'] == 'positive':
                    self.score += 1
                elif senti_classifier(text)[0]['label'] == 'negative':
                    self.score -= 1
                else:
                    pass
            
            # 긍정부정 비슷하게 있다면 0, 긍정적인 내용이 더 많으면 1, 부정적인 내용이 더 많으면 2
            if self.score == 0:
                self.score = 0
            elif self.score > 0:
                self.score = 1
            elif self.score < 0:
                self.score = 2

            return self.score







