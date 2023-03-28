if __name__ == '__main__':
    n = int(input())
    suite = [i for i in range(n+1)]
    for value in suite:
        if value > 0:
            print(suite[value], end='')
