import Random as Rnd
import Num as Num
import Range as Rng

def x(z):
    return z[0]

def cls(z):
  v = 0.0
  if z < 0.2:
    v = 0.2 + 2*Rnd.r()/100
  elif z < 0.6:
    v = 0.6 + 2*Rnd.r()/100
  else:
    v = 0.9 + 2*Rnd.r()/100
  return v

if __name__ == "__main__":
    t, n = [], Num.create()
    for _ in range(1,51):
        w = Rnd.r()
        c = cls(w)
        Num.update(n, c)
        t.append(list({w, c}))
    print("\nUnsupervised ranges")
    for j, one in enumerate(Rng.main(t, x)):
        print("x", j+1, str(one))