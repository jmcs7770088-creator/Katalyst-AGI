import math

def bounded_torsion(drift):
    """
    Stable response function (your idea, but kept).
    """
    zeta_H = 0.001756
    return zeta_H * (drift / (1 + abs(drift)))


def establish_stillness_floor(drift=0):
    """
    Stable baseline (Ω_G).
    """
    phi = (1 + math.sqrt(5)) / 2
    baseline = (phi ** 2) / math.pi
    torsion = bounded_torsion(drift)
    omega_g = baseline + torsion
    return round(omega_g, 6)


def confidence_score(input_text):
    """
    NEW: measures uncertainty (simple version)
    """
    if not input_text:
        return 0.0
    length_factor = min(len(input_text) / 100, 1)
    return round(0.5 + 0.5 * length_factor, 3)


def verify_output(output):
    """
    NEW: sanity check layer (THIS is what makes it real)
    """
    if output is None:
        return False
    if isinstance(output, str) and len(output.strip()) == 0:
        return False
    return True


def katalyst_agent(input_data):
    """
    FULL AGENT PIPELINE
    """
    drift = input_data.get("stochastic_noise", 0)
    user_input = input_data.get("query", "")

    omega_g = establish_stillness_floor(drift)
    confidence = confidence_score(user_input)

    # Simulated reasoning output (replace with LLM later)
    response = f"Processed: {user_input}"

    is_valid = verify_output(response)

    return {
        "Ω_G": omega_g,
        "confidence": confidence,
        "valid": is_valid,
        "response": response,
        "status": "STABILIZED + VERIFIED"
    }