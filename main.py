# The learner

#creating first list 
file2 = open("commands.txt","r")
data2 = file2.readlines()
new_list = [item.strip() for item in data2]
cmd2= []
for i in new_list:
    cmd2.append(i)
file2.close()

#creating list 2
file1=open("output.txt","r")
data1 = file1.readlines()
new_list2 = [item.strip() for item in data1]
cmd=[]
for i in new_list2:
    cmd.append(i)
file1.close()

# making chat dictionary
res = {}
for i in cmd2:
        for j in cmd:
                res[i] = j
                cmd.remove(j)
                break


prefix=open("commands.txt","a")
out=open("output.txt","a")



    # print(res)
    # print(cmd2)
def respond(user):
  for i in res:
      if i == user:
          print("Bot:",res[i])
                


while True:
  user = str(input("You: "))
  user = user.lower()
  respond(user)
  if user not in cmd2:
      prefix.write("\n" + user)
      out.write("\n" + str(input("Bot: What to reply on this?\nYou: ")))
      prefix.close()
      out.close()
      break
   
    