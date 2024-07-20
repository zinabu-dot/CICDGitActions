def while_loop(a: int) -> int:
    b = 0
    while a < 10:
        b+=a
        a+=1
    return b

if__name__ == '__main__':
    forward_sum = while_loop(6)
    print(forward_sum)
    
