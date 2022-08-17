import time
import random
start_time = time.time()
print("Let us practise multiplication tables.")
print(" ")
correct = 0
flag = False
while flag == False:
    correct = 0
    print("Supply the answers to the following 5 questions:")
    for i in range(1, 6):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        result = num1 * num2
        answer = int(input(str(num1) + " x " + str(num2) + " = "))
        if result != answer:
            print("***Incorrect***")
        else:
            print("***Correct***")
            correct += 1
    end_time = time.time()
    total_time = end_time - start_time
    total_time = round(total_time, 1)
    print(" ")
    print("Your score is " + str(correct) + " out of 5")
    print(" ")
    print("The total time it took you to answer the session questions, is " + str(total_time) + " seconds")
    print("======================================================")
    another = input("Would you like to do another session? y/n: ")
    if another.lower() == "n":
        flag = True
        stop = input("Press enter to stop")
    else:
        print(" ")
