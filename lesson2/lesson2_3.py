A = 10
B = 50
C = 30

cond_1 = ( A < 45 ) and (B >= 45) and (C >= 45)
cond_2 = ( A >= 45 ) and (B < 45) and (C >= 45)
cond_3 = ( A >= 45 ) and (B >= 45) and (C < 45)

print(cond_1 or cond_2 or cond_3)
