import torch
from torch import nn
from transformers import BertJapaneseTokenizer, BertForMaskedLM


class MaskedLanguageModel(object):
    def __init__(self):
        #self.tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
        #self.model = BertForMaskedLM.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
        self.history = []

    def tokenize(self, text) -> list:
        return self.tokenizer.tokenize(text)

    """
    def predict(self, masked_input:str, top_k=5) -> list:
        tokenized_text = self.tokenize(masked_input)
        index_mask = tokenized_text.index('[MASK]')
        input_ids = torch.tensor(self.tokenizer.convert_tokens_to_ids(tokenized_text))
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(input_ids)
            predictions = outputs[0][0, index_mask].topk(top_k)
        return [self.tokenizer.convert_ids_to_tokens([index_t.item()])[0] for index_t in predictions.indices]
    """
    def predict(self, text):
        self.history.append(text)
        self.history.append('hoge')
        return self.history
    
    def clear(self,):
        self.history = []