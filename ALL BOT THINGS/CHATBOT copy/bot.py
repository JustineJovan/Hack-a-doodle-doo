from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
n="no"
count=-1
History=[]
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
    Similar_Matrix=cosine_similarity(Matrix[-1],Matrix)#Gets the cosine similarity values by checking the user input with the rest of the matrix
    index=[]
    index.append(Similar_Matrix.argsort()[0][-4])#Gets the most similar answers index
    index.append(Similar_Matrix.argsort()[0][-3])
    index.append(Similar_Matrix.argsort()[0][-2])
    print(index)
    Similar_Matrix=Similar_Matrix.flatten()#making into single array
    Similar_Matrix.sort()#sorting it
    #print(Similar_Matrix)#for checking
    value=Similar_Matrix[-2]#taking the value of the closest answer
    if(value>0.2):#condition for value to be true
     while(n=="no"):
        a=index[count]
        print("Bot:",info[a],"Does this answer satisfy your question? (input:'yes' or 'no')")
        n=input("You:")
        n=n.lower()
        count=count-1
        if(n=="yes"):
         print("Bot:That's great! We can continue another chat if you want")
         continue
        if(count==-4):
           n='Not there'
           print("Bot:Could not find the answer, check 'link' to know more about the topic, We could start a new chat if you want.")
     #History=History+["Bot:",info[index]]
    else:
     print("Bot:Sorry I couldn't find an answer")
     #History=History+["Bot:",info[index]]
    info.pop() 
    n="no"
    count=-1
    user_input=input("You:")#gets input from user
    

