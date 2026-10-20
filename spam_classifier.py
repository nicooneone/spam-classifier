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

tokenized = []
spam = {}
ham = {}

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

mtoken(messages)

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

ham_msgs, spam_msgs = count_totalmessages(tokenized)

print("Messages: " + str(ham_msgs), str(spam_msgs))
        
