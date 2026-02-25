import random
import math
class field:
  def __init__(self,size:int,density:float):
    self.__size = size
    if density > 0.9:
      density = 0.2
    self.__density = density
    self.__field = [[0 for _ in range(size) ]for _ in range(size)]
    self.__cover = [["?" for _ in range(size) ]for _ in range(size)]
    self.__visited = []
    self.__mine_amount = int((self.__size**2)*self.__density)//2
   
    self.__undiscover_mine = self.__mine_amount
    
  def generate_field(self):
    
    amount_left = self.__mine_amount
    while amount_left > 0:
      for x in range(self.__size):
        for y in range(self.__size):
          if amount_left <= 0:
                break
          else:
            if self.__field[x][y] != "m":
              if random.randint(1,100)>99:
                self.__field[x][y] = "m"
                amount_left -= 1
              
    self.count_surround()



  def fieldArray(self):
    return self.__field

  def coverArray(self):
    return self.__cover
  
  def count_surround(self):
    for x in range(self.__size):
        for y in range(self.__size):
          mine_count = 0
          for i in range(-1,2):
            for j in range(-1,2):
              if x+i >= 0 and y+j >= 0 and x+i < self.__size and y+j < self.__size:
                
                if self.__field[x+i][y+j] == "m":
                  mine_count += 1
          
          if self.__field[x][y] != "m":
            self.__field[x][y] = mine_count 

  def showBlock(self,y,x):
    if [x,y] not in self.__visited:
      self.__visited.append([x,y])
      if self.__field[x][y] == 0:
        self.__cover[x][y] = self.__field[x][y]
        # Recursive calls for the neighbouring cells
        if x > 0:
            self.showBlock(x-1, y)
        if x < self.__size-1:
            self.showBlock(x+1, y)
        if y > 0:
            self.showBlock(x, y-1)
        if y < self.__size-1:
            self.showBlock(x, y+1)    
        if x > 0 and y > 0:
            self.showBlock(x-1, y-1)
        if x > 0 and y < self.__size-1:
            self.showBlock(x-1, y+1)
        if x < self.__size-1 and y > 0:
            self.showBlock(x+1, y-1)
        if x < self.__size-1 and y < self.__size-1:
            self.showBlock(x+1, y+1)  

    # If the cell is not zero-valued            
      if self.__field[x][y] != 0 and self.__field[x][y] != "m":
        self.__cover[x][y] = self.__field[x][y]
      
  def checkMine(self,y,x):
    if self.__field[x][y] == "m":
      return True
    else:
      return False
      
  def setFlag(self,y,x):
    self.__cover[x][y] = "f"
    if self.__field[x][y] == "m":
      self.__undiscover_mine -= 1
    if self.__undiscover_mine <= 0:
      return True
    else:
      return False
  
  def removeFlag(self,y,x):
    if self.__cover[x][y] == "f":
      self.__cover[x][y] = "?"
      self.__undiscover_mine += 1
        


class game:
  def __init__(self,size:int,diffcuity:float):
    self.__size = size
    self.__diffcuity = diffcuity
    self.field = field(self.__size,self.__diffcuity)
    self.field.generate_field()

  def start(self):
    end = False
    while not end:
      cover = self.field.coverArray()
      self.showField(cover)
      print("Please enter a coord")
      x,y = int(input("x: ")),int(input("y: "))
      option = int(input("Option 1: dig \nOption 2: flag\nOption 3: Remove Flag\nOption: "))
      if option == 1:
        if not self.field.checkMine(x,y):
          self.field.showBlock(x,y)
        else:
          print("Hit a mine")
          self.showField(self.field.fieldArray())
          break
      elif option == 2:
        result = self.field.setFlag(x,y)
        if result:
          print("You Win!!")
          break
      elif option == 3:
        self.field.removeFlag(x,y)
        
  
  def showField(self,array):
    x_array = "  "
    for l in range(len(array[0])):
      x_array += f'{l} '
    print(x_array)
    y_array = 0
    for i in array:
      row_string = f'{y_array} '
      for j in i:
        row_string += f'{j} '
      print(row_string)
      y_array +=1
