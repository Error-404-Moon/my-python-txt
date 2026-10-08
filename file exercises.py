import os 
file = "C:/Users/Home/Exercise_one.txt"
file1 = "C:/Users/Home/Exercise_two.txt"
file2 = "C:/Users/Home/Exercise_three.txt"
file3 = "C:/Users/Home/Exercise_four.txt"
file4 = "C:/Users/Home/Exercise_five.txt"
answer_list = ['yes', 'no', 'no', 'no','yes', 'no','yes','yes','yes', 'no','yes']
answer_file ="C:/Users/Home/answer_file.txt"
def exercise_one ():
    with open (file, 'r') as f :
        #print (f'read: \n{f.read()}')
        lines= f.readlines()
        print( f'read lines : \n{lines}')
        
def exercise_two ():
    with open (file,'a') as f:
        f.add('\nand you?')
exercise_two()
exercise_one()
def exercise_three ():
    with open (file2, 'w') as f1:
        f1.write('ali\n')
        f1.write('sara\n')
    with open (file3, 'w') as f2 :
        f2.write('taha\n')
        f2.write('omid\n')
        f2.write('mahsa\n')
    with open(file2) as f1, open(file3) as f2:
        data1 = f1.read()
        data2 = f2.read()
    with open(file4, 'w') as f3:
        f3.write(data1+data2)
exercise_three()
def answer_exercise ():
    with open (answer_file, 'w') as f:
        for answer in 