if __name__ == '__main__':
    n = int(input())
    i = n
    list_int = [i*i for i in range(n)]
    for value in list_int:
        print(value)
