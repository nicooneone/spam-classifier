import random

messages = [("spam", "WINNER! You have won a FREE prize. Claim now!"),
    ("spam", "Free entry to win $1000 cash, text WIN to 80085."),
    ("spam", "Urgent: your account has been selected for a cash reward, call now."),
    ("spam", "Congratulations, you won a free vacation! Click the link to claim."),
    ("spam", "Limited offer: get cheap loans now, no credit check, apply today."),
    ("ham",  "Hey, are we still on for lunch tomorrow?"),
    ("ham",  "Can you send me the notes from class today?"),
    ("ham",  "I'm running late, be there in ten minutes."),
    ("ham",  "Are you free this weekend? Want to grab dinner?"),
    ("ham",  "Call me when you get home, mom wants to talk."),]

def organize(dataset):

    nlist = []

    with open(dataset) as s:
        for i in s:
            
            i_s = i.strip("\n")
            i_ss = i_s.split("\t")

            newt = (i_ss[0], i_ss[1])

            nlist.append(newt)

    return nlist

messages = (organize("SMSSpamCollection"))

random.seed(42)
random.shuffle(messages)

def splitdata(messages):
    total = len(messages)
    ptotal = round(total * 0.8)

    Tlist = []
    Ulist = []

    for i in range(ptotal):
        Tlist.append(messages[i])

    for i in range(total - ptotal):
        Ulist.append(messages[i + ptotal])

    return Tlist, Ulist

train_set, test_set = splitdata(messages)

tokenized = []

def tokenize(text):
    text = text.lower()
    Ltext = text.split()

    for i in range(len(Ltext)):
                Ltext[i] = Ltext[i].strip(".,!?:")

    return Ltext

def mtoken(messages):
    for i in range(len(messages)):
        
        #Tokenize
        tok = messages[i]
        en = tok[1]
        Lfix = en.lower()

        fix = Lfix.split()

        for j in range(len(fix)):
            fix[j] = fix[j].strip(".,!?:")

        tokenized.append((tok[0], fix))

mtoken(train_set)

def count_totalmessages(tokenized):

    totalmessages_ham = 0
    totalmessages_spam = 0

    for i in range(len(tokenized)):
        temp = tokenized[i]
        
        if temp[0] == "spam":
            totalmessages_spam += 1
        else: 
            totalmessages_ham += 1

    return totalmessages_ham, totalmessages_spam

totalmessages_ham, totalmessages_spam = count_totalmessages(tokenized)

def count_totalwords(tokenized):

    totalwords_ham = 0
    totalwords_spam = 0

    for i in range(len(tokenized)):
        temp = tokenized[i]

        if temp[0] == "spam":
            totalwords_spam += len(temp[1])
        else:
            totalwords_ham += len(temp[1])

    return totalwords_ham, totalwords_spam

totalwords_ham, totalwords_spam = count_totalwords(tokenized)

def train(tokenized):
    
    spam = {}
    ham = {}
    vocab_size = 0

    for i in range(len(tokenized)):

        temp = tokenized[i]
        mes = temp[1]
        
        if temp[0] == "spam":
           for j in range(len(temp[1])):
    
               if mes[j] not in spam:
                   if mes[j] not in ham:
                        vocab_size += 1
                   spam[mes[j]] = 1
               else:
                   spam[mes[j]] += 1
        else:
            for k in range(len(temp[1])):
               
                if mes[k] not in ham:
                    if mes[k] not in spam:
                        vocab_size += 1
                    ham[mes[k]] = 1
                else:
                    ham[mes[k]] += 1

    return ham, spam, vocab_size

ham, spam, vocab_size = train(tokenized)
            
def score(messages, word_counts, total_words, class_messages, total_messages, vocab_size):
    
    score1 = 1
    final_score = 0
    
    for word in messages:
        
        if word in word_counts: 
            score1 = ((word_counts[word] + 1)/(total_words + vocab_size)) * score1
        else:
            score1 = (1/(total_words + vocab_size)) * score1
    
    final_score = (class_messages/total_messages) * score1

    return final_score

def classify(your_message, spam, ham, totalmessages_spam, totalmessages_ham, totalwords_ham, totalwords_spam, vocab_size):
    
    your_message = tokenize(your_message)

    total_messages = totalmessages_spam + totalmessages_ham

    spam_score = score(your_message, spam, totalwords_spam, totalmessages_spam, total_messages, vocab_size)
    ham_score = score(your_message, ham,  totalwords_ham,  totalmessages_ham,  total_messages, vocab_size)

    if spam_score > ham_score:
        return "spam"
    else:
        return "ham"

def evaluate(test_list, spam, ham, totalmessages_spam, totalmessages_ham, totalwords_ham, totalwords_spam, vocab_size):

    accurate = 0
    accuracy = 0.0
    catch_rate = 0.0
    
    caught_spam = 0
    caught_ham = 0

    actual_spam = 0
    actual_ham = 0
    
    for i in range(len(test_list)):
        temp = test_list[i]
        Iclass = classify(temp[1], spam, ham, totalmessages_spam, totalmessages_ham, totalwords_ham, totalwords_spam, vocab_size)

        if temp[0] == "spam":
            actual_spam +=1
        else:
            actual_ham += 1
        
        if Iclass == "spam" and temp[0] == "spam":
            caught_spam += 1
        elif Iclass == "ham" and temp[0] == "ham":
            caught_ham += 1

        accurate = caught_ham + caught_spam

    accuracy = accurate/len(test_list)

    catch_rate = caught_spam/actual_spam

    return accuracy, catch_rate

accuracy, catch_rate = evaluate(test_set, spam, ham, totalmessages_spam, totalmessages_ham, totalwords_ham, totalwords_spam, vocab_size)

print(f"Accuracy: {accuracy:.1%}")
print(f"Catch Rate: {catch_rate:.1%}")

#print(classify("Win free money", spam, ham, totalmessages_spam, totalmessages_ham, totalwords_ham, totalwords_spam, vocab_size))     
