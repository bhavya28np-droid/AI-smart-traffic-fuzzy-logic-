# AI-Based Smart Traffic Signal Using Fuzzy Logic

A simple Python mini-project demonstrating **Fuzzy Logic** for dynamic traffic-signal timing.

## Idea

Instead of using a fixed green-light duration, the system considers:

- Traffic density
- Waiting time

and recommends a suitable green-light duration.

## Fuzzy Categories

### Traffic Density
- Low
- Medium
- High

### Waiting Time
- Short
- Medium
- Long

### Output
- Green-light duration: 20–60 seconds

## Example Rule

**IF traffic is HIGH AND waiting time is LONG → green-light duration is 60 seconds.**

The program uses fuzzy membership functions, IF-THEN rules, the minimum operator for AND conditions, and weighted-average defuzzification.

## Sample Output

```text
Traffic= 15% | Waiting= 10 | Green= 20.0s
Traffic= 50% | Waiting= 50 | Green= 40.0s
Traffic= 90% | Waiting= 90 | Green= 60.0s
```

## Run

Requires Python 3.8+.

```bash
python main.py
```

No external libraries are required.

## Project Structure

```text
smart-traffic-fuzzy-logic/
├── main.py
├── README.md
└── requirements.txt
```

## Future Scope

- Real-time traffic sensors
- Camera-based vehicle detection
- IoT integration
- Coordination between multiple signals
- Computer-vision based traffic estimation

> This is an educational simulation and does not directly control real traffic signals.
