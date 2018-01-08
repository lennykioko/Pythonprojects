def fizzbuzz(start, upto):

    for number in range(start, upto):
        if number %3 == 0 and number %5 == 0:
            print("Fizzbuzz")
        elif number %3 == 0:
            print("Fizz")
        elif number %5 == 0:
            print("Buzz")
        else:
            print(number)

       
# Call the function with your desired arguements
fizzbuzz(100, 9999)
