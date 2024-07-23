# Catalan Numbers
## Introduction
Catalan numbers are a sequence of positive integers that are found in many counting problems in combinatorics.   
They count certain  types of:   
- lattice paths
- permutations
- binary trees
- other combinatorial objects

They satisfy a fundamental recurrence relation, and have a closed-form formula in terms of binomial coefficients.

## Definition
C<sub>0</sub>, C<sub>1</sub>, C<sub>2</sub>, ..., C<sub>n</sub> are given by the formula:   
C<sub>n</sub> = $\frac{1}{n+1}$($\frac{2n}{n}$)   

The first few Catalan numbers are:   
*C<sub>0</sub> = 1*   
*C<sub>1</sub> = 1*  
*C<sub>2</sub> = 2*  
*C<sub>3</sub> = 5*  
*C<sub>4</sub> = 14*  
*C<sub>5</sub> = 42*  

## Applications
There are many areas of applications of catalan numbers. The following are handful:
- Dyck Paths
- Acceptable Sequence
- Balanced Parenthesis
- Binary Tree
- Triangulations of Polygons 
- Mountain Ranges

### Dyck Paths
##### Theorem
The number of valid parenthesis expressions that consists of `n` right parenthesis is equal to the n<sup>th</sup> Catalan number.
For example C<sub>3</sub> = 5 and there are 5 ways to create valid expressions with 3 sets of parenthesis.
- `() () ()`
- `(())()`
- `()(())`
- `((()))`
- `(()())`

Let us consider the right parenthesis to be `+1s`, and the left parenthesis `-1s`, we can write this formally as follows:

The number of sequences a<sub>1</sub>, a<sub>2</sub>, ... a<sub>2n</sub> of 2n terms that can be formed by using `n` copies of `+1's` and `n` copies `-1's` whose partial sums satisfy  
a<sub>1</sub> + a<sub>2</sub> + ... a<sub>k</sub> ≥ 0  

for `k` = `1`, `2`, `3`, `...`, `2n` equals the n<sup>th</sup> Catalan number. 


## Computation Methods
- Recurrence Relation
- Generating Functions