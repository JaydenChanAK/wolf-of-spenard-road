#AP Computer Science Principles Final Project

#-----Import Statements-----
import random as rndm
import matplotlib.pyplot as plt

#-----Variables-----
#Prices
starting_price_max = 100
starting_price_min = 50
price_change_max = 10
price_change_min = -5

#Companies
stock_1_name = "Builders League United"
stock_1_acronym = "blu"
stock_1_price = rndm.randint(starting_price_min, starting_price_max)
old_value1 = stock_1_price
new_value1 = stock_1_price

stock_2_name = "Reliable Excavation Demolition"
stock_2_acronym = "red"
stock_2_price = rndm.randint(starting_price_min, starting_price_max)
old_value2 = stock_2_price
new_value2 = stock_2_price

stock_3_name = "Elbertson's Industrial Concern"
stock_3_acronym = "eic"
stock_3_price = rndm.randint(starting_price_min, starting_price_max)
old_value3 = stock_3_price
new_value3 = stock_3_price

stock_4_name = "Crowley's Diamond Consortium"
stock_4_acronym = "cdc"
stock_4_price = rndm.randint(starting_price_min, starting_price_max)
old_value4 = stock_4_price
new_value4 = stock_4_price

stock_5_name = "Chan's Lithium Excavation"
stock_5_acronym = "cle"
stock_5_price = rndm.randint(starting_price_min, starting_price_max)
old_value5 = stock_5_price
new_value5 = stock_5_price

#Player
initial_balance = 2000
balance = initial_balance
portfolio = 0

stock_1_stocks = 0
stock_1_portfolio = 0
stock_2_stocks = 0
stock_2_portfolio = 0
stock_3_stocks = 0
stock_3_portfolio = 0
stock_4_stocks = 0
stock_4_portfolio = 0
stock_5_stocks = 0
stock_5_portfolio = 0

#Days
current_day = 0
total_days = 10
goal = 5000

#-----Initializations-----
#clears the txt file of the stocks so that the files will be readable when new data is entered in game
clear_stock1 = open('stock_data1.txt', 'w')
clear_stock2 = open('stock_data2.txt', 'w')
clear_stock3 = open('stock_data3.txt', 'w')
clear_stock4 = open('stock_data4.txt', 'w')
clear_stock5 = open('stock_data5.txt', 'w')

#opens the txt files so new lines of data can be added each day
append_stock1 = open('stock_data1.txt', 'a+')
append_stock2 = open('stock_data2.txt', 'a+')
append_stock3 = open('stock_data3.txt', 'a+')
append_stock4 = open('stock_data4.txt', 'a+')
append_stock5 = open('stock_data5.txt', 'a+')

#values for the x or y axis of stocks 1-5. This is what is being appended to from text files to create the graph visualization
x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

#-----Functions-----
def end_day(): #changes stock prices and adds to current day counter
  global stock_1_price, stock_2_price, stock_3_price, stock_4_price, stock_5_price, current_day, total_days, balance, portfolio, old_value1, old_value2, old_value3, old_value4, old_value5, new_value1, new_value2, new_value3, new_value4, new_value5

  old_value1 = stock_1_price
  old_value2 = stock_2_price
  old_value3 = stock_3_price
  old_value4 = stock_4_price
  old_value5 = stock_5_price

  stock_1_price += rndm.randint(price_change_min, price_change_max)
  stock_2_price += rndm.randint(price_change_min, price_change_max)
  stock_3_price += rndm.randint(price_change_min, price_change_max)
  stock_4_price += rndm.randint(price_change_min, price_change_max)
  stock_5_price += rndm.randint(price_change_min, price_change_max)

  new_value1 = stock_1_price
  new_value2 = stock_2_price
  new_value3 = stock_3_price
  new_value4 = stock_4_price
  new_value5 = stock_5_price

  current_day += 1
  if current_day == total_days:
    if (balance + portfolio) >= goal:
      print("Congratulations! You have met the goal of", goal, ". You are the Wolf of Spenard Road.")
    else:
      print("You have failed to meet the goal of", goal, ". Your father is very disappointed in you.")

  update_stock_graphs()
  graph_stocks()
  
