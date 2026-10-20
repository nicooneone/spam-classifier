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

print(tokenized)
  
        
        