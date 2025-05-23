import numpy as np
from task1 import xor_between_vectors
from task3 import decoder
from task2 import encoder
from task1 import plot_statistic

#i define epsilon and delta as costants
EPSILON = 0.1
DELTA = 0.3

def bsc(input, probability_error):
    #returns an array of the length of the input with [0,1) values
    flip = np.random.rand(len(input)) < probability_error
    output_bits = xor_between_vectors(input, flip.astype(int))
    return output_bits

def number_of_errors(input, output):
    if len(input) != len(output):
        raise ValueError("Array length should be equal")
    errors = 0
    for i in range(len(input)):
        if input[i] != output[i]:
            errors += 1
    return errors


def main():
 

    input = np.random.randint(0, 2, 50)
    legitimate_channel = bsc(input, EPSILON)
    legitimate_channel_errors = number_of_errors(input, legitimate_channel)
    print(f"Legitimate channel errors: {legitimate_channel_errors}")
    eavesdropper_channel = bsc(input, DELTA)
    eavesdropper_channel_errors = number_of_errors(input, eavesdropper_channel)
    print(f"Eavesdropper channel errors: {eavesdropper_channel_errors}")

    errors = 0

    iterations = 50000

    for _ in range(iterations):
        input = np.random.randint(0, 2, 3)
        output = decoder(bsc(encoder(input), EPSILON))
        errors += number_of_errors(input, output)
    print(f"Number of errors in legitimate channel (with epsilon={EPSILON}): {errors}, bit error rate:{errors/(iterations * 3):.3f}")

    errors = 0 
    for _ in range(iterations):
        input = np.random.randint(0, 2, 3)
        output = decoder(bsc(encoder(input), DELTA))
        errors += number_of_errors(input, output)
    print(f"Number of errors in eavesdropper channel (with delta={DELTA}): {errors}, bit error rate: {errors/(iterations * 3):.3f}")


if __name__ == "__main__":
    main()