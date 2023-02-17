import spacy
nlp = spacy.load('en_core_web_md')

# Similarity using SpaCy
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print()

# Working with vectors
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print()

# Working with sentances
sentence_to_compare ="Why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car",
"I\'ve lost my car in my car","I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence +" - ",similarity)

# Comments on results
""" It was interesting that the monkey was similar to the bananna at 0.40
which would make sense being Monkeys eat banannas 

Interestingly I changed them to cat, dog and mouse. Cat and mouse was similar to Monkey and Banana but Cat and Dog was a stronger similarity at 0.82      

Using 'en_core_web_sm' gave significantly lower similarity scores compared with 'en_core_web_md' """