
# for row in range(20):
#     for col in range(16):
#        if row==0 or row==19 or col==0 or col==15 or (col==2 and(row==7 or row==8 or row==9 or row==10 or row==11 or row==12))or (row==2 and (col ==6 or col ==7 or col==8)) or (row==3 and col ==6) or (row==3 and col ==6) or (row ==4 and(col ==6 or col ==7)) or (row==5 and col==7) or (row ==6 and(col ==3 or col==4 or col==5 or col==6 or col==7)) or (row==13 and(col==2 or col==3 or col==4)) or (col==5 and (row==8 or row==9 or row==10 or row==11 or row==12)) or (row==8 and (col==6 or col==7 or col==8)) or (col==9 and (row==3 or row==4 or row==5 or row==6 or row==7)):
#             print("*",end="   ")
      
#             print("  ",end="   ")
            
#     print()
   
   
   
   
   
  #python first part1
#   border row==0 or row==19 or col==0 or col==1
# 1.(col==2 and(row==7 or row==8 or row==9 or row==10 or row==11 or row==12))
#2.(row==2 and (col ==6 or col ==7 or col==8)) 
#3. (row==3 and col ==6)
#4.(row ==4 and(col ==6 or col ==7))
#5.(row==5 and col==7)
#6.(row ==6 and(col ==3 or col==4 or col==5 or col==6 or col==7))
#7.(row==13 and(col==2 or col==3 or col==4))
#8.(col==5 and (row==8 or row==9 or row==10 or row==11 or row==12))
#9.(row==8 and (col==6 or col==7 or col==8))
#10.(col==9 and (row==3 or row==4 or row==5 or row==6 or row==7))

#python 2nd part
# 1.(row==6 and(col==11 or col==12))
# 2.(col==10 and( row==7 or row ==8 or row ==9))
# 3.(row==10 and(col==7 or col==8 or col==9 or col==10))
# 4.(col==6 and (row==11 or row==12 or row==13 or row==14 or row==15 or row==16))
# 5.(row==17 and (col==7 or col==8))
# 6.(col==9 and (row==14 or row==15 or row==16))
# 7.(col==8 and(row==13 or row==14))
# 8.(row==12 and(col==8 or col==9 or col==10 or col==11 or col==12))
# 9.(col==13 and(row==7 or row==8 or row==9 or row==10 or row==11 or row==12))

# 1st-1 and 2nd - 9 lines code decreses
# ((col==2 orcol==13) and(row==7 or row==8 or row==9 or row==10 or row==11 or row==12))

for row in range(20):
    for col in range(16):
      if row==0 or row==19 or col==0 or col==15:
         print("*",end="   ")
      elif (col==2 and(row==7 or row==8 or row==9 or row==10 or row==11 or row==12)) or (row==2 and (col ==6 or col ==7 or col==8)) or (row==3 and col ==6) or (row ==4 and(col ==6 or col ==7)) or (row==5 and col==7) or (row ==6 and(col ==3 or col==4 or col==5 or col==6 or col==7)) or (row==13 and(col==2 or col==3 or col==4)) or (col==5 and (row==8 or row==9 or row==10 or row==11 or row==12)) or (row==8 and (col==6 or col==7 or col==8)) or (col==9 and (row==3 or row==4 or row==5 or row==6 or row==7)):
        print("*",end="   ")
      elif (row==6 and(col==11 or col==12)) or (col==10 and( row==7 or row ==8 or row ==9)):
        print("*",end="   ")
      elif (row==10 and(col==7 or col==8 or col==9 or col==10)) or (col==6 and (row==11 or row==12 or row==13 or row==14 or row==15 or row==16)):
        print("*",end="   ")
      elif (row==17 and (col==7 or col==8)) or (col==9 and (row==14 or row==15 or row==16)) or (col==8 and(row==13 or row==14)):
        print("*",end="   ")
      elif (row==12 and(col==8 or col==9 or col==10 or col==11 or col==12)) or (col==13 and(row==7 or row==8 or row==9 or row==10 or row==11 or row==12)):
        print("*",end="   ") 
      else:
        print("  ",end="   ")
    
    print()  
         
        