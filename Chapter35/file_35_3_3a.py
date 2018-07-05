LAKES = 20

names = [None] * LAKES
depths = [None] * LAKES
countries = [None] * LAKES
areas = [None] * LAKES

for i in range(LAKES):
    names[i] = input()
    depths[i] = float(input())
    countries[i] = input()
    areas[i] = float(input())

maximum = depths[0]
m_name = names[0]
m_country = countries[0]
m_area = areas[0]
for i in range(1, LAKES):
    if depths[i] > maximum:
        maximum = depths[i]
        m_name = names[i]
        m_country = countries[i]
        m_area = areas[i]
        
print(maximum, m_name, m_country, m_area)