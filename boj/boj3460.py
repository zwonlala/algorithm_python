t = int(input());
for _ in range(t):
    var = int(input());
    idx = 0;
    while not var == 0 :
        if var%2 == 1:
            print(idx, end=' ');
        idx += 1;
        var //= 2;
    print();
