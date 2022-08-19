import random

from numpy import number

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
                if self.boardMatrix[i][j] != 9 :
                    aroundValues = []
                    if i != 0 :
                        if j != 0 :
                            aroundValues.append(self.boardMatrix[i-1][j-1])
                        aroundValues.append(self.boardMatrix[i-1][j])
                        if j != self.dimX - 1 :
                            aroundValues.append(self.boardMatrix[i-1][j+1])
                    if j != 0 :
                        aroundValues.append(self.boardMatrix[i][j-1])
                    if j != self.dimX - 1 :
                        aroundValues.append(self.boardMatrix[i][j+1])
                    if i != self.dimY -1 :
                        if j != 0 :
                            aroundValues.append(self.boardMatrix[i+1][j-1])
                        aroundValues.append(self.boardMatrix[i+1][j])
                        if j != self.dimX - 1 :
                            aroundValues.append(self.boardMatrix[i+1][j+1])
                    self.boardMatrix[i][j] = aroundValues.count(9)
                    
                    
    
    def getCaseValue(self,posX : int, posY : int) -> int :
        return self.boardMatrix[posY],[posX]
    
    def debugMe(self) -> None :
        for i in self.boardMatrix :
            print (i)