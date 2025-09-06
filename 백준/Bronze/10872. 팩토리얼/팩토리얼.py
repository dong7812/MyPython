def main():
    input_value = int(input())
    print(pactorial(input_value))
    
def pactorial(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else :
        return pactorial(n-1) * n
    
if __name__ == "__main__":
    main()