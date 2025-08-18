
# finally exception will work in every case. As in function too
def main():
    try:
        a= int(input("enter your no.:" ))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("I'm inside finally:")

    print("I'm inside finally")
    



main()

