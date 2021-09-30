for _ in range(int(input())):
    candy, child = map(int, input().split())
    print('You get {} piece(s) and your dad gets {} piece(s).'.format(candy // child, candy % child))