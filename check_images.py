# Name: Joy Tari-Bagshaw
# Date: 14th November, 2024

from time import time, sleep  # Importing required functions

def main():
    """
    Main function that times the program's execution and outputs the runtime.
    """
    # TODO: 0: Timing Code - Record Start Time
    start_time = time() 

    # Simulating program execution with sleep (Replace sleep with actual code later)
    sleep(10) 

    # TODO: 0: Timing Code - Record End Time
    end_time = time()  

    # Calculate Total Runtime
    tot_time = end_time - start_time

    # Print Total Runtime in Seconds
    print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")

    # Print Total Runtime in hh:mm:ss format
    print("\nTotal Elapsed Runtime (formatted):", 
          str(int(tot_time / 3600)).zfill(2) + ":" +
          str(int((tot_time % 3600) / 60)).zfill(2) + ":" +
          str(int(tot_time % 60)).zfill(2))

if __name__ == "__main__":
    main()
