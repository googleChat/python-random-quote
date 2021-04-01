import random

def main():
  f = open("C:\MyProject\python-random-quote\quotes.txt.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0,last)


  print(quotes[rnd])



if __name__ == "__main__":
  main()

