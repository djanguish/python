import urllib.request
import math

mapnum=input("map number: ")
lowlim=input("lower limit: ")
uplim=int(input("upper limit: "))
lotnum=lowlim
while int(lotnum)<=uplim:
    name='{}-{}'.format(mapnum,lotnum)
    url='https://cms8.revize.com/revize/milfordme/{}.pdf'.format(name)
    path='E:\DATA sources\Milford Tax Maps\Map {}\{}.pdf'.format(mapnum, name)
    urllib.request.urlretrieve(url, path)
    lotnum=int(lotnum)+1
    intlen=0
    while intlen < 3:
        intlen=math.ceil(math.log(int(lotnum), 10))
        lotnum='0{}'.format(lotnum)
    
