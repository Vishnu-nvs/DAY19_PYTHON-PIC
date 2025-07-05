print("\n")
for row in range(20):
    for col in range(19):
      if (row==6 and(col==3 or col==4 or col==5 or col==6 or col==7)):
        print("*",end=" ")
      elif (col==2 and (row==7 or row==8 or row==9 or row==10 or row==11)):
        print("*",end=" ")
      elif (row==3 and(col==6 or col==7 or col==8 or col==9 or col==10)):
        print("*",end=" ")
      elif (col==5 and (row==4 or row==5 or row==11 or row==12 or row==13 or row==14 or row==15)):
        print("*",end=" ")
      elif (col==11 and (row==4 or row==5 or row==6 or row==7 or row==8 or row ==9)):
        print("*",end=" ")
      elif (col==15 and (row==7 or row==8 or row==9 or row==10 or row==11 or row ==12)):
        print("*",end=" ")
      elif (row==13 and(col==9 or col==10 or col==11 or col==12 or col==13 or col==14)):
        print("*",end=" ")
      elif (row==6 and(col==12 or col==13 or col==14)):
        print("*",end=" ")
      elif ((row==10 or row==16) and(col==6 or col==7 or col==8 or col==9 or col==10)):
        print("*",end=" ")
      elif (row==12 and(col==3 or col==4)):
        print("*",end=" ")
      elif (col==11 and(row==14 or row==15)):
        print("*",end=" ")
      elif row==0 or row==19 or col==0 or col==18:
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print() 
        
      
 