# write a program to filter a list of numer which are divisible by 5

def divisible5(n):
    if(n%5==0):
        return True
    return False
a = [1,2,32,45,332,45334,5224,45645,66435,15567,238,250]

f =list(filter(divisible5,a))
print(f)

