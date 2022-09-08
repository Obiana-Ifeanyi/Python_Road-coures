from fib_main import fib, fib_generator


if __name__ == '__main__':
    n = 20
    print (f'The number under the index {n} is {ﬁb(20)}')
    print ('***')

    n = 5
    print (f'The number under the index {n} is {ﬁb(5)}')
    print ('***')

    for i, n in enumerate(ﬁb_generator(5)):
        print (f'Fibonacci number for {i} is {n}')
    print ('***')

    for i, n in enumerate(ﬁb_generator(10)):
        print (f'Fibonacci number for {i} is {n}')
    print ('***')
