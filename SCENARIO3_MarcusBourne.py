from random import randrange

class randomList:
    def __init__(self,size):
        self.__count = size
        self.__intList = []
        self.fill()
        
    def fill(self):
        for i in range(self.__count):
            self.__intList.append(randrange(100)+1)
            
    def getCount(self):
        return self.__count;
    
    def getTotal(self):
        total = 0
        for val in self.__intList:
            total += val
        return total
        
    def getAverage(self):
        return self.getTotal() / self.getCount()

    def __str__(self):
        string = ""
        for i in range(self.__count - 1):
            string += str(self.__intList[i])+", "
        string += str(self.__intList[self.__count-1])
        return string

print("Random Integer List\n")
intlist = int(input("How many integers should the list contain?: "))
menu = True

while(menu):
    numberList = randomList(intlist)
    print("\nRandom Integers")
    print(f'='*15)
    print("Integers: ",numberList)
    print("Count: ",numberList.getCount())
    print("Total: ",numberList.getTotal())
    print("Average: ",numberList.getAverage())

    choice = input("\nContinue? (y/n):")
    if(choice=='n'):
        menu = False

print("\nBye!")