def buy(): #iniitiates buy prompt
  global balance, stock_1_price, stock_2_price, stock_3_price, stock_4_price, stock_5_price, stock_1_stocks, stock_2_stocks, stock_3_stocks, stock_4_stocks, stock_5_stocks, stock_1_portfolio, stock_2_portfolio, stock_3_portfolio, stock_4_portfolio, stock_5_portfolio

  print("Your current balance is:", balance)
  print("You have", stock_1_stocks, "stocks, worth", stock_1_portfolio, "in", stock_1_name)
  print("You have", stock_2_stocks, "stocks, worth", stock_2_portfolio, "in", stock_2_name)
  print("You have", stock_3_stocks, "stocks, worth", stock_3_portfolio, "in", stock_3_name)
  print("You have", stock_4_stocks, "stocks, worth", stock_4_portfolio, "in", stock_4_name)
  print("You have", stock_5_stocks, "stocks, worth", stock_5_portfolio, "in", stock_5_name)
  
  active_company = input("Which company would you like to buy stocks from? ")
  if active_company == stock_1_acronym:
    buy_amount = int(input("How many stocks would you like to buy? "))
    if (buy_amount*stock_1_price) > balance:
      print("You cannot afford that.")
      return
    else:
      stock_1_stocks += buy_amount
      stock_1_portfolio = stock_1_stocks * stock_1_price
      balance -= (buy_amount*stock_1_price)
      return
  elif active_company == stock_2_acronym:
    buy_amount = int(input("How many stocks would you like to buy? "))
    if (buy_amount*stock_2_price) > balance:
      print("You cannot afford that.")
      return
    else:
      stock_2_stocks += buy_amount
      stock_2_portfolio = stock_2_stocks * stock_2_price
      balance -= (buy_amount*stock_2_price)
      return
  elif active_company == stock_3_acronym:
    buy_amount = int(input("How many stocks would you like to buy? "))
    if (buy_amount*stock_3_price) > balance:
      print("You cannot afford that.")
      return
    else:
      stock_3_stocks += buy_amount
      stock_3_portfolio = stock_3_stocks * stock_3_price
      balance -= (buy_amount*stock_3_price)
      return
  elif active_company == stock_4_acronym:
    buy_amount = int(input("How many stocks would you like to buy? "))
    if (buy_amount*stock_4_price) > balance:
      print("You cannot afford that.")
      return
    else:
      stock_4_stocks += buy_amount
      stock_4_portfolio = stock_4_stocks * stock_4_price
      balance -= (buy_amount*stock_4_price)
      return
  elif active_company == stock_5_acronym:
    buy_amount = int(input("How many stocks would you like to buy? "))
    if (buy_amount*stock_5_price) > balance:
      print("You cannot afford that.")
      return
    else:
      stock_5_stocks += buy_amount
      stock_5_portfolio = stock_5_stocks * stock_5_price
      balance -= (buy_amount*stock_5_price)
      return
  elif active_company != stock_1_acronym or stock_2_acronym or stock_3_acronym or stock_4_acronym or stock_5_acronym:
    print("That is not a recognized company.")
    return
  
def sell(): #initiates sell prompt
  global balance, stock_1_price, stock_2_price, stock_3_price, stock_4_price, stock_5_price, stock_1_stocks, stock_2_stocks, stock_3_stocks, stock_4_stocks, stock_5_stocks, stock_1_portfolio, stock_2_portfolio, stock_3_portfolio, stock_4_portfolio, stock_5_portfolio

  print("Your current balance is:", balance)
  print("You have", stock_1_stocks, "stocks, worth", stock_1_portfolio, "in", stock_1_name)
  print("You have", stock_2_stocks, "stocks, worth", stock_2_portfolio, "in", stock_2_name)
  print("You have", stock_3_stocks, "stocks, worth", stock_3_portfolio, "in", stock_3_name)
  print("You have", stock_4_stocks, "stocks, worth", stock_4_portfolio, "in", stock_4_name)
  print("You have", stock_5_stocks, "stocks, worth", stock_5_portfolio, "in", stock_5_name)
  
  active_company = input("Which company would you like to sell stocks from? ")
  if active_company == stock_1_acronym:
    sell_amount = int(input("How many stocks would you like to sell? "))
    if sell_amount > stock_1_stocks:
      print("You cannot sell that much.")
      return
    else:
      stock_1_stocks -= sell_amount
      stock_1_portfolio = stock_1_stocks * stock_1_price
      balance += (sell_amount*stock_1_price)
      return
  if active_company == stock_2_acronym:
    sell_amount = int(input("How many stocks would you like to sell? "))
    if sell_amount > stock_2_stocks:
      print("You cannot sell that much.")
      return
    else:
      stock_2_stocks -= sell_amount
      stock_2_portfolio = stock_2_stocks * stock_2_price
      balance += (sell_amount*stock_2_price)
      return
  if active_company == stock_3_acronym:
    sell_amount = int(input("How many stocks would you like to sell? "))
    if sell_amount > stock_3_stocks:
      print("You cannot sell that much.")
      return
    else:
      stock_3_stocks -= sell_amount
      stock_3_portfolio = stock_3_stocks * stock_3_price
      balance += (sell_amount*stock_3_price)
      return
  if active_company == stock_4_acronym:
    sell_amount = int(input("How many stocks would you like to sell? "))
    if sell_amount > stock_4_stocks:
      print("You cannot sell that much.")
      return
    else:
      stock_4_stocks -= sell_amount
      stock_4_portfolio = stock_4_stocks * stock_4_price
      balance += (sell_amount*stock_4_price)
      return
  if active_company == stock_5_acronym:
    sell_amount = int(input("How many stocks would you like to sell? "))
    if sell_amount > stock_5_stocks:
      print("You cannot sell that much.")
      return
    else:
      stock_5_stocks -= sell_amount
      stock_5_portfolio = stock_5_stocks * stock_5_price
      balance += (sell_amount*stock_5_price)
      return
  elif active_company != stock_1_acronym or stock_2_acronym or stock_3_acronym or stock_4_acronym or stock_5_acronym:
    print("That is not a recognized company.")
    return
    
