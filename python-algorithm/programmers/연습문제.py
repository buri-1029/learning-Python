# 정수 내림차순으로 배치하기
def solution1(n):
    return int(''.join(sorted(str(n), reverse=True)))

# 콜라츠 추측


def solution2(num):
    answer = 0
    while(num != 1):
        if num % 2 == 0:
            num = num//2
            answer += 1
        else:
            num = num*3 + 1
            answer += 1
    return answer if answer < 500 else -1


# 하샤드 수
def solution3(x):
    return not (x % sum([int(i) for i in str(x)]))


# 핸드폰 번호 가리기
def solution4(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[-4:]


# 문자열 내 마음대로 정렬하기
def solution5(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x: x[n])


# 시저 암호
def solution6(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif 97 <= ord(s[i]) <= 122:
            answer += chr(((ord(s[i])+n-97) % 26 + 97))
        else:
            answer += chr((ord(s[i])+n-65) % 26 + 65)
    return answer


# 약수의 합
def solution7(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    return sum

# 자연수 뒤집어 배열로 만들기


def solution8(n):
    return [int(i) for i in str(n)][::-1]

# arr=[]
# for i in str(n):
#   arr.append(int(i))
# print(arr[::-1])
