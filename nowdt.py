from datetime import datetime

n = str(datetime.now())
date = [n[8:10],n[5:7]]
ms = n[-7:]
for i in date:
    print(i,end='/')
print(n[:4],n[11:-7])
