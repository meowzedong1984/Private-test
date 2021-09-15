import time
seconds = time.time()
sugaruserinput = 0
kettlevolume = 0
cuptea = 0
teabag = 0
sugar = 0
kettletemp = 17
water = 401
cupwatervolume = 0
while sugaruserinput == 0:
    try:
        x = int(input("how many sugars "))
    except ValueError: continue
    print (x)
    sugaruserinput = 1
