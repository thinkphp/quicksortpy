#
# Quick__Sort.py - Quick Sort - Algorithm Sorting an array of randomly permuted of values.
# Website <http://adrianstatescu.ro>(MIT License).
# Email   <mergesortv@gmail.com>.
# Copyright (c) 2015, Adrian Statescu.
# 
 

class QuickSort:

  vec = [] 

  len = -1

  def __init__(self, arr):

        self.vec = arr

        self.len = len( self.vec )

        self.sort() 

  def get( self ):

      return self.vec  

  def sort( self ):

      self._quicksort(0, self.len - 1 )

  def _quicksort(self, lo, hi ):

      i = lo
      j = hi
      
      pivot = self.vec[ (lo + hi ) >> 1 ]      

      while i <= j:

         while self.vec[ i ] < pivot:

               i += 1

         while self.vec[ j ] > pivot:

               j -= 1

         if i <= j:

            self.swap( i, j )

            i += 1
            j -= 1

      if(lo < j): 
        self._quicksort(lo, j)
      if(i < hi): 
        self._quicksort(i, hi)


  def swap(self, i, j):

      temp = self.vec[ i ] ^ self.vec[ j ]

      self.vec[ i ] = temp ^ self.vec[ i ]

      self.vec[ j ] = temp ^ self.vec[ j ]