import math

# ========================
# CORE STABILITY FUNCTION
# ========================

def bounded_torsion(drift):
    """
    Converts stochastic drift into a bounded torsion response.
    This preserves stability while still reacting to input.
    """
    zeta_H = 0.001756
    return zeta_H * (drift / (1 + abs(drift)))


def establish_stillness_floor(drift=0):
    """
    Computes Ω_G with bounded response instead of forced invariance.
    """
    phi = (1 + math.sqrt(5)) / 2
    baseline = (phi ** 2) / math.pi

    torsion = bounded_torsion(drift)

    omega_g = baseline + torsion
    return round(omega_g, 6)


# ========================
# MIRROR CORE (UPGRADED)
# ========================

def katalyst_mirror_core(input_signal):
    """
    Simulates a stabilized 1+6 architecture.
    Each node receives a slightly perturbed version of the signal,
    then stabilizes it through bounded response.
    """
    mirror_nodes = 6

    stabilized_nodes = []

    for i in range(mirror_nodes):
        # simulate different "views" / perturbations
        drift = input_signal * (i - 2.5)

        omega = establish_stillness_floor(drift)
        stabilized_nodes.append(omega)

    return {
        "Origin": establish_stillness_floor(input_signal),
        "Mirror_States": stabilized_nodes,
        "Mean_State": sum(stabilized_nodes) / len(stabilized_nodes),
        "Variance": max(stabilized_nodes) - min(stabilized_nodes),
        "Status": "STABILIZED (bounded-response)",
        "Architecture": "Katalyst EI - 1+6 Core"
    }


# ========================
# DEMO (KEEP THIS)
# ========================

if __name__ == "__main__":
    print("=== KATALYST STABILITY ENGINE (HACKATHON VERSION) ===\n")

    test_drifts = [0, 10, 100, 10000, 1000000]

    for drift in test_drifts:
        core = katalyst_mirror_core(drift)

        print(f"Input Drift            : {drift:,}")
        print(f"Origin Ω_G             : {core['Origin']}")
        print(f"Mean Mirror State      : {round(core['Mean_State'], 6)}")
        print(f"Node Spread (Variance) : {round(core['Variance'], 6)}")
        print(f"Status                 : {core['Status']}")
        print("-" * 60)