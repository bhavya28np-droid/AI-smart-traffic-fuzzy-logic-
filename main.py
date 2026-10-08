# AI-Based Smart Traffic Signal Using Fuzzy Logic
# Educational mini-project

def left_shoulder(x, a, b):
    if x <= a: return 1.0
    if x >= b: return 0.0
    return (b - x) / (b - a)

def right_shoulder(x, a, b):
    if x <= a: return 0.0
    if x >= b: return 1.0
    return (x - a) / (b - a)

def triangular(x, a, b, c):
    if x <= a or x >= c: return 0.0
    if x == b: return 1.0
    if x < b: return (x - a) / (b - a)
    return (c - x) / (c - b)

def fuzzify_traffic(x):
    return {
        "low": left_shoulder(x, 20, 50),
        "medium": triangular(x, 20, 50, 80),
        "high": right_shoulder(x, 50, 80)
    }

def fuzzify_waiting(x):
    return {
        "short": left_shoulder(x, 20, 50),
        "medium": triangular(x, 20, 50, 80),
        "long": right_shoulder(x, 50, 80)
    }

def fuzzy_controller(traffic_density, waiting_time):
    traffic = fuzzify_traffic(traffic_density)
    waiting = fuzzify_waiting(waiting_time)

    # IF traffic AND waiting THEN green-light duration
    rules = [
        ("low", "short", 20), ("low", "medium", 25), ("low", "long", 35),
        ("medium", "short", 30), ("medium", "medium", 40), ("medium", "long", 50),
        ("high", "short", 40), ("high", "medium", 50), ("high", "long", 60)
    ]

    numerator = denominator = 0.0
    active_rules = []

    for t, w, output in rules:
        strength = min(traffic[t], waiting[w])
        if strength > 0:
            numerator += strength * output
            denominator += strength
            active_rules.append((t, w, strength, output))

    green_time = numerator / denominator if denominator else 20.0
    return green_time, traffic, waiting, active_rules

def main():
    print("=" * 60)
    print("AI-BASED SMART TRAFFIC SIGNAL USING FUZZY LOGIC")
    print("=" * 60)

    # Demonstration cases
    for density, wait in [(15, 10), (50, 50), (90, 90)]:
        green, _, _, _ = fuzzy_controller(density, wait)
        print(f"Traffic={density:>3}% | Waiting={wait:>3} | Green={green:>5.1f}s")

    print("\nEnter your own values:")
    try:
        density = float(input("Traffic density (0-100): "))
        wait = float(input("Waiting time (0-100): "))

        if not (0 <= density <= 100 and 0 <= wait <= 100):
            raise ValueError

        green, traffic, waiting, active = fuzzy_controller(density, wait)

        print("\nTraffic membership:", {k: round(v, 2) for k, v in traffic.items()})
        print("Waiting membership:", {k: round(v, 2) for k, v in waiting.items()})
        print(f"Recommended green-light duration: {green:.1f} seconds")

        print("\nActive fuzzy rules:")
        for t, w, strength, output in active:
            print(f"IF traffic={t} AND waiting={w} -> {output}s "
                  f"(strength={strength:.2f})")

    except ValueError:
        print("Please enter valid values from 0 to 100.")

if __name__ == "__main__":
    main()
