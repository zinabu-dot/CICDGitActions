def while_loop(a: int) -> int:
    b = 0
    while a < 10:
        b += a
        a += 1  # Increment 'a' to eventually break the loop
    return b


def main():
    forward_sum = while_loop(6)
    looped_sum = while_loop(0)
    print(forward_sum+looped_sum)


main()
