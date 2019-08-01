#bad likebot by 9m

from urllib.request import urlopen,Request
AccId= 0
GJP = 0
if not AccId != "":
    print ("Enter AccId please")
    print()

if not GJP!= "":
  print ("Enter your goddamn geometry dash password")

ReceivingLevelID =input ("Level ID?")
Secret = input ("Secret")
print("Staring...")
while (True):
    url = "http://www.boomlings.com/database/likeGJItem211.php"
    p =  "gameVersion=20&binaryVersion=35&gdw=0&accountID=0&gjp=&"
    p = p.encode()
    data = urlopen (url,p).read().decode()

    if not data!= "1":
         print("Likebot has succeded")
         print()

         if not data!= "-1":
             print("likebot has failed try again")
             print()
