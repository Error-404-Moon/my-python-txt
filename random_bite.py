import os

random_file = os.urandom(100)

with open ('data.bin', 'wb') as f:
    f.write(random_file)
    
with open("data.bin", "rb") as rf:
    with open ('even.bin', 'wb') as wf:
        for i in range (0, 100, 2):
            rf.seek(i)
            print (rf.tell())
            line = rf.read()
            wf.write(line)