from array import array
import random
import time

class Board :
    """ An object which describe the board composition """

    def __init__(self,numberOfMines : int,dimensionX : int,dimensionY : int) -> None :
        self.boardMatrix = []
        self.dimX = dimensionX
        self.dimY = dimensionY
        self.__createBoard()
        self.__generateMinesPosition(numberOfMines)
        self.__calcCellsValues()
    
    def __createBoard(self) -> None :
        for i in range(self.dimY) :
            line = []
            for j in range(self.dimX) :
                line.append(0)
            self.boardMatrix.append(line)


    def __generateMinesPosition(self,numberOfMines : int) -> None :
        while numberOfMines > 0 :
            minePosX = random.randint(1,self.dimX)
            minePosY = random.randint(1,self.dimY)
            if self.boardMatrix[minePosY-1][minePosX-1] != 9 :
                self.boardMatrix[minePosY-1][minePosX-1] = 9
                numberOfMines = numberOfMines - 1
            
    
    def __calcCellsValues(self) -> None :
        for i in range(self.dimY) :
            for j in range(self.dimX) :
                if self.getCellValue(j,i) not in [-1,9] :
                    aroundValues = []
                    aroundValues.append(self.getCellValue(j-1,i-1))
                    aroundValues.append(self.getCellValue(j,i-1))
                    aroundValues.append(self.getCellValue(j+1,i-1))
                    aroundValues.append(self.getCellValue(j-1,i))
                    aroundValues.append(self.getCellValue(j+1,i))
                    aroundValues.append(self.getCellValue(j-1,i+1))
                    aroundValues.append(self.getCellValue(j,i+1))
                    aroundValues.append(self.getCellValue(j+1,i+1))
                    self.boardMatrix[i][j] = aroundValues.count(9)
                    
                    
    
    def getCellValue(self,posX : int, posY : int) -> int :
        if posX >= 0 and posX < self.dimX and posY >= 0 and posY < self.dimY :
            return self.boardMatrix[posY][posX]
        return -1
    
    def debugMe(self) -> None :
        for i in self.boardMatrix :
            print (i)