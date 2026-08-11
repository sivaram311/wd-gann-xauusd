"""
W.D. Gann utility functions for XAUUSD
-------------------------------------
Simple, pure-Python implementations of:
- Square of Nine price projections
- Scaled Gann angle levels (for day-trading and swing)

These are research helpers, not a full trading engine.
"""

import math
from typing import List, Tuple


def square_of_nine_levels(origin: float, steps: int = 8) -> List[float]:
    """
    Generate approximate Square of Nine levels around an origin price.

    Classic Gann Square of Nine is a spiral. For practical trading we
    generate the cardinal and near-cardinal levels using the square-root
    method commonly used by modern practitioners:

        level = (sqrt(origin) ± n * 0.125 or 0.25)^2

    Returns a sorted list of levels above and below the origin.
    """
    if origin <= 0:
        raise ValueError("Origin must be positive")

    root = math.sqrt(origin)
    levels = set()

    # 0.125 and 0.25 increments cover many of the important rotations
    for n in range(1, steps + 1):
        for delta in (0.125, 0.25, 0.5, 1.0):
            levels.add(round((root + n * delta) ** 2, 2))
            levels.add(round((root - n * delta) ** 2, 2))

    # Always include the origin itself
    levels.add(round(origin, 2))
    return sorted(l for l in levels if l > 0)


def gann_angle_price(
    origin_price: float,
    origin_bar: int,
    current_bar: int,
    angle: str = "1x1",
    scale: float = 2.5,
) -> float:
    """
    Project a Gann angle price at a future (or past) bar.

    Parameters
    ----------
    origin_price : float
        Price of the pivot (PDL, PDH, swing high/low)
    origin_bar : int
        Bar index of the pivot (0 = first bar)
    current_bar : int
        Bar index where we want the angle value
    angle : str
        One of "1x1", "2x1", "1x2", "3x1", "1x3", "4x1", "1x4"
    scale : float
        Price units per bar for the 1x1 angle.
        For Gold day-trading a value between 2.0–3.5 is typical on H1.
        For Daily charts a larger scale (e.g. 8–15) is usually needed.

    Returns
    -------
    float : projected price of the angle at current_bar
    """
    ratios = {
        "1x1": 1.0,
        "2x1": 2.0,
        "1x2": 0.5,
        "3x1": 3.0,
        "1x3": 1.0 / 3.0,
        "4x1": 4.0,
        "1x4": 0.25,
    }
    if angle not in ratios:
        raise ValueError(f"Unsupported angle: {angle}")

    bars_elapsed = current_bar - origin_bar
    move = bars_elapsed * scale * ratios[angle]

    # Rising angle from a low, falling from a high — caller decides sign
    return origin_price + move


def rising_angles_from_low(
    low_price: float,
    low_bar: int,
    current_bar: int,
    scale: float = 2.5,
) -> dict:
    """Convenience: all common rising angles from a low."""
    return {
        a: gann_angle_price(low_price, low_bar, current_bar, a, scale)
        for a in ["1x1", "2x1", "1x2", "3x1", "1x3"]
    }


def falling_angles_from_high(
    high_price: float,
    high_bar: int,
    current_bar: int,
    scale: float = 2.5,
) -> dict:
    """Convenience: all common falling angles from a high."""
    # For falling angles we subtract the move
    result = {}
    for a in ["1x1", "2x1", "1x2", "3x1", "1x3"]:
        # Re-use the function then invert the direction
        up = gann_angle_price(high_price, high_bar, current_bar, a, scale)
        move = up - high_price
        result[a] = high_price - move
    return result


if __name__ == "__main__":
    # Quick demo
    print("Square of Nine around 4380:")
    levels = square_of_nine_levels(4380, steps=5)
    print(levels[:12], "...")

    print("\nRising 1x1 from 4313 at bar 0, evaluated at bar 12 (scale=2.5):")
    print(gann_angle_price(4313, 0, 12, "1x1", scale=2.5))
