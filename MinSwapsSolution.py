def swapcnt(inar):
    temp = []
    outcnt = []
    outnum = None
    length = len(inar) - 1
    # maxindex = inar.index(max(inar))
    if length == 0:
        return (length)
    elif length%2 != 0:
        temp.append((length-1)//2)
        temp.append((length+1)//2)
    else:
        temp.append(length//2)
    #print(temp)
    rpt = [i for i,val in enumerate(inar) if val==max(inar)]
    #print(rpt)
    if  len(set(rpt).intersection(set(temp))) > 0:
        return 0
    else:
        for i in range(len(temp)):
            for j in range(len(rpt)):
                diff = abs(rpt[j] - temp[i])
                # if diff == 0:
                #     return 0
                # else :
                if outnum is None:
                    outnum = diff
                elif outnum > diff:
                    outnum = diff
                    # outcnt.append(abs(rpt[j] - temp[i]))
        return outnum


t = int(input())
in_dict = {}
for x in range(2*t):
     a = [int(x) for x in input().split(' ')]
     in_dict[x]= a

for k,v in in_dict.items():
    if k%2 != 0:
        print(swapcnt(v))
