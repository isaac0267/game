theBoard={'7':' ','8':' ' ,'9':' ',
          '4':' ', '5':' ','6':' ',
          '1':' ', '2':' ','3':' '
}

#now we will make the funcion: 
def printbord(bord): # we make the function bord and it take parameter
    print(bord['7']+'|'+bord['8']+'|'+bord['9'])
    print('-+-+-')
    print(bord['4']+'|'+bord['5']+'|'+bord['6'])
    print('-+-+-')
    print(bord['1']+'|'+bord['2']+'|'+bord['3'])

printbord(theBoard) # we call the function. 

def game():
    turn='X'
    count=0

    for i in range(2):
        printbord(theBoard)
        print("It is your turn"+turn+"The move that you should")
        
        move=input()

        if theBoard[move]=='':
            theBoard[move]=turn
            count+=1 
        else:
            print("The place is not empty")
            continue      


        
           