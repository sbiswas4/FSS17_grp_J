import Random as Rnd
import Num as Num
import Range as Rng

def x(z):
    return z[0]

def cls(z):
    v = 0.0
    if z > 0 and z < 0.2:
        v = 0.2
    elif z >= 0.2 and z <= 0.6:

        v = 0.6
    else:
        v = 0.9
    return v

def sort_t(t):
    t = sorted(t, key=lambda v: x(v))
    return t

if __name__ == "__main__":
    t, n = [], Num.create()
    bin_length =[]
    bin_most = []
    for _ in range(1,51):
        w = Rnd.r()
        c = cls(w)
        Num.update(n, c)
        t.append(list([w, c]))
# Generate Unsupervised ranges
    print("\nUnsupervised ranges")
    Ranges = Rng.main(t, x)
    for j, one in enumerate(Rng.main(t, x)):
        print("x", j + 1, str(one))
        bin_length.append(one.n)
        bin_most.append(one.hi)
        
# Generate Supervised ranges

    sorted_tab = sort_t(t)
    start = 0
    dict_pure = {}
    purity = [] #False impure, True pure

    for i in bin_length:
        for j in range(start,start + i):
            if sorted_tab[start][1] != sorted_tab[j][1]:
                purity.append({'purity': False})
                break
        start += i

        purity.append({'purity':True,'class':sorted_tab[j][1]})

    index =0
    for hi in  bin_most:
        purity[index]['most'] = hi
        index+=1
    start = 0
    length =len(purity)
    while start<length-1:
        if purity[start]['purity'] == True:
            if purity[start]['purity'] == purity[start+1]['purity'] and purity[start]['class'] == purity[start+1]['class']:
                purity.pop(start)
                length-=1
            else:
                start+=1
        else:
            start+=1
    print("\n Supervised ranges")

    for i in range(0,len(purity)):
        purity[i].update({'label':i+1})
        purity[i].pop('purity')
        print(purity[i])
