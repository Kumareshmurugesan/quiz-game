A=["1. What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton?",
   "2. What is the title of the first ever Carry On film made and released in 1958?"
   "3. What is the name of the biggest technology company in South Korea?"
   "4. Which singer fronted the 1970s’ pop group Showaddywaddy?"
   "5. Which now famous TV chef started cooking at the age of eight in his parents’ pub, ‘The Cricketers’, in Clavering, Essex?"]
S=len(A)
count=0
awsner=[]
correct=["1912",
 "Carry on Sergeant",
 "Samsung",
 "Dave Bartram",
 "Jamie Oliver",
 "Christian Kist"]
for i in range(0,S):
    P=input("Enter your answer_____")
    print(A[i])
    if P==correct[i]:
       print("correct good to go")
    else:
        print("wrong")


