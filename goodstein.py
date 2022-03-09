import math
import sys

def purge_tail(array):
    for i in range(len(array)):
        if set(array[i:]) == {0}:
            return array[:i]
    return array

def base_coeff_array(n, base):
    out = []
    for i in range(math.ceil(math.log(n, base)), -1, -1):
        out = [n//(base**i)] + out
        n = n%(base**i) #remainder
    return purge_tail(out)

def base_jump(n, base):
    if n == 1:
        return 1
    ar = base_coeff_array(n, base)
    out = 0
    for i in range(len(ar)):
        if i<base:
            out += ar[i]*(base+1)**i
        else:
            out += ar[i]*(base+1)**base_jump(i, base)
    return out

def base_form(n, base):
    if n < base:
        return str(n)
    ar = base_coeff_array(n, base)
    string = str(ar[0]) if ar[0]!=0 else ""
    for i in range(1, len(ar)):
        if ar[i]==0:
            continue
        else:
            temp = base_form(i, base) if i>base else i
            if ar[i]==1:
                if temp == 1:
                    add = str(base)
                else:
                    add = f"{base}^({temp})"
            else:
                if temp == 1:
                    add = f"{ar[i]}*{base}"
                else:
                    add = f"{ar[i]}*{base}^({temp})"
            string = add if string == "" else f"{add}+{string}"
    return string

def goodstein(a, n):
    out = [a]
    print(f"g({a},0) = {out[0]}")
    print(f"g({a},0) = ", end = "")
    print(base_form(a, 2))
    print()
    for j in range(0, n):
        base = j+2
        ar = base_coeff_array(out[-1], base)
        temp = 0
        for i in range(len(ar)):
            if i<base:
                temp += ar[i]*(base+1)**i
            else:
                temp += ar[i]*(base+1)**base_jump(i, base)
        out.append(temp-1)
        
        print(f"g({a},{j+1}) = {out[-1]}")
        print(f"g({a},{j+1}) = ", end = "")
        print(base_form(out[-1], base+1))
        print()
        

if __name__ == "__main__":
    try:
        a = int(sys.argv[sys.argv.index('-a')+1])
    except:
        a = int(input("Enter the start value:"))

    try:
        n = int(sys.argv[sys.argv.index('-n')+1])
    except:
        n = int(input("Enter the number of terms:"))

    goodstein(a, n)
