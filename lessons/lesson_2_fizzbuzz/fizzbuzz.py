def fizzbuzz(num):
    output = []
    counter = 1
    while counter <= num:
        if counter % 15 == 0:
            output.append("FizzBuzz")
        elif counter % 5 == 0:
            output.append("Buzz")
        elif counter % 3 == 0:
            output.append("Fizz")
        else:
            output.append(counter)
        counter += 1
    print(output)
    return output
