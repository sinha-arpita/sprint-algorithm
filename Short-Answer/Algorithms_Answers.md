#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)a)  a = 0
    while (a < n * n * n):
      a = a + n * n
``runtime is O(n).while loop will  atleast run n times.


b)b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
    we have 2 nested loops . so runtime will be O(n^2)


c)c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
This is a recursive function call, with one function call per recursion. So if there are 5 bunnies then the
 function is recursively call for 4,3, 2,1 bunny respectively. 
Hence It will be a linear function of n.

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, 
and doesn't get broken if dropped off a floor less than floor f. We have a strategy to determine the value of f
 such that the number of dropped + broken eggs is minimized.

ANS:Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is
 thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f.
 we have  a strategy to determine the value of f such that the number of dropped eggs is minimized.

 To find out the floor f from which the egg will not break we can start from nth floor or 1st floor and go linearly
 to check where egg breaks/does not break. But this approach is not optimum in terms of run time.
 This will require n eggs in worst case.

We can apply binary search here, So we will start from middle floor and this way we can neglect one half of the floor

middle floor = highestfloor+lowest floor//2

Let's say middle floor is the 5th floor and

egg breaks from 5th floor , so we hve to test the lower floor that is the 4th floor, left side of the array
egg does not break, so we have to go upper floor
Like binary search, we continue to find eliminate and find right floor.

We can think of this as binary search of a key, but finding leftmost occurance of it. Lets say,
 we represent floors as array index, and store 0 at each floor if egg does not break,
  1 if it does. For example, floors = [0,0,0,1,1,1,1,1] <- Indicates egg does break on 1st, 2nd and 3rd floor.
   And it starts to break from 4th floor. Now problem reduces to finding leftmost occurance of key 1 in this
    sorted array

so,

def find_min_floor(floors):
    last_floor_seen = None
    low=0
    high = len(floors)
    while low <= high:
        middle = (low + high) //2 
        if floors[middle]  == 1: #We find one occurance of 1, go left to check there are more
            last_floor_seen = middle
            high = middle -1
        else: #We found 0, 1 will be right of it. So go right.
            low = middle + 1
        
    return last_floor_seen   



