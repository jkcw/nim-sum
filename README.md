# nim-sum
It calculates the Nim sum of a nim game.

# The rules of Nim
The traditional game of Nim is played with a number of coins arranged in heaps: the number of coins and heaps is up to you. There are two players. When it's a player's move he or she can take any number of coins from a single heap. They have to take at least one coin, though, and they can't take coins from more than one heap. The winner is the player who makes the last move, so there are no coins left after that move. (Some people play the game the other way around, with the last person to make a move losing the game) 

# Winning Strategy

## Adding the Nim way (Nim Sum)
The secret to finding the winning strategy hinges on writing the sizes of the heaps (the number of coins in each heap) in binary, and then adding those numbers up — but not using the ordinary way of adding numbers, but something appropriately called Nim addition.

To add some given binary numbers using Nim addition, you first write them underneath each other, as you might for ordinary addition. Then you look at each of the columns in turn. If the number of 1s in a column is odd, you write a 1 underneath it; if it's even, you write a 0 underneath it. Doing this for each column gives a new binary number, and that's the result of the Nim addition.

As an example, let's Nim-add the binary numbers 10, 11, and 100 (which stand for the decimal numbers 2, 3 and 4):

```
0 1 0
0 1 1
1 0 0

Nim Sum:
1 0 1
```
So the result, which is called the Nim sum, is the binary number 101. Nim addition is not the same as ordinary addition: the binary number 101 is 5 in decimal, which is not equal to the ordinary sum 2+3+4 = 9.

## The Fact of Nim Sum
 - **Fact 1:** Suppose it's your turn and the Nim sum of the number of coins in the heaps is equal to 0. Then whatever you do, the Nim sum of the number of coins after your move will not be equal to 0.

 - **Fact 2:** Suppose it's your turn and the Nim sum of the number of coins in the heap is not equal to 0. Then there is a move which ensures that the Nim sum of the number of coins in the heaps after your move is equal to 0.

Now suppose you are player A, so you go first. Also suppose that the Nim sum of the number of coins in the heaps is not equal to 0. Your strategy will be this: if possible always make a move that reduces the next Nim sum, the Nim sum after your move, to 0. This would then mean that whatever player B does next, by fact 1 the move would turn the next Nim sum into a number that's not 0.

# Usage
In the following paragraphs, I am going to describe how you can get and use nim-sum for your own projects.

## Getting it
To download nim-sum, either fork this github repo or simply use Pypi via pip.
```
$ pip install NimSum
```

## Using it
```python
from NimSum import NimSum
```

# References
[Plus Magazine: Play to win with Nim](https://plus.maths.org/content/play-win-nim)
