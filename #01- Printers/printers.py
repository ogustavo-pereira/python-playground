from __future__ import print_function
#!Criando Variavel
a = "Ola mundo"
b = 2
c = 2.44

#!printers

#! Print this
print("Print this")

#! Ola mundo 2 2.44
print(a,b,c)

#!Print Ola mundo  Number 2 float 2.44
print("Print",a," Number",b,"float",c)

#!Print number 2 for stringg Ola mundo and float 2.44
print("Print number %s for stringg %s and float %s" % (b,a, c))

#!Print Ola mundo , 2 2.44
print("Print %(texto)s , %(number)s %(float)s" % {'texto': a, 'number': b,'float':c})

#!print Ola mundo for 2.44 is 2
print("print {} for {} is {}".format(a,c ,b))

#! Print with future import print_function Ola mundo is 2
print(f'Print with future import print_function {a} is {b}')