import time

def get_parameters():

    make = input("Enter the make of the vehicle to search: ")
    model = input("Enther the model to search: ")

    return make, model


def result_size_wait(results_size):
    seconds = results_size / 2.0
    print("waiting %5i seconds" % seconds)
    time.sleep(seconds)

