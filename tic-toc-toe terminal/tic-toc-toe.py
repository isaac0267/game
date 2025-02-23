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
