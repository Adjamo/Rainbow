import os
import time
import random
from colorama import Fore, Back, Style

def ad_step(my_grid):

    count_col = 0    

    next = [[0 for i in range(80)] for j in range(20)]

    #next[5][15] = 2
    #next[5][25] = 3

    for row in my_grid:
        count_row = 0
        for e in row:

            #print(count_col)

            if(my_grid[count_col][count_row] != 0):


              # 1 alergic to 3
              # 2 alergic to 1
              # 3 alergic to 2
              #dave = []
              #dave = [[1,3],[2,1],[3,2]] # rock papaer scissors

              dave = [[1,2],[2,3],[3,4],[4,5],[5,1]] # rock papaer scissors

              #dave = [[1,3],[2,1],[3,2],[4,2]]
              
              for animal in dave:

                if(my_grid[count_col][count_row] == animal[0]):#rock (red)
                  if(count_col > 0):
                    if(my_grid[count_col-1][count_row] != animal[1] and next[count_col-1][count_row] != animal[1]):
                      next[count_col-1][count_row] = animal[0]
                  else:
                    if(my_grid[19][count_row] != animal[1] and next[19][count_row] != animal[1]):
                      next[19][count_row] = animal[0]
                    
                  if(count_col < 19):
                    if(my_grid[count_col+1][count_row] != animal[1] and next[count_col+1][count_row] != animal[1]):
                      next[count_col+1][count_row] = animal[0]
                  else:
                    if(my_grid[0][count_row] != animal[1] and next[0][count_row] != animal[1]):
                      next[0][count_row] = animal[0]
                  
                  if(count_row > 0):
                    if(my_grid[count_col][count_row-1] != animal[1] and next[count_col][count_row-1] != animal[1]):
                      next[count_col][count_row-1] = animal[0]
                  else:
                    if(my_grid[count_col][79] != animal[1] and next[count_col][79] != animal[1]):
                      next[count_col][79] = animal[0]

                  if(count_row < 79):
                    if(my_grid[count_col][count_row+1] != animal[1] and next[count_col][count_row+1] != animal[1]):
                      next[count_col][count_row+1] = animal[0]
                  else:
                    if(my_grid[count_col][0] != animal[1] and next[count_col][0] != animal[1]):
                      next[count_col][0] = animal[0]


                  if(next[count_col][count_row] != animal[1] and my_grid[count_col][count_row] != animal[1]):
                    next[count_col][count_row] = animal[0]
              
              #next[count_col-1][count_row] %= 9

            else:
              #next[count_col][count_row] += 1
              pass

            count_row += 1
        count_col += 1


    return next

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        for e in row:
            
            if(e==1):print(Fore.RED + '#', end='') # end='' removes newline
            if(e==2):print(Fore.GREEN + '@', end='') # end='' removes newline
            if(e==3):print(Fore.BLUE + '%', end='') # end='' removes newline
            if(e==4):print(Fore.YELLOW + '*', end='') # end='' removes newline
            if(e==5):print(Fore.MAGENTA + '!', end='') # end='' removes newline
            if(e==6):print(Fore.CYAN + '£', end='') # end='' removes newline
            
            
            #if(e==1):print(Fore.RED + u"\u2588", end='') # end='' removes newline
            #if(e==2):print(Fore.GREEN + u"\u2588", end='') # end='' removes newline
            #if(e==3):print(Fore.BLUE + u"\u2588", end='') # end='' removes newline
            #if(e==4):print(Fore.YELLOW + u"\u2588", end='') # end='' removes newline
            #if(e==5):print(Fore.MAGENTA + u"\u2588", end='') # end='' removes newline
            #if(e==6):print(Fore.CYAN + u"\u2588", end='') # end='' removes newline
            if(e==7):print(Fore.WHITE + 'Z', end='') # end='' removes newline
            if(e==8):print(Fore.BLACK + 'Y', end='') # end='' removes newline
            if(e==9):print(Fore.RED + "X", end='') # end='' removes newline
            #print(Fore.RED + u"\u2588")
            
            #print(Fore.GREEN + u"\u2588")

            #print(Style.RESET_ALL)


            if(e==0):print(' ', end='') # end='' removes newline
            
            #print(e, end='') # end='' removes newline
        print()

def game(grid,record):

  #print_grid(grid)
  steps = 0
  old = []

  while True:
    #print_grid(grid)
  
    # add 'x' onto a master grid

    x = ad_step(grid)
    #print_grid(x)
    #x = kill_cells(x,grid)
    grid = x
    
    print()
    print()
    print_grid(x)
    print(Fore.WHITE + 'steps: ' + str(steps) )
    print(Fore.WHITE + 'record: ' + str(record) )
    
    steps += 1
    time.sleep(0.1)

    if( x in old ): # pattern is repeating
      return steps

    old.append(x)

number = 0
while True:
  # start with a random map
  col_num = 0
  row_num = 0

  grid = [[0 for i in range(80)] for j in range(20)]
  next = [[0 for i in range(80)] for j in range(20)]
  
  for row in grid:
    for e in row:
      if( 1 > random.randint(0, 50) ):
        grid[col_num][row_num] = random.randint(0, 5)# set number of colours here
      else:
        grid[col_num][row_num] = 0
      row_num += 1
    col_num += 1
    row_num = 0
    
  new_number = game(grid,number)

  if(new_number > number): # keep the record
    number = new_number

  if(number > 199):
    print('Success! A ' + str(number) + ' step pattern was found!!')
  else:
    print('A ' + str(number) + ' step pattern was found')


