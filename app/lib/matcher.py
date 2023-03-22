from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# nltk.download('punkt')
# nltk.download('stopwords')

raw_text = "A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."

sentences = sent_tokenize(raw_text)

stop_words = set(stopwords.words('english'))

preprocessed_sentences = []
vocab = {}

for sentence in sentences:
    words = word_tokenize(sentence)
    result = []

    for word in words:
        word = word.lower()

        if word not in stop_words and len(word) > 2:
            result.append(word)
            if word not in vocab:
                vocab[word] = 0
            vocab[word] += 1

    preprocessed_sentences.append(result)

sorted_vocab = sorted(vocab.items(), key=lambda x: x[1], reverse=True)

word_to_index = {}

for i in range(len(sorted_vocab)):
    (word, freq) = sorted_vocab[i]
    if freq > 1: word_to_index[word] = i + 1

word_to_index['OOV'] = len(word_to_index) + 1

encoded_sentences = []
for sentence in preprocessed_sentences:
    encoded_sentence = []
    for word in sentence:
        try:
            # 단어 집합에 있는 단어라면 해당 단어의 정수를 리턴.
            encoded_sentence.append(word_to_index[word])
        except KeyError:
            # 만약 단어 집합에 없는 단어라면 'OOV'의 정수를 리턴.
            encoded_sentence.append(word_to_index['OOV'])
    encoded_sentences.append(encoded_sentence)
print(encoded_sentences)
