def division(a,b):
    try:
        r=a/b
        # print(r)
        return r
    except ZeroDivisionError:
        print("Division by zero is not possible")
        return 0

ans=division(8,4)
print(ans)
ans=division(5,0)
print(ans)