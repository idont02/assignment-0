dicts = {'00':0, '01':1,'02':2,'03':3,'09':9,'0a':11,'0f':15,'10':16,'fe':254,'ff':255}
print(dicts.keys())
print(dicts.get('01'))

print(dicts)
dicts['0a']= 10
print(dicts)

print(dicts.values())
