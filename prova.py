stringa = 'ciao'
print(stringa[1])

lista=["ciao","miao","bau"]

if ("ciao" in lista) :

    print("yes")

print(lista)

prova= 4 * "hi"
print(prova)

prova2="free"+"time"
print(prova2)

#operatori su liste

lista2=["mamma","papà","fratello"]
print(lista+lista2)


"h"+"e"+"l"+"l"+"o"

lista3=["ciao","Gio"]

print(lista3[0]+' '+lista3[1])

dizio1={'fratello':'Carlo','cane':'Kingo'}

dizio2={'fratello':'2005','cane':'2022'}

print( "mio fratello {} ha un cane di nome {} nato nel {}".format(dizio1['fratello'],dizio1['cane'],dizio2['cane']))


#for item in lista2:
    #print(item)

#for i in range(3,33,3):
    #print(i)


listanumeri =[2,4,6,8,10,12,14,16,18,20,22]

#for item in listanumeri:
    #if item > 14 :
        #print(item)

for i, item in enumerate(lista):
    print(i,item)
    print('position {}: item {}'.format(i,item))