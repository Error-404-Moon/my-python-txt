import json
statistics_dict ={}    
file = input("Enter your file adress : ")#"C:/Users/Home/files/student11.txt"
with open (file, 'r') as f:
    file_str = f.read()
    
lines = file_str.splitlines()
words = file_str.split()
count = 0

for txt in file_str :
    if not txt.isspace() :
        count += 1
        

statistics_dict['Lines'] =len(lines)
statistics_dict['words'] =len(words)
statistics_dict['characters'] =count

print(f" Lines : {len(lines)}, words : {len(words)}, characters : {count} \n count of words:\n")
    
for i in words:
    print(f"{i} : {words.count(i)}")
    statistics_dict[i] = words.count(i)

with open("C:/Users/Home/files/statistics.json", 'w') as f:
    json.dump(statistics_dict, f, indent=2)
