import time
import random

# being able to do math fast is useful in real life :)

def math_sprint(total_questions):

    print(f"--- {total_questions} Question Sprint! ---")

    start_time = time.time()

    count = 0
    
    for i in range(1, total_questions + 1):

        num = random.randint(1, 100)
        multiplier = random.randint(1, 20) # change the multiplier here
        
        while True:
            try:
                user_input = int(input(f"{num} * {multiplier} = "))
                break
            except ValueError:
                print("please enter a number!")

        if user_input == num * multiplier:
            count += 1
            print("Correct :)")
        else:
            print(f"Incorrect, it was {num * multiplier}!")
    
    end_time = time.time()
    elapsed = end_time - start_time

    print("---Score Board---")
    print(f"Time: {elapsed: .2f} seconds")
    print(f"Correction Rate: {count / total_questions * 100} %")


math_sprint(int(input("Input the number of questions: ")))