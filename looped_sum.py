def while_loop(a: int) -> int:
    b = 0
    while a < 10:
        b += a
        a += 1  # Increment 'a' to eventually break the loop
    return b


forward_sum = while_loop(6)
print(forward_sum)
