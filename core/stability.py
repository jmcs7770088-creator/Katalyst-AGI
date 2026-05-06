import math

def bounded_torsion(drift):
    zeta_H = 0.001756
    return zeta_H * (drift / (1 + abs(drift)))

def establish_stillness_floor(drift=0):
    phi = (1 + math.sqrt(5)) / 2
    baseline = (phi ** 2) / math.pi
    torsion = bounded_torsion(drift)
    return baseline + torsion