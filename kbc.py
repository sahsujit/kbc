print("Welcome to my KBC program")
questions=[
   [
    "Where is janki temple located?","kathmandu", "Dharan", "pokhara", "Janakpur",4
   ],
   [
    "When is pi day celebrated around the world?","march 7", "march 9", "march 14", "march 10",3
   ],
   [
    "How many digits does the value of pi have?","7", "Infinite", "22", "4",2
   ],
   [
    "where is phasupatinath temple located?","Kathmandu", "dharan", "pokhara", "janakpur",1
   ],
   [
    "What is the only number that has letters in alphabetical order?","four", "forty", "thirty", "twelve",2
   ],
   [
    "Which country does volleybal originate form?","China", "India", "USA", "England",3
   ],
   [
    "What is the average life of RBC?","15 days", "50 days", " 120 days", "130 days",3
   ],
   [
    "How many bones are there in the face?","14", "10", "13", "15",1
   ],
   [
    "During which year did World War I begin?","1814 A.D", "1914 A.D", "1918 A.D", "1915 A.D",2
   ],
   [
    "How many years did it take to build the Taj Mahal?","5", "10", "20", "21",3
   ],
   [
    "Which animal is having the longest pregnancy period?","Lion", "Elephant", "Cow", "monkey",2
   ],
   [
    "which is the latest window?","Xp", "10", "12", "11 pro",4
   ],
   [
    "which was abacus invented?","USA", "China", "Russia", "India",2
   ],
   [
    "which is the hottest place in Nepal?","Kathmandu", "pkhara", "Manang", "Nepalgung",4
   ],
   [
    "Which country Mt.Everest located?","china", "USA", "Russia", "Nepal",4
   ],
   [
    "which is the bigest country in the word?","USA", "Russia", "India", "china",2
   ],
   [
    "What is the total sum of number 1to60?","820", "840", "900", "1830",4
   ],
   [
    "Who is the director of 3 idiots movie?","Rohit shetti", "Karan johar", "S.Shankar", "Rajkumar Hirani",4
   ],
   [
    "which gas found in fluroscent lamp?","Hydrogen", "Argon", "Mercury", "Nitrogen",3
   ],
   [
    "she'd rather repeat the lessson,    ?","wouldn't she", "will she", "shall she", "won't she",1
   ],
   [
    "which date is the international womans day celebrated?","8 january", "9 march", "8 may", "8 march",4
   ],
   ]
levels=[1000,2000,4000,6000,8000,10000,15000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
money=0
for i in range(0, len(questions)):
    question=questions[i]
    print(f"question for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"a.{question[1]}            b.{question[2]}")
    print(f"c.{question[3]}            d.{question[4]}")
    reply=int(input("Enter your answer: "))
    if (reply==question[-1]):
      print(f"correct answer,you have won Rs. {levels[i]}")
      if(i==4):
         money=8000
      elif(i==9):
         money=40000
      elif(i==21):
         money=100000
    else:
       print(f"wrong answer,you have loss Rs. {levels[i]}")
       break
print(f"you take home money is {money}")
