import math

print("점 A의 좌표를 입력하여라: ")
x1 = float(input())
y1 = float(input())

print("점 B의 좌표를 입력하여라: ")
x2 = float(input())
y2 = float(input())

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("두 점 사이의 거리:", d)
