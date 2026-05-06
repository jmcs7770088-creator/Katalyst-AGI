from core.stability import establish_stillness_floor

def stabilize_signal(x):
    return x / (1 + abs(x))

def run_agent(input_value):
    omega = establish_stillness_floor(input_value)

    stabilized = stabilize_signal(input_value)

    return {
        "input": input_value,
        "omega": omega,
        "stabilized": stabilized
    }