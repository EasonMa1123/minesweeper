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

  def generate_field(self):
    mine_amount = int((self.__size**2)*self.__density)
    print(mine_amount)
    amount_left = mine_amount
    while amount_left > 0:
      for x in range(self.__size):
        for y in range(self.__size):
          if self.__field[x][y] != "m":
            if random.randint(1,10)>8:
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
      if self.__field[x][y] != 0:
        self.__cover[x][y] = self.__field[x][y]


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
      for i in cover:
        row_string = ""
        for j in i:
          row_string += f'{j} '
        print(row_string)
      print("Please enter a coord")
      self.field.showBlock(int(input("x: ")),int(input("y: ")))





