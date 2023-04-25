import statistics

def main():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]

    mean = round(statistics.mean(numbers), 2)
    deviations = [round(x - mean, 2) for x in numbers]
    squared_deviations = [round(x**2, 2) for x in deviations]

    sum_squared_deviations = round(sum(squared_deviations), 2)
    variance = round(sum_squared_deviations / len(numbers), 2)
    std_deviation = round(statistics.stdev(numbers), 2)

    print("\nTable:")
    print("Number\tDeviation\tSquared Deviation")
    for i in range(len(numbers)):
        print(f"{numbers[i]}\t{deviations[i]}\t{squared_deviations[i]}")

    print("\nMean:", mean)
    print("Sum of Squared Deviations:", sum_squared_deviations)
    print("Variance:", variance)
    print("Standard Deviation:", std_deviation)

if __name__ == "__main__":
    main()
