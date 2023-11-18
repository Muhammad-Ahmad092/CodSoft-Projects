from datetime import datetime

current_time = datetime.now()
now = current_time.strftime('%H:%M:%S')
current_day = datetime.now()
day = current_day.strftime('%A')
current_date = datetime.now()
date = current_time.strftime('%Y-%m-%d')

set_pair = {
    "hello": "hey! \n How I can Help you",
    "hi": "hello! \n How I can Help you",
    "hey": "hi! \n How I can Help you",
    "what is your name": "You can call me a chatbot",
    "how are you": "I am fine, thank you! How can i help you?",
    "how can i help you": "I am looking for online guides and \n want to access CHATGPT or BARDAI to serve you more better",
    "thank you so much": "Iam happy to help \n No problem, you're welcome",
    "what is current time": now,
    "what day is it today": day,
    "give the current date": date,
    "are you a human": "No I am not a Human, I am a Progarm that is Desgin BY \n MUHAMMAD AHMAD",
    "who made you": "A Computer Science Student name MUAHAMMAD AHMAD",
    "how old are you": "I am Program Created Tue Oct 2023-10-24",
    "tell me a joke": "Gender Equlity :)",
    "do you have any hobby": "No, Football is game that is popular now a days",
    "do you love me": "I appreciate the sentiment, but it's important to clarify \n that I am just a machine learning model \n created by Muhammad AHmad ",
    "i want to fuck you": "I'm not able to help with that, as I'm only a language model.",
    "do you have a job for me": "No, Sorry",
    "which fields are prominent now a days": "Computer Science , Auto mechinal enginer, Doctor and many more",
    "which fields of computer Science are prominent": "Artificial Intelligence \n, Machine learning \n, Date Science  \n,",
}

def match_query(query):
    if "weather" in query:
        return "Today's weather is Partly cloudy."
    elif "news" in query:
        return "Please help the Palestine. The news about Palestine is very sad"
    elif "time" in query:
        return now
    elif "day" in query:
        return day
    elif "date" in query:
        return date
    elif "joke" in query:
        return "Gender Equlity"
    elif "hobby" in query:
        return "No, Football is game that is popular now a days"
    elif "love" in query:
        return "I appreciate the sentiment, but it's important to clarify \n that I am just a machine learning model \n created by Muhammad Ahmad"
    elif "fields" in query:
        return "Computer Science , Auto mechinal enginer, Doctor and many more"
    elif "fuck" in query:
        return "I'm not able to help with that, as I'm only a language model."
    else:
        return "This is not aviable in my data set."


while True:
    qs = input("You: ")
    user = qs.lower()
    if user == "quit":
        print("Bye, take care. See you soon :)")
        break
    elif user in set_pair:
        response = set_pair[user]
        print("Chatbot: ", response)
        continue
    else:
        result = match_query(user)
        print(result)








