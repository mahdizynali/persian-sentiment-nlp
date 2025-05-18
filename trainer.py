from config import *
from tokenizer import MaZe_tokenizer

def naive_bayes(freqs, y_train):

    loglikelihood = {}
    logprior = 0

    vocab = set([pair[0] for pair in freqs.keys()])
    V = len(vocab)

    N_pos = N_neg = 0
    for (word, label), count in freqs.items():
        if label == 1:
            N_pos += count
        else:
            N_neg += count

    D = len(y_train)

    D_pos = sum(y_train)
    D_neg = D - D_pos

    logprior = np.log(D_pos / D_neg)

    for word in tqdm(vocab, desc="Calculating loglikelihood"):
        freq_pos = freqs.get((word, 1), 0)
        freq_neg = freqs.get((word, 0), 0)

        p_w_pos = (freq_pos + 1) / (N_pos + V)
        p_w_neg = (freq_neg + 1) / (N_neg + V)

        loglikelihood[word] = np.log(p_w_pos / p_w_neg)

    return logprior, loglikelihood


def naive_bayes_predict(txt, logprior=0, loglikelihood=0):

    token = MaZe_tokenizer()
    word_l = token.do_tokenize(txt)

    p = logprior

    for word in word_l:
        if word in loglikelihood:
            p += loglikelihood[word]


    return p