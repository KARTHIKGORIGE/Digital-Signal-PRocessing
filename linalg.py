#program to perform linear algebraic and arithmetic operations  on matrices
import numpy as k
a=k.array(input('enter 3*3 matrix:'))
print 'you entered the matrix\n',a
d=k.linalg.det(a)
print 'the determinent of entered matrix is:\n',d
i=k.linalg.inv(a)
print 'the inverse of entered matrix is:\n',i
e=k.linalg.eigvals(a)
print 'the eigen values of entered matrix are:\n',e
ev=k.linalg.eig(a)
print 'the eigen vectors of entered matrix are:\n',e
r=k.linalg.matrix_rank(a)
print 'the rank of enterd matrix is:\n',r
q=k.linalg.qr(a)
print 'the QR decomposition of the entered matrix is:\n',q
p=k.linalg.matrix_power(a,3)
print 'the power of the enterd matrix raised to 3 is\n',p
b=k.array(input('enter 3*3 matrix:'))
print 'your entered matrix b is',b
ad=k.add(a,b)
print 'the addition of two matrices is:\n',ad
sub=k.subtract(a,b)
print 'the subtraction of a from b is:\n',sub
mul=k.multiply(a,b)
print 'the element by element multiplication of matrices a and b is:\n',mul
prod=k.dot(a,b)
print 'the product of matrices a and b is:\n',prod
div=k.divide(a,b)
print 'the element by element divsion of matrices a and b is:\n',div






