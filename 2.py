kot=int(input(''))
schet=0
for i in range(kot):
    z=input('')
    zkot=list(z)
    for i in range(len(zkot)):
        if zkot[i]=='к' and zkot[i+1]=='о' and zkot[i+2]=='т' or zkot[i]=='К' and zkot[i+1]=='о' and zkot[i+2]=='т':
            schet=schet+1
if schet>=1:
    print('МЯУ')
else:
    print('НЕТ')
                
