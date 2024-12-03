# Day 2: Red-Nosed Reports
def part1():
    with open("input.txt", "r") as input:
        increasing = None
        safe_ct = 0
        for line in input:
            report = line.split()
            safe = True
            for i in range(1, len(report)):
                if i == 1:
                    increasing = int(report[i-1]) < int(report[i])
                else:
                    if (int(report[i-1]) < int(report[i])) != increasing:
                        safe = False
                        break
                
                diff = abs(int(report[i]) - int(report[i-1]))
                if diff < 1 or diff > 3:
                    safe = False
                    break
            
            if safe: safe_ct += 1
    
    print(f'There are {safe_ct} safe reports.')

def part2():
    def is_safe(report):
        """
        Check if the report is safe without any modifications.
        """
        increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
        decreasing = all(-3 <= report[i+1] - report[i] <= -1 for i in range(len(report) - 1))
        return increasing or decreasing

    def can_be_safe_with_dampener(report):
        """
        Check if the report can be made safe by removing one level.
        """
        for i in range(len(report)):
            # Create a modified report with one level removed
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                return True
        return False
    
    with open("input.txt", "r") as input:
        safe_ct = 0  # Initialize the count of safe reports

        for line in input:
            report = list(map(int, line.split()))  # Parse the line into a list of integers
            
            # Check if the report is safe or can be made safe with the dampener
            if is_safe(report) or can_be_safe_with_dampener(report):
                safe_ct += 1

        print("Number of safe reports:", safe_ct)



if __name__ == '__main__':
    # part1()
    part2()