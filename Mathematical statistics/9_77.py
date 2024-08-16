Ai = [-7.5600, -6.8810, -6.2020, -5.5230, -4.8440, -4.1650, -3.4860, -2.8070, -2.1280, -1.4490]
Bi = [-6.8810, -6.2020, -5.5230, -4.8440, -4.1650, -3.4860, -2.8070, -2.1280, -1.4490, -0.7700]

p_j = [0.1188, 0.1089, 0.1089, 0.0792, 0.0495, 0.0990, 0.0990, 0.1485, 0.1089, 0.0693]

pj = [(Bi[i] + 2.7735) / 1.2436 - (Ai[i] + 2.7735) / 1.2436 for i in range(len(Ai))]

result = [((p_j[i] - pj[i]) ** 2) / pj[i] for i in range(len(pj))]

for value in result:
    print(value)

print(sum(p_j))    
print(sum(pj))
print(sum(result))

data = [-4.97, -4.93, -4.85, -4.78, -4.75, -4.37, -4.34, -4.18, -3.98,
        -3.94, -3.94, -3.87, -3.85, -3.78, -3.77, -3.66, -3.64, -3.51, -3.35, -3.31, -3.12, -3.10, -3.03, -2.98, -2.95,
        -2.92, -2.92, -2.87, -2.79, -2.79, -2.77, -2.74, -2.60, -2.59, -2.56, -2.49, -2.48, -2.48, -2.45, -2.44, -2.29,
        -2.26, -2.20, -2.04, -2.01, -1.92, -1.87, -1.85, -1.85, -1.83, -1.57, -1.57, -1.56, -1.51, -1.44, -1.32, -1.29,
        -1.17, -1.05, -0.94, -0.81, -0.77]

print(len(data))        
