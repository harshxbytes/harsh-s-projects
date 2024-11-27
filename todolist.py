print("Let's move one step forward toward the destiny --Note your to do here and do it ")
print("Enter which are those activities you have to hit today (kindly seprate it with commas and when you complete the to do please write \"done\" at the end)")
todolist = []
for i in range (1,50):
    work = str(input(f"enter your {i} to do of this day:- "))
    if work.upper() == "DONE":
        break
    todolist.append(work)
print("you have to try to complete these stuff today")
for j in todolist:
    print(j)
print("have you completed any of your to do if yes then write c down as remove those all from to do and get a fresh list of it and if you have not completed any write n")
complete = str(input("write here --"))

if complete.upper() == "C":
    for k in range(1,len(todolist)):
        enter=int(input("enter the number of that to do you have completed(write 0 at the end):- "))
        ink = int(enter) - 1
        
        if enter == 0 :
            break
        todolist.pop(ink)
elif complete.upper() == "N":
    print("i hope you will complete all the work ")

for t in todolist :
    print(t)