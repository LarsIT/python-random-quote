from random import randint, random



def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[randint(0,len(quotes)-1)])
  
if __name__== "__main__":
  primary()

