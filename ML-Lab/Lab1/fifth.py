#used inbuilt functions for mode,mean,median and used random for random number generation
import random     
import statistics

def random_numbers():
    no = 100
    res = random.choices(range(100, 151), k=no)
    print("Random Numbers:\n", res)


    mean_val = statistics.mean(res)
    median_val = statistics.median(res)
    mode_val = statistics.mode(res)

    print(f"\nMean: {mean_val}")
    print(f"Median: {median_val}")
    print(f"Mode: {mode_val}")

def main():
    random_numbers()

if __name__ == "__main__":
    main()