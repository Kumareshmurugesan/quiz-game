Questions=["1.)40+29____?",
           "2.)50+38____?",
           "3.)100-48____?",
           "4.)499-59____?",
           "5.)66-48____?"]
length=len(Questions)
Answers=["A","B","C","D","A"]
Count=0
answer=[]
for i in range(0,length):
      print(Questions[i])
      options=["A.69 B.58 C.47 D.45",
               "A.42 B.88 C.45 D.64",
               "A.79 B.56 C.52 D.45",
               "A.79 B.38 C.45 D.440",
               "A.18 B.56 C.41 D.18"]
      print(options[i])
      P=input("Enter your answer_____.")
      answer.append(P)
      if (answer[i] == Answers[i]):
            Count= Count+1
      else:
            Count=Count
print("Your correct Answers:>>>>>",Count)
print("correct answer's....")
print(Answers)

