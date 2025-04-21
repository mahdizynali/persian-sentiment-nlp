from config import *

class Numpy_Trainer:
    def __init__(self, freqs, learning_rate=LEARNING_RATE, num_classes=CLASSES, num_iters=ITRATION):
        self.freqs = freqs
        self.lr = learning_rate
        self.num_classes = num_classes
        self.num_iters = num_iters
        self.vocab = self.build_vocab()
        self.weights = np.zeros((self.num_classes, len(self.vocab)))

    def build_vocab(self):
        '''ساخت دایره لغات منحصر'''
        vocab = set()
        for word, _ in self.freqs.keys():
            vocab.add(word)
        return list(vocab)

    def extract_features(self, tweet, tokenizer):
        x = np.zeros(len(self.vocab))
        tokens = tokenizer.do_tokenize(tweet)
        for token in tokens:
            if token in self.vocab:
                idx = self.vocab.index(token)
                x[idx] += 1
        return x

    def softmax(self, z):
        e_z = np.exp(z - np.max(z))
        return e_z / e_z.sum(axis=0)
    
    def train(self, X, y, tokenizer):
        for i in range(self.num_iters):
            
            for tweet, label in tqdm(zip(X, y), total=len(X), desc=f"Epoch {i+1}/{self.num_iters}"):
                x = self.extract_features(tweet, tokenizer)
                z = np.dot(self.weights, x)
                y_hat = self.softmax(z)

                y_true = np.zeros(self.num_classes)
                y_true[label] = 1

                gradient = np.outer((y_hat - y_true), x)

                self.weights -= self.lr * gradient

            if i % 10 == 0 or i == self.num_iters - 1:
                print(f"Iteration {i+1} completed.")

    def predict(self, tweet, tokenizer):
        x = self.extract_features(tweet, tokenizer)
        z = np.dot(self.weights, x)
        y_hat = self.softmax(z)
        return np.argmax(y_hat)