# import spacy
# from spacy.lang.en.stop_words import STOP_WORDS
# from string import punctuation

# text = """Job placement is a service that connects employers and employees. Also known as a recruitment agency, executive search or staffing agency, job placement services have an important role in helping individuals find work. They can place individuals directly with an employer, help students find internships, support former military members in finding civilian work and offer educational services that help clients develop professional skills. For example, a recent graduate might go to a job placement agency to practice interviewing and learn how to write a resume so they can prepare for the job search process."""

# stopwords = list(STOP_WORDS)
# # print(STOP_WORDS)
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(text)
# # print(doc)
# tokens = [token.text for token in doc]
# # print(tokens)

# word_freq = {}
# for word in doc:
#     if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
#         if word.text not in word_freq.keys():
#             word_freq[word.text] = 1
#         else:
#             word_freq[word.text] += 1

# # print(word_freq)

# max_freq = max(word_freq.values())
# # print(max_freq)

# for word in word_freq.keys():
#     word_freq[word] = word_freq[word]/max_freq
#     # print(word_freq)


# sent_tokens = [sent for sent in doc.sents]
# # print(sent_tokens)

# sent_scores = {}
# for sent in sent_tokens:
#     for word in sent:
#         if word.text in word_freq.keys():
#             sent_scores[sent] = word_freq[word.text]
#         else:
#             sent_scores[sent] += word_freq[word.text]


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text = """Job placement is a service that connects employers and employees. Also known as a recruitment agency, executive search or staffing agency, job placement services have an important role in helping individuals find work. They can place individuals directly with an employer, help students find internships, support former military members in finding civilian work and offer educational services that help clients develop professional skills. For example, a recent graduate might go to a job placement agency to practice interviewing and learn how to write a resume so they can prepare for the job search process."""

stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

word_freq = {}
for word in doc:
    if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in word_freq:
            word_freq[word.text] = 1
        else:
            word_freq[word.text] += 1

max_freq = max(word_freq.values())

# Normalize word frequencies
for word in word_freq:
    word_freq[word] = word_freq[word] / max_freq

sent_tokens = [sent for sent in doc.sents]

sent_scores = {}
for sent in sent_tokens:
    for word in sent:
        if word.text in word_freq:
            if sent not in sent_scores:
                sent_scores[sent] = word_freq[word.text]
            else:
                sent_scores[sent] += word_freq[word.text]

# Print sentence scores
for sent, score in sent_scores.items():
    print(f"Sentence: '{sent.text}'\nScore: {score}\n")
