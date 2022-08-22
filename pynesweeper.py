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

class PlayableBoard :

    def __init__(self,numberOfMines : int,dimensionX : int,dimensionY : int) -> None :
        self.HIDDEN = "X"
        self.EMPTY = " "
        self.FLAG = "P"
        self.MINE = "*"
        self.b = Board(numberOfMines,dimensionX,dimensionY)
        self.this = []
        self.__createBoard(dimensionX,dimensionY)

    def __createBoard(self,dimX : int,dimY : int) -> None :
        for i in range(dimY) :
            line = []
            for j in range(dimX) :
                line.append(self.HIDDEN)
            self.this.append(line)

    def act(self,action : str,posX : int,posY : int) -> int :
        if posX >= 0 and posX < self.b.dimX and posY >= 0 and posY < self.b.dimY :
            if self.this[posY][posX] in [self.HIDDEN,self.FLAG] :
                if action == "reveal" :
                    return self.__actAsReveal(posX,posY)
                if action == "flag" :
                    self.__actAsFlag(posX,posY)
        return 0

    def __actAsReveal(self,posX : int,posY : int) -> int :
        if self.this[posY][posX] == self.HIDDEN :
            cv = self.b.getCellValue(posX,posY)
            match cv :
                case 0 :
                    self.__recursiveReveal(posX,posY)
                case 9 :
                    self.this[posY][posX] = self.MINE
                    return 1
                case _ :
                    self.this[posY][posX] = str(cv)
        return 0
    
    def __recursiveReveal(self,posX : int,posY : int) -> None :
        if self.this[posY][posX] == self.HIDDEN :
            self.this[posY][posX] = self.EMPTY
            self.__recursiveRevealAct(posX,posY-1)
            self.__recursiveRevealAct(posX-1,posY)
            self.__recursiveRevealAct(posX+1,posY)
            self.__recursiveRevealAct(posX,posY+1)
    
    def __recursiveRevealAct(self,posX : int,posY : int) -> None :
        cv = self.b.getCellValue(posX,posY)
        match cv :
            case -1 : pass
            case 0 : self.__recursiveReveal(posX,posY)
            case 9 : pass
            case _ : self.__recursiveRevealNumber(posX,posY,cv)

    def __recursiveRevealNumber(self,posX : int,posY : int,number : int) -> None :
        if self.this[posY][posX] == self.HIDDEN :
            self.this[posY][posX] = str(number)

    def __actAsFlag(self,posX : int,posY : int) -> None :
        if self.this[posY][posX] == self.HIDDEN :
            self.this[posY][posX] = self.FLAG
        else :
            if self.this[posY][posX] == self.FLAG :
                self.this[posY][posX] = self.HIDDEN