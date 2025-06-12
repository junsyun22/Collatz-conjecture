import json

def print_collatz_typography():
    art = r'''
  ____      _ _       _       
 / ___|___ | | | __ _| |_ ____
| |   / _ \| | |/ _` | __|_  /
| |__| (_) | | | (_| | |_ / / 
 \____\___/|_|_|\__,_|\__/___|
'''
    print(art)

def print_manual():
    manual = """
    === Collatz 프로그램 매뉴얼 ===
    1: 십진수 경로 출력 모드
    2: 이진수 경로 출력 모드
    0: 종료
    """
    print(manual)

def collatz_sequence_decimal(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

def collatz_sequence_binary(n):
    sequence = []
    while n != 1:
        sequence.append(bin(n)[2:])
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append('1')
    return sequence

def run_decimal_mode():
    while True:
        print_manual()
        try:
            n = int(input("숫자 n을 입력하세요 (종료: 0): "))
            if n == 0:
                break
            sequence = collatz_sequence_decimal(n)
            print(f"십진수 경로: {' → '.join(map(str, sequence))}")
            print(f"총 {len(sequence)-1}단계 만에 1에 도달합니다.")
        except ValueError:
            print("유효한 정수를 입력해주세요.")

def run_binary_mode():
    while True:
        print_manual()
        try:
            n = int(input("숫자 n을 입력하세요 (종료: 0): "))
            if n == 0:
                break
            sequence = collatz_sequence_binary(n)
            print(f"이진수 경로: {' → '.join(sequence)}")
            print(f"총 {len(sequence)-1}단계 만에 1에 도달합니다.")
        except ValueError:
            print("유효한 정수를 입력해주세요.")

def main():
    print("Collatz 추측 분석기")
    print_collatz_typography()
    print_manual()
    while True:
        choice = input("모드를 선택하세요 (1, 2, 0): ")
        if choice == '1':
            print("십진수 경로 출력 모드로 진입합니다.")
            run_decimal_mode()
        elif choice == '2':
            print("이진수 경로 출력 모드로 진입합니다.")
            run_binary_mode()
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효한 선택이 아닙니다. 다시 입력해주세요.")

if __name__ == '__main__':
    main()
