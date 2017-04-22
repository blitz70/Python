#print age(15-60) and allowed ages

def allowed_age(age):
    allowed = age/2 + 7
    return allowed

for x in range(15,61):
    print('If',x,',can date',allowed_age(x),'or older')

