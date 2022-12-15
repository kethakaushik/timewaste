car={"brand":"ford","model":"mustang","year":1964}
car.clear()
print("cleared dictionary is:",car)
a=car.copy()
print("copied dictionary is:",a)
x={'key1','key2','key3'}
y=0
thisdict=dict.fromkeys(x,y)
print("dictionary after from keys() is :",thisdict)
b=car.get('model')
print("model of the car is:",x)
c=car.items()
print("items are:",c)
d=car.keys()
print("keys are:",d)
car.pop(model)
print("popped dictionary is:",car)


