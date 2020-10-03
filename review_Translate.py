from googletrans import Translator
import re


def translate(sentence):
    trans = Translator()
    result = trans.translate(sentence, dest='en')
    return result.text


def preprocess(review_all):
    review_cleaned = []
    for review in review_all:
        # regex
        sentence = review.replace('\n', ' ')
        sentence = re.sub('[-_~=+,#/?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>\{\}`\'…》]', '', sentence)
        sentence = re.compile('[0-9|ㄱ-ㅎ|ㅏ-ㅣa-z|A-Z]+').sub('', sentence)
        sentence = re.sub(' +', ' ', sentence)
        sentence = sentence.strip()
        # translate
        # sentence = translate(sentence)
        # save
        review_cleaned.append(sentence)

    return review_cleaned
