import random
a=int(input("как вы хотете участвовать? первыми(1); последним(2): "))
w=[1,2,3,4,5,6,7,8,9]
b=0
if a==1:
  while b<9:
    print("", w[0], "|", w[1], "|", w[2], "\n", "—", "+", "—", "+", "—", "\n", w[3], "|", w[4], "|", w[5], "\n", "—", "+", "—", "+", "—", "\n", w[6], "|", w[7], "|", w[8])
    d=0
    while d<1:
        e=0
        while e<1:
            c=int(input("Введите число, за место которого поставите X: "))
            if c<1 or c>9:
                print("Нет такого числа.")
            else:
                e+=1
        c-=1
        if w[c]=="X" or w[c]=="O":
            print("Занято.")
        else:
            w[c]="X"
            d+=1
    if w[0]==w[1]==w[2] or w[3]==w[4]==w[5] or w[6]==w[7]==w[8] or w[0]==w[3]==w[6] or w[1]==w[4]==w[7] or w[2]==w[5]==w[8] or w[0]==w[4]==w[8] or w[6]==w[4]==w[2]:
        print("", w[0], "|", w[1], "|", w[2], "\n", "—", "+", "—", "+", "—", "\n", w[3], "|", w[4], "|", w[5], "\n", "—", "+", "—", "+", "—", "\n", w[6], "|", w[7], "|", w[8])
        print("Вы победили.")
        b=9
    else:
        if b==8:
            b+=1
            print("", w[0], "|", w[1], "|", w[2], "\n", "—", "+", "—", "+", "—", "\n", w[3], "|", w[4], "|", w[5], "\n", "—", "+", "—", "+", "—", "\n", w[6], "|", w[7], "|", w[8])
            print("Ничья.")
        else:
            b+=1
            print("", w[0], "|", w[1], "|", w[2], "\n", "—", "+", "—", "+", "—", "\n", w[3], "|", w[4], "|", w[5], "\n", "—", "+", "—", "+", "—", "\n", w[6], "|", w[7], "|", w[8])
            print("Бот сходил.")
            d=0
            while d<1:
                c=random.randint(1, 9)
                c-=1
                if w[c]=="X" or w[c]=="O":
                    d=0
                else:
                    w[c]="O"
                    d+=1
            if w[0]==w[1]==w[2] or w[3]==w[4]==w[5] or w[6]==w[7]==w[8] or w[0]==w[3]==w[6] or w[1]==w[4]==w[7] or w[2]==w[5]==w[8] or w[0]==w[4]==w[8] or w[6]==w[4]==w[2]:
                print("", w[0], "|", w[1], "|", w[2], "\n", "—", "+", "—", "+", "—", "\n", w[3], "|", w[4], "|", w[5], "\n", "—", "+", "—", "+", "—", "\n", w[6], "|", w[7], "|", w[8])
                print("Вы проиграли.")
                b=9
            else:
                b+=1

elif a==2:
  while b<9:
    print("", w[0], "|", w[1], "|", w[2], "\n", "—", "+", "—", "+", "—", "\n", w[3], "|", w[4], "|", w[5], "\n", "—", "+", "—", "+", "—", "\n", w[6], "|", w[7], "|", w[8])
    d=0
    while d<1:
      c=random.randint(1, 9)
      c-=1
      if w[c]=="X" or w[c]=="O":
        d=0
      else:
        w[c]="O"
        d+=1
          if w[0]==w[1]==w[2] or w[3]==w[4]==w[5] or w[6]==w[7]==w[8] or w[0]==w[3]==w[6] or w[1]==w[4]==w[7] or w[2]==w[5]==w[8] or w[0]==w[4]==w[8] or w[6]==w[4]==w[2]:
            print("", w[0], "|", w[1], "|", w[2], "\n", "—", "+", "—", "+", "—", "\n", w[3], "|", w[4], "|", w[5], "\n", "—", "+", "—", "+", "—", "\n", w[6], "|", w[7], "|", w[8])
            print("Вы проиграли.")
            b=9
          else:
            b+=1
    else:
      e=0
        while e<1:
            c=int(input("Введите число, за место которого поставите X: "))
            if c<1 or c>9:
              print("Нет такого числа.")
            else:
                e+=1
        c-=1
        if w[c]=="X" or w[c]=="O":
          print("Занято.")
        else:
          w[c]="X"
          d+=1
    if w[0]==w[1]==w[2] or w[3]==w[4]==w[5] or w[6]==w[7]==w[8] or w[0]==w[3]==w[6] or w[1]==w[4]==w[7] or w[2]==w[5]==w[8] or w[0]==w[4]==w[8] or w[6]==w[4]==w[2]:
      print("", w[0], "|", w[1], "|", w[2], "\n", "—", "+", "—", "+", "—", "\n", w[3], "|", w[4], "|", w[5], "\n", "—", "+", "—", "+", "—", "\n", w[6], "|", w[7], "|", w[8])
      print("Вы победили.")
      b=9
    else:
      if b==8:
        b+=1
        print("", w[0], "|", w[1], "|", w[2], "\n", "—", "+", "—", "+", "—", "\n", w[3], "|", w[4], "|", w[5], "\n", "—", "+", "—", "+", "—", "\n", w[6], "|", w[7], "|", w[8])
        print("Ничья.")
else:
  print("не коретное чесло наберите 1 или 2")