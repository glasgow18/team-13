import nltk
import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vuedj.settings')

import django
django.setup()

from chatbot.models import Service

import inquirer

from nltk.stem.lancaster import LancasterStemmer

nltk.download('punkt')
stemmer = LancasterStemmer()

with open('intents.json') as json_data:
    intents = json.load(json_data)

words = []
classes = []
documents = []
ignore_words = ['?']
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# remove duplicates
classes = sorted(list(set(classes)))

# print (len(documents), "documents")
# print (len(classes), "classes", classes)
# print (len(words), "unique stemmed words", words)




training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)

# create train and test lists
train_x = list(training[:,0])
train_y = list(training[:,1])

# reset underlying graph data
tf.reset_default_graph()
# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
# Start training (apply gradient descent algorithm)
model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save('model.tflearn')


def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

model.load('./model.tflearn')

# create a data structure to hold user context
context = {}

ERROR_THRESHOLD = 0.6
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list

def response(sentence, userID='123', get_details=True):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    contextout = ""
                    tagout = ""
                    if 'context_set' in i:
                        if get_details: contextout = ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if get_details: tagout = ('tag:', i['tag'])
                        # a random response from the intent
                        return (random.choice(i['responses']), tagout, contextout)

            results.pop(0)

#response("I want to make new friends")


def tagcheck(taglist):
    # matches the tags with services in models
    check = ""
    message = ""
    d = Service.objects.filter(tags__tag__icontains=taglist[0][1]).values('description')
    l = Service.objects.filter(tags__tag__icontains=taglist[0][1]).values('link')
    des = d[0]['description']
    link = l[0]['link']
    if des != "":
      check = "true"
    message += "There is a " + des + " in your area! For more information click: " + link
    message += "\nI hope you found this useful. Feel free to come again with more requests! Goodbye!"
    # return: check, message
    return check, message


#print("Hey there! What brings you to Health in Mind today? ")
userin = input("Hey there! What brings you to Health in Mind today? ")
tags = []
location = []
agegroup = []
responseout, tag, context = response(userin)
print(responseout)
tags.append(tag)
print("We offer a range of services in different locations and for different age groups.")
# questions = [
#   inquirer.List('size',
#                 message="Where do you live?",
#                 choices=["Edinburgh", "Scottish Borders", "Midlothian", "West Lothian", "East Lothian", "other"],
#             ),
# ]
# location = inquirer.prompt(questions)
# location = (location["size"])
location = input("Which city do you live in? ")
agegroup = input("What is your age? ")
while(True):
  #tag check function in from modles
  servicematch, message = tagcheck(tags)
  if(servicematch != ""):
    print(message)
    #confirm = {
    #   inquirer.Confirm('confirmed',
    #                  message="Is there anything else I could help you with?" ,
    #                  default=True),
    # }
    # confirmation = inquirer.prompt(confirm)
    # userin == (confirmation["confirmed"])
    # print ("Happy to help, bye.")
    break;

  userin = input("Could you tell me more? ")
  responseout, tag, context = response(userin)
  print(responseout)
  tags.append(tag)
