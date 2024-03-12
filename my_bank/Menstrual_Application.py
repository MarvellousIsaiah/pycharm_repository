from calendar import month
from datetime import datetime, timedelta


class MenstrualFlowCalculator:
        def __init__(self):
            pass

        def collectAgeRange(self):
            pass

        def displayMonths(self):
            return input("Please enter from (01 for January) - 12 for December: ")

        def collectRangeOfFlow(self):
            return int(input("Please enter the range of your menstrual flow (1-8): "))

        def setCycleLength(self):
            return int(input("Please enter the length of your menstrual cycle: "))

        def getPreviousFlowDate(self, year, month, day):
            return datetime(int(year), int(month), int(day))

        def getNextFlowDate(self, cycle_length):
            return self.getPreviousFlowDate(year, month, day) + timedelta(days=cycle_length)

        def getOvulationDate(self, start_date):
            return start_date + timedelta(days=14)

        def displayFertileWindow(self, start_date):
            fertile_start = start_date + timedelta(days=10)
            fertile_end = start_date + timedelta(days=16)
            return fertile_start, fertile_end

        def displaySafePeriod(self, start_date, range_of_flow, cycle_length):
            safe_start = start_date + timedelta(days=range_of_flow)
            safe_end = start_date + timedelta(days=cycle_length)
            return safe_start, safe_end

    if __name__ == "__main__":
        flowCalculator = MenstrualFlowCalculator()

        print("Welcome to Your Period Tracker")

        year = input("What is the year of your last flow (e.g. 2024): ")
        while True:
            try:
                converted_year = int(year)
                if 1990 <= converted_year <= 2025:
                    break
                else:
                    year = input("Please enter a recent and valid year: ")
            except ValueError:
                year = input("Please enter a valid year (e.g. 2024): ")





