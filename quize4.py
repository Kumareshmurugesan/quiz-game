ques = ["2+5=?", "5*5=?", "8/2=?", "8-10=?", "5+4-3*2/1=?"]
Range = len(ques)
count = 0
correct = ["b", "a", "b", "c", "d"]
answer = []
# print(Range)
for i in range(0, Range):
    print(ques[i])
    options = ["a.25,b.7,c.52,d.7.1",
               "a.25,b.55,c.75,d.95",
               "a.82,b.4,c.0,d.0.25,",
               "a.2,b.810,c.-2,d.8",
               "a.12,b.-54,c.-3,d.8"]
    print(options[i])
    a = input("Enter your answer:")
    answer.append(a)
    #print(answer)

    if (answer[i] == correct[i]):
        count = count + 1
    else:
        count = count

print("Your total mark", count)
print("CORRECT-ANSWERS:")
print(correct)