def average (numbers):
    """calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)



if __name__ == "__main__":
    sample = [10, 20, 30, 40, 50]

    print("Average:", average(sample))
