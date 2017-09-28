import Random as Rnd
import Num as Num
import Range as Rng

tree_max_depth = 10

class sdtree:
	def __init__(self):
		self._t = None
		self._kids = []
		self.yfun = None
		self.pos = None
		self.attr = None
		self.val = None
		self.stats = None

	def create(self,t,yfun,pos,attr,val):
		self._t = t
		self._kinds={}
		self.yfun = yfun
		self.pos = pos
		self.attr = attr
		self.val = val
		self.stats = num.updates(t.rows, yfun)
		return
	def order(t,y):
		#def __init__(self, t, y):
		#	self.t = t
		#	self.y = y
		#	self,.out = {}
		#return

		def xpect(col):
			tmp = 0
			for _,x in enumerate(cols.nums):
				tmp = tmp + x.sd * x.n / col.n
		return tmp

		def whatif(head, y):
			col = {'pos':head.pos, 'what'=head.txt, 'nums'={}, 'n'=0}
			for _,row in enumerate(t.rows):
				x = row.cells[col['pos']]
				col['n'] = col['n'] + 1
				col['nums']['x'] = num.update(col['nums']['x'], y(row))
			return {'key':xpect(col), 'val':col}
		out = []
		for _,h in enumerate(t.x.cols):
			out.append(whatif(h,y))
		# how to write function (x,y) return x.key < y.key
		table.sort(out,x.key<y.key)
		# the last line too
		return lst.collect(out, x.val)


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
# Unsupervised range generation
    print("\nUnsupervised ranges")
    Ranges = Rng.main(t, x)
    for j, one in enumerate(Rng.main(t, x)):
        print("x", j + 1, str(one))
        bin_length.append(one.n)
        bin_most.append(one.hi)
# Supervised range generation
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

 
