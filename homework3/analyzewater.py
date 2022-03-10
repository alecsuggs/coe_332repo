#!/usr/bin/env python3

import json
import logging

logging.basicConfig(level=logging.INFO)


def turbidity(const: float, current: float) -> float:
    """calculates the current turbidity

    This function calculates the turbidity in NTU (0-40) of the water in the Mars laboratory
    by using the calibration constant and detector current.

    :param const (float): Calibration constant of nephelometer
    :param current (float): Ninety degree detector current
    :return (float): T: Turbidity in NTU
    """
    T = const * current
    return T


def issafe(thresh: float, cur: float, decay: float, hours: float) -> bool:
    """water safe true or false

    This function returns a false value if the water turbidity is greater
    than or equal to the turbidity threshold. If the water is below the threshold
    turbidity then it is safe and the function returns a true value.

    :param thresh (float): The turbidity threshold of safe water
    :param cur (flaot): The current turbidity of the Lab water
    :param decay (float): The decay factor per hour expressed as a decimal
    :param hours (float): The time elapsed in hours
    :return issafe (bool): true or false output, true for safe false for unsafe
    """
    if thresh <= (cur * (1 - decay) ** hours):
        return False
    else:
        return True


def threshold(thresh: float, cur: float, decay: float) -> float:
    """calculates the minimum time until safe

    This function calculates the minimum time required for the water to be below
    the safety threshold

    :param thresh (float): The turbidity threshold of safe water
    :param cur (flaot): The current turbidity of the Lab water
    :param decay (float): The decay factor per hour expressed as a decimal
    :return hours (float): The minimum time required until the water is safe again
    """
    hours = 0
    while thresh <= (cur * (1 - decay) ** hours):
        hours = hours + 0.1
    return hours


def main():
    Ts = 0
    decay = 0.02
    thresh = 1.0
    with open('turbidity_data.json', 'r') as f:
        turb = json.load(f)
    for i in range(5):
        T = turbidity(turb["turbidity_data"][-i]["calibration_constant"],
                      turb["turbidity_data"][-i]["detector_current"])
        Ts = Ts + T
    Ts = Ts/5
    if issafe(thresh, Ts, decay, 0):
        print('Average turbidity based on five most recent measurements', Ts)
        logging.info(' Turbidity is below threshold for safe use')
        print('Minimum time required to return below a safe threshold = 0')
    else:
        print('Average turbidity based on five most recent measurements', Ts)
        logging.warning(' Turbidity is above threshold for safe use')
        print('minimum time required to return below threshold = ', threshold(thresh, Ts, decay), " hours")

if __name__ == '__main__':
    main()
