import numpy as np

u = np.array([3, 1])
v = np.array([4, 2])

## produto escalar
u_dot_v = np.dot(u, v)
print("O produto escalar de u e v é:", u_dot_v)

## cos 0
cos_theta = u_dot_v / (np.linalg.norm(u) * np.linalg.norm(v))   
print("O cosseno do ângulo entre u e v é:", cos_theta)

## relação geometrica ente os vetores
if np.isclose(cos_theta, 0):
    print("Os vetores u e v são ortogonais.")   
elif np.isclose(cos_theta, 1):
    print("Os vetores u e v são paralelos.")