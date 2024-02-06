sent_scores = {}
for sent in sent_tokens:
    for word in sent:
        if word.text in word_freq.keys():
            sent_scores[sent] = word_freq[word.text]
        else:
            sent_scores[sent] += word_freq[word.text]
