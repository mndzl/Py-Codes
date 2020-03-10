for i in range(1, 101):
    ans = str(i)
    if i%3==0:
        ans='Fizz'
        if i%5==0:
            ans+='Buzz'
        print(ans)
        continue

    if i%5==0:
        ans='Buzz'

    print(ans)
