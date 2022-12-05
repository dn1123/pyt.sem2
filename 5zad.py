import datetime 

min_n = 10
max_n = 100

def get_rand():
    while True:
        number =  datetime.datetime.now().microsecond%50
        if min_n <= number <= max_n:
            return number


n = get_rand()

print(n)
