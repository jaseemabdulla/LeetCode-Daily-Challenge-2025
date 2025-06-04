arr = [1,2,34,3,4,5,7,23,12]

c = 0
def f(arr):
    c = 0
    for i in arr:
        if i % 2 != 0:
            c += 1
        elif i % 2 == 1:
            c = 0
        if c == 3:
            return True 
    return False

print(f(arr))
    
  