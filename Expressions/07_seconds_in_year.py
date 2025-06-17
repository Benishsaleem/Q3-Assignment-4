DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_HOUR = 60

def main():
    total_seconds = DAYS_PER_YEAR *  HOURS_PER_DAY *  MIN_PER_HOUR *  SEC_PER_HOUR 
    
    print(f"Total Seconds in a Year are {total_seconds}")
    
if __name__ == "__main__":
    main()