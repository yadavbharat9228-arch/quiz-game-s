score = 0

print("Welcome to Quiz Game!\n")

# Question 1
print("Q1: What is the capital of India?")
print("a) Mumbai  b) Delhi  c) Kolkata  d) Chennai")
ans = input("Enter answer: ")

if ans.lower() == 'b':
    print("Correct!\n")
    score += 1
else:
    print("Wrong!\n")

# Question 2
print("Q2: Which language is used for AI?")
print("a) Python  b) HTML  c) CSS  d) C")
ans = input("Enter answer: ")

if ans.lower() == 'a':
    print("Correct!\n")
    score += 1
else:
    print("Wrong!\n")

# Question 3
print("Q3: 5 + 3 = ?")
print("a) 6  b) 7  c) 8  d) 9")
ans = input("Enter answer: ")

if ans.lower() == 'c':
    print("Correct!\n")
    score += 1
else:
    print("Wrong!\n")

print("Your final score is:", score)
