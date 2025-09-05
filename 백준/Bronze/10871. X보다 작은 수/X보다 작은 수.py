import sys

def filter_lt(threshold, line, limit=None):
    nums = list(map(int, line.split()))
    if limit is not None:
        nums = nums[:limit]  # 첫 줄의 a개만 쓰고 싶다면 사용
    result = [str(x) for x in nums if x < threshold]
    return ' '.join(result)

def main():
    lines = sys.stdin.read().splitlines()
    a, b = map(int, lines[0].split())  # 예: "10 5"
    out = filter_lt(b, lines[1], limit=a)
    print(out)

if __name__ == "__main__":
    main()