def update_portfolio(): #updates player portfolio based on stock portfolios
  global portfolio, stock_1_portfolio, stock_2_portfolio, stock_3_portfolio, stock_4_portfolio, stock_5_portfolio
  
  portfolio = stock_1_portfolio + stock_2_portfolio + stock_3_portfolio + stock_4_portfolio + stock_5_portfolio

def help(): #how to play the game
  print("You have been appointed as Interim Chief Executive of your father's investment firm. Before you are appointed to the position permanently, you are expected to achieve a goal of", goal)

  print("There are 5 companies you have been permitted to invest in:",
  stock_1_name,",", stock_2_name,",", stock_3_name,",", stock_4_name,",", stock_5_name)
  
  print(  
  """
  For the purposes of this exercise, you must refer to them by their acronym in lowercase.
  You will use this terminal to achieve your goals:
  Type buy() to begin the buying process. 
  Type sell() to begin the selling process.
  Type tell_me() to learn how many days you have left, your current balance, and your current portfolio across all companies.
  Type end_day() to move onto the next day and update the stock market.
  Type help() to see this information again.
  """)
  
  print("Your father has given you", initial_balance, "dollars and", total_days, "days to prove your worth. Good luck.")

def reset_stock_data():
  clear_stock1.close()
  clear_stock2.close()
  clear_stock3.close()
  clear_stock4.close()
  clear_stock5.close()

def update_stock_graphs():
  global stock_1_price, stock_2_price, stock_3_price, stock_4_price, stock_5_price, current_day, old_value1, old_value2, old_value3, old_value4, old_value5, new_value1, new_value2, new_value3, new_value4, new_value5

  append_stock1=open('stock_data1.txt', 'w')
  append_stock2=open('stock_data2.txt', 'w')
  append_stock3=open('stock_data3.txt', 'w')
  append_stock4=open('stock_data4.txt', 'w')
  append_stock5=open('stock_data5.txt', 'w')
  
  if current_day == 0:
    previous_day = 0
  else:
    previous_day = (current_day - 1)
  
  append_stock1.write(str(previous_day)+', '+str(old_value1)+'\n'+str(current_day)+', '+str(new_value1))
  append_stock2.write(str(previous_day)+', '+str(old_value2)+'\n'+str(current_day)+', '+str(new_value2))
  append_stock3.write(str(previous_day)+', '+str(old_value3)+'\n'+str(current_day)+', '+str(new_value3))
  append_stock4.write(str(previous_day)+', '+str(old_value4)+'\n'+str(current_day)+', '+str(new_value4))
  append_stock5.write(str(previous_day)+', '+str(old_value5)+'\n'+str(current_day)+', '+str(new_value5))
  
  append_stock1.close()
  append_stock2.close()
  append_stock3.close()
  append_stock4.close()
  append_stock5.close()

def graph_stocks():
  for line in open('stock_data1.txt', 'r'):
    lines = [i for i in line.split()]
    x.append(lines[0])
    y1.append(int(lines[1]))
  for line in open('stock_data2.txt', 'r'):
    lines = [i for i in line.split()]
    y2.append(int(lines[1]))
  for line in open('stock_data3.txt', 'r'):
    lines = [i for i in line.split()]
    y3.append(int(lines[1]))
  for line in open('stock_data4.txt', 'r'):
    lines = [i for i in line.split()]
    y4.append(int(lines[1]))
  for line in open('stock_data5.txt', 'r'):
    lines = [i for i in line.split()]
    y5.append(int(lines[1]))
  plt.title("STOCKS")
  plt.xlabel('DAY')
  plt.ylabel('MONEY')
  plt.yticks()
  plt.axis([0, 10, 0, 200])
  plt.plot(x, y1, marker='o', c='red', label='BLU')
  plt.plot(x, y2, marker='o', c='blue', label='RED')
  plt.plot(x, y3, marker='o', c='yellow', label='EIC')
  plt.plot(x, y4, marker='o', c='green', label='CDC')
  plt.plot(x, y5, marker='o', c='orange', label='CLE')
  
  if current_day == 0:
    plt.legend(loc='lower right')
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
  else:
    this_is_not_a_variable_just_skipping_else_statement = 1
  plt.ion()
  plt.show()

def tell_me(): #player command to learn current day, balance, and portfolio
  update_portfolio()
  print("Your current balance is:", balance)
  print("Your current combined portfolio is:", portfolio)
  print("You have", stock_1_stocks, "stocks, worth", stock_1_portfolio, "in", stock_1_name)
  print("You have", stock_2_stocks, "stocks, worth", stock_2_portfolio, "in", stock_2_name)
  print("You have", stock_3_stocks, "stocks, worth", stock_3_portfolio, "in", stock_3_name)
  print("You have", stock_4_stocks, "stocks, worth", stock_4_portfolio, "in", stock_4_name)
  print("You have", stock_5_stocks, "stocks, worth", stock_5_portfolio, "in", stock_5_name)
  print("You have", (total_days - current_day), "days to reach your goal")

#-----Main Code-----
reset_stock_data()
update_stock_graphs()
help()
graph_stocks()