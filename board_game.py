class Cell:
    """"Represent a cell in a game's board. Every cell has Value attribute.
        default=" " """

    def __init__(self, value=" "):
        
        self.value=value
  
    def __repr__(self):
        return self.value

    def set_value(self, value):
        self.value=value
        
    def get_value(self):
        return self.value

    def clear(self):
        self.value=" "

        
   

    

class Column:
    """ Represents column in the game's board. every column is a
        list of cells. setting cell in the column is depended in
        the insertion status: if free: setting is possible in every
        cell at the column.
        else: just the first empety cell is avialble to be setted. """ 

    def __init__(self,n, free=True):
        self.lst=[Cell() for i in range (n)]
        self.free_insertion=free
        

    @property
    def last (self):
        cnt=-1
        for cell in self.lst:
            if cell.get_value()==" ":
                cnt+=1
                
        return cnt

    
    

    def set_by_index(self, index, val):
        if self.free_insertion:
            self.lst[index].set_value(val)

        else:
            """ignore the index"""
            i=self.last
            self.lst[i].set_value(val)
        

    def is_full(self):
        """ true iff last cell not full"""
        return self.last==-1





class Board:
      """Represent the game's board as a n*m matrix of cells.
         the board matrix is m columns with n cells"""
      def __init__ (self, n, m, insertion_opt):
        self.cols=n
        self.rows=m
        self.matrix=[Column(n, insertion_opt) for i in range (m)]

      def set_cell(self, i, j, val):
          """set the cell in the i col and the j row to val  """
          self.matrix[i].set_by_index(j,val)

      def get_cols(self):
          return self.cols

      def get_rows(self):
          return self.rows

      def get_cell(self, i,j):
          return self.matrix[i].lst[j].get_value()
      def clear_cell(self,i,j):
          self.matrix[i].lst[j].clear()

      def is_empty_cell(self, i,j):
          return self.get_cell(i,j)==" "
          

      def print_board(self):
         """print the board to screen"""
          def print_line(n):
              """print n times "====" to create the upline of every row"""
              for i in range (n):
                  print (" ====", end="")

          def print_cell(val):
              """print cell by printing the frame and the value of this cell"""
              seperator=" "
              print("| "+str(val)+seperator , end=" ")

          def print_all(board ,rows, cols):
              """ printing the whole board"""
              print(" ", end="")        
              for i in range (cols):
                  print(" "+"{word:4}".format(word=str(i+1)), end="") #printing the numbers of the columns
              print()
              for i in range(rows):
                print_line(cols)                                      #printing the upline
                print()
                for j in range(cols):
                    print_cell(self.get_cell(j,i))                    #printing the cell
                  
                    if j==cols-1:
                      print("|")
                    
                
                if i==rows-1:
                    print_line(cols)
                    print()

          print_all(self.matrix, self.rows, self.cols)



