co = float(input('Qual é o cateto oposto? '))
ca = float(input('Qual é o cateto adjacente? '))
h = (co*co + ca*ca)
#calcular a hipotenusa do triangulo retangulo
h = (h**(1/2))
#Usar a info para trazer o sen e o cos e a tang do ==
s = (co/h)
c = (ca/h)
t = (co/ca)
#jogar na tela as informações
print('Após calcular a hipotenusa do triangulo com o co e o ca, descobrimos que o sen é {:.2f} o cos é {:.2f} e a tang é {:.2f}'.format(s, c, t))
