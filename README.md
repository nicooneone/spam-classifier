#Spam Classifier

A Naive Bayes spam filter built from scratch in pure Python, with no external libraries. Given a text message, it decides whether the message is spam or ham (ham meaning a normal, non-spam message).

#How it works

Naive Bayes is a machine learning algorithm that learns from labeled examples. The model is trained on thousands of messages that are already marked as spam or ham, and it learns which words tend to show up in each.

Training is counting. For every word in the training messages, the model counts how many times it appeared in spam and how many times it appeared in ham. It also counts how many messages and how many total words belong to each class.

Classifying is scoring. To classify a new message, the model calculates two scores: one for spam and one for ham. Each score starts with the fraction of training messages in that class, then gets multiplied by the probability of each word in the message appearing in that class. Whichever score is higher wins.

What matters is how a word's frequency in spam compares to its frequency in ham. A word like "you" shows up in both, so it barely moves the scores. A word like "claim" shows up almost only in spam, so it pushes a message strongly toward spam.

Smoothing. If a word never appeared in one class (for example, "lunch" in spam), its probability would be 0, and multiplying by 0 wipes out the entire score. To fix this, the model uses Laplace smoothing: it adds 1 to every word count and adjusts the totals to match. Unseen words get a small probability instead of ruining the score.

Why "naive"? The model assumes every word is independent of the others. That's not really true, since "free" and "prize" tend to show up together, but the algorithm works very well anyway.

##Results

The data was shuffled and split into 80% for training (4,459 messages) and 20% for testing (1,115 messages). The test messages were never seen during training.

Metric	Result
Accuracy	97.0%
Catch rate (spam recall)	92.5%
Accuracy is the percentage of test messages classified correctly.
Catch rate is the percentage of actual spam messages that the model flagged as spam.

For context: about 87% of the messages in the dataset are ham, so a "model" that always guessed ham would score about 87% accuracy while catching zero spam. Accuracy alone can be misleading, which is why the catch rate is reported too.

##How to run

No installs needed, just Python 3:

bash
python3 spam_classifier.py

The dataset file SMSSpamCollection needs to be in the same folder as the script.

##Dataset

SMS Spam Collection from the UCI Machine Learning Repository, created by Tiago A. Almeida and José María Gómez Hidalgo. It contains 5,574 SMS messages, each labeled as spam or ham.

##Functions
organize: Reads the dataset file and organizes it into a list of tuples. The first item in each tuple is the label (spam or ham), and the second is the message itself.

splitdata: Splits the data so that 80% is used to train the model and the other 20% is used to test its accuracy.

tokenize & mtoken: Tokenizing turns a message into a list of clean words: everything is lowercased, split into individual words, and stripped of punctuation. tokenize handles one message, and mtoken handles the whole list of labeled messages.

count_totalmessages: Counts how many spam messages and how many ham messages are in the training data.

count_totalwords: Counts the total number of words in spam messages and in ham messages.

train: Builds the model. It goes through the tokenized training messages and, based on each message's label, counts every word in either the spam dictionary or the ham dictionary. The first time a word is seen in a class, it's added with a count of 1; after that, its count goes up by 1 each time. It also counts the vocabulary size (the number of unique words across both classes), which is needed for smoothing.

score: Calculates how well a message fits one class. It starts with the fraction of training messages in that class, then multiplies in the smoothed probability of each word in the message.

classify: Tokenizes a message, scores it as spam and as ham, and returns whichever label scored higher.

evaluate: Tests the model on the test set. Each test message is classified and compared to its real label, which gives the accuracy and the catch rate.