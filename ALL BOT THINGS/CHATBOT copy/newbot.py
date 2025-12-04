from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

with open ("content.json","r") as f:
    info=json.load(f)#loads the json file data into info
    print("Bot:Ask me Questions! and if you want to end the chat enter 'quit'")
    user_input=input("You:")#gets input from user
    #print(info) #for checking
while(user_input!="exit"):
 #History=History+user_input
    info.append(user_input)#adding it to the last index of the list
    vector=TfidfVectorizer()#used for TfidfVectorizer
    Matrix=vector.fit_transform(info)#transforms the info a matrix with the number of occurences from TfidfVectorizer
    Similar_Matrix=cosine_similarity(Matrix[-1],Matrix).flatten()#Gets the cosine similarity values by checking the user input with the rest of the matrix
    
    top_indices = Similar_Matrix.argsort()[-11:-1]

    found_answer = False
    # Go through top 10 most similar paragraphs
    for idx in reversed(top_indices):
        print("Bot:", info[idx])
        n = input("Does this answer satisfy your question? (yes/no): ").lower()
        if n == "yes":
            print("Bot: Great! We can continue another chat if you want.")
            found_answer = True
            break

    if not found_answer:
        print("Bot: Could not find a good answer. Check the sources or ask differently.")

    info.pop()  # Remove user input from the list
    user_input = input("You: ")
