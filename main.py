print("current leader")
print("Analyzing high scores winner data...")
f = open("high.score", "r")
scores = f.read().split("\n")
f.close()
print(scores)

highscore = 1
name = None

for rows in scores:
  data = rows.split()
  print(data)
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The Winner is",name, "with score", highscore )







































#print("Analyzing high score winner data ....")
#f = open("high.score","r")
#scores = f.read().split()
#f.close()
#print(scores)

#highscore = 1
#name = None

#for rows in scores:
  #data = rows.split()
  #print(data)
  #if data != []:
    #if int(data[1]) > highscore:
      #highscore = int(data[1])
      #name = data[0]

#print("The winner is", name, "with the score", highscore)

  







































#f = open("filenames.list","r")
#contents = f.readline().strip()
#print(contents)
#contents = f.readline().strip()
#print(contents)
#contents = f.readline().strip()
#print(contents)
#contents = f.readline().strip()
#print(contents)

#f.close()
#f = open("filenames.list","r")
#while True:
 # contents = f.readline().strip()

  #if contents == "":
   # break
  #The last line in the file will be a blank
  #We break the loop if the line read is a blank

  #print(contents)
  # Moved the print after the break so it won't output the final blank line.

#f.close()


#f = open("filenames.list","r")
#while True:
  #contents = f.readline().strip()
  #print(contents)

  #if contents == "":
    #break
  #print(contents)

#f = open("filenames.list","r")
#while True:
  #contents = f.readline().strip()
  #if contents == "":
    #break

  #else:

   #print(contents)




#f = open("filenames.list", "r")
#contents = f.read()
#f.close()

#contents = contents.split() #added split here

#print(contents)

#f = open("filenames.list","r")
#contents = f.readline()
#print(contents)

#f.close()

#f = open("filenames.list","r")
#contents = f.readline().strip()
#print(contents)
#contents = f.readline().strip()
#print(contents)
#contents = f.readline().strip()
#print(contents)
#contents = f.readline().strip()
#print(contents)

#f.close()

#f = open("filenames.list","r")
#while True:
  #contents = f.readline().strip()

  #if contents == "":
    #break
  #The last line in the file will be a blank
  #We break the loop if the line read is a blank

 # print(contents)
  # Moved the print after the break so it won't output the final blank line.

#f.close()

#f = open("filenames.list","r")
#while True:
  #contents = f.readline().strip()
  

  #if contents == "":
    #break
  #print(contents)

#f = open("filenames.list","r")
#while True:
  #contents = f.readline().strip()
  #if contents == "" :
    #break

  #print(contents)
#f = open("filenames.list", "r")
#while True:
  #contents = f.readline().strip()
  #if contents == "" : 
    #break

  #print(contents)
#import os, time
#print("Current Leader")
#print("Analyzing high scores winner data...")
#f = open("high.score", "r")
#scores = f.read().split("\n")
#f.close()
#print(scores)

#highscore = 1
#name = None

#for rows in scores:
  #data = rows.split()
  #print(data)
  #if data != []:
    #if int(data[1]) > highscore:
      #highscore = int(data[1])
      #name = data[0]

#print("The Winner is",name, "with score", highscore )
    
    