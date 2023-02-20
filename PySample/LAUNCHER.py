#Sample Program written by Me.
#To display my sample writting style etc;
#For all in one page in a glance without external .py 



bank = []   #data from file
counter = []    #counter, [0] for counting, [1] for founded row


###
def newLine():
    print("\n"*5)

### File
#Read
with open("data\\records.txt", "r") as data:   ##Data load into bank[]

    for i in data:
        i = i.strip("\n")
        bank.append(i.split(","))



#Write
def WriteData():
    
    with open("data\\records.txt", "w") as data:
        data.write("")

    with open("data\\records.txt", "a") as data:
        for i in bank:
            for d in i:
                print(d)
                if d != "":
                    data.write(d)
                    data.write(",")
                    
                else:
                    continue
                    
                
            data.write("\n")
        print("File Updated")
    
###Objectified Class
#Person
class Ort:
    def __init__(self, ort):
        self.place = ort

class Person(Ort):
    def __init__(self, place, name, age):
        super().__init__(place)
        self.name = name
        self.age = age

    def Describe(self):
        print(f"Person {self.name}, currently at {self.age} is living in {self.place}")


def DataMaker(name, age, place):
    newPerson = Person(place, name, age)
    newPerson.Describe()
    

        

###
#Processor
def process():
    tempData = Search(str(input("Enter the data to be search for: ")))

    print("\n")
    print(f"1. Add in new Data")
    print(f"2. Update current Data")
    print(f"3. Erase Selected Data")
    print(f"4. Describe Selected Data")
    print("Other Answer to Quit")

    choice = str(input("\nChoice: "))

    if choice == "1":
        AddOn()

    elif choice == "2":
        Update(tempData)

    elif choice == "3":
        choice = str(input("Which Data are you deleting on? #: "))
        del(bank[tempData[choice]])
        
    elif choice == "4":
        c = str(input("Which Data are you looking on? #: "))
        DataMaker(bank[tempData[c]][0],bank[tempData[c]][1],bank[tempData[c]][2])
            
    else:
        pass


#Update
def Update(tempData):
    choice = str(input("Which Data are you updating on? #: "))

    question = int(input("1. Name, 2. Age, 3.Place from, 4.All:\n"))
    
    
    if question == 1:
        bank[tempData[choice]][int(question-1)] = (x := input("Person Name: "))

    elif question == 2:
        bank[tempData[choice]][int(question-1)] = (x := input("Person Age: "))   
        
    elif question == 3:
        bank[tempData[choice]][int(question-1)] = (x := input("Person From: "))
        
    elif question == 4:
        del(bank[tempData[choice]])
        AddOn()
        
    else:
        print("Invalid choice, Restarting")

    newLine()
    print("Process complete, Restarting")


#Add New        
def AddOn():
    newData = []

    newData.append(input("Person Name: "))
    newData.append(input("Person Age: "))
    newData.append(input("Person From: "))
    
    if (choice := input(f"{newData[0]}, age {newData[1]} from {newData[2]}, confirmed? y/n:  ")) == "y":
        bank.append(newData)
        print("Data Created")
    else:
        print("Data Entry Terminated\n")
    

#Display
def TotalDisplay(): #display whole database
    newLine()
    for i in bank:
        print(i)

    
def ResultDisplay():
    count = 0
    pair = {}
    pair.clear()
    for i in counter[1:]:  #i is data row
        print("\n #"+ str(count))
        print(bank[i])
        print("data Row: "+ str(i))
        
        pair.update({str(count):i})
        count += 1
    return pair     #option no + data row No



#Search & Display
def Search(searcher):
    counter.clear() #counter reset 0
    counter.append(0) #counter reset 1
    for i in bank:
        if searcher in i:
            counter.append(counter[0])
            

        else:
            pass

        counter[0] += 1
        
    if len(counter) > 1:
        newLine()
        print(f"Total Found at data Row {counter[1:]}")
        return ResultDisplay()
    else:
        newLine()
        print("None Found")


### Run time ###

while True:
    newLine()
    print(f"1. Display All Data")
    print(f"2. Search/ Update/ Erase Data")
    print(f"3. Add On")
    print(f"4. Save and Close")


    choice = str(input("Option: "))

    if choice == "1":
        TotalDisplay()

    elif choice == "2":
        process()
        
    elif choice == "3":
        AddOn()

    elif choice == "4":
        WriteData()
        break
    else:
        print("Answer Not Found, Restarting")
    
    
        
