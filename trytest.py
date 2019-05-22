act, ls, el, att, acts, tlst, sk = [], [], [], [], {}, [], []

lst1 = input().split()

lst = ''

for i in lst1:
    lst = lst + i

l = list('('+lst+')')

lst = list(lst)

while '(' in l:

    left = 0
    right = 0

    while l[right] != ')': 

        right += 1

    left = right

    while l[left] != '(':

        left -= 1

    tlst = [left-1, right-1]

    sk.append(left-1)
    sk.append(right-1)

    for j in range(left,right+1):

        if l[j] == '*':

            tlst.append(j-1)
            el.append(j-1)
            
    for j in range(left,right+1):

        if l[j] == '+':
            tlst.append(j-1)
            el.append(j-1)

        l[j] = ' '
        


    if l[left-1] == '!':

        tlst.append(left-2)
        el.append(left-2)

        l[left-1] = ' '

    act.append(tlst)


g = -1

for i in el:

    g += 1
    
    acts[i] = []

    if lst[i] == '!':

        if (lst[i+1] == '(') and (lst[i+3] == ')'):
            acts[i].append(i+2)
            att.append(i+2)

        else:

            acts[i].append(el[g-1])

    else:

        if (i-1 not in att):
            
            acts[i].append(i-1)
            att.append(i-1)
            
            k = 1
            while k < len(sk) and sk[k] != i-1:
                k += 2
            if k < len(sk):
                att.append(sk[k-1])
                   
        else:
            acts[i].append(-2)


        if (i+1 not in att) and (lst[i+1] != '!'):

            acts[i].append(i+1)
            att.append(i+1)
            k = 0
            while k < len(sk) and sk[k] != i+1:
                k += 2
            if k < len(sk):
                att.append(sk[k+1])
   
        elif (lst[i+1] == '!') and (i+2 not in att) :

            acts[i].append(i+2)
            att.append(i+2)
            k = 0
            while k < len(sk) and sk[k] != i+2:
                k += 2
            if k < len(sk):
                att.append(sk[k+1])

        else:
            acts[i].append(-2)

for i in acts:

    if acts[i][0] in sk:

        k = 0
        while act[k][1] != acts[i][0]:
            k += 1
        acts[i][0] = act[k][-1]


    if (len(acts[i]) > 1) and (acts[i][1] in sk):

        k = 0
        while act[k][0] != acts[i][1]:
            k += 1
        acts[i][1] = act[k][-1]

    if acts[i][0] == -2 and acts[i][1] == -2:
        k = 0
        while i not in act[k]: 
            k += 1
        h = 0
        while act[k][h] != i:
            h += 1
        acts[i][0] = act[k][h-2]
        acts[i][1] = act[k][h-1]

    elif acts[i][0] == -2:
        
        k = 0
        while i not in act[k]: 
            k += 1
        h = 0
        while act[k][h] != i:
            h += 1
        acts[i][0] = act[k][h-1]

    elif (len(acts[i]) > 1) and acts[i][1] == -2:
        
        k = 0
        while i not in act[k]: 
            k += 1
        h = 0
        while act[k][h] != i:
            h += 1
        acts[i][1] = act[k][h-1]
            
print(acts) # - это результат, далее по этому графика

#Пример выражения: A + B* !( J+C)