# Initial attempt:
# Time Complexity: O(R x L), where R is reports and L is levels. 
#                  Closer to O(R x K), where K is the number of comparisons before failure
#                  because of the early checks before continuing
# Space Complexity: O(R x L) becuase I store all the reports AND levels
with open("day2.txt", "r") as file:
    safe = 0
    reports = []

    for line in file:
        # make a list of each report
        levels = list(map(int, line.split()))
        reports.append(levels)

    for i in range(len(reports)):
        # initialize 
        increasing = False
        decreasing = False
        is_safe = True
        for levels in range(len(reports[i])-1):

            difference = reports[i][levels + 1] - reports[i][levels]
            
            # if increase or decrease is out of range, it's not safe
            if not (-3 <= difference <= -1 or 1 <= difference <= 3):
                is_safe = False
                break

            # if level i is less than level i+1 and difference is less than 3, it is increasing
            if reports[i][levels] < reports[i][levels+1]:
                # if decreasing, that means its unsafe since ALL have to be increasing to be safe
                if decreasing == True:
                    is_safe = False
                    break
                increasing = True
            # if level i is greater than level i+1 and difference is less than 3, it is decreasing
            elif reports[i][levels] > reports[i][levels+1]:
                # if decreasing, that means its unsafe since ALL have to be decreasing to be safe
                if increasing == True:
                    is_safe = False
                    break
                decreasing = True
    
        # if the report is still marked as safe, then it passed all checks
        if is_safe:
            safe += 1 

    print (safe)

#chatGPT approach:
# time complexity: O(R x L) still because of the two for loops
# space complexity: O(L) because it processes reports line by line, rather than storing all reports
with open("day2.txt", "r") as file:
    safe = 0  # Counter for safe reports

    for line in file:
        levels = list(map(int, line.split()))

        # Assume the report is safe initially
        increasing = True
        decreasing = True

        for i in range(len(levels) - 1):
            diff = levels[i + 1] - levels[i]

            # Check if the difference is invalid
            if not (-3 <= diff <= -1 or 1 <= diff <= 3):
                increasing = decreasing = False
                break

            # Update flags based on the trend
            if diff > 0:
                decreasing = False
            elif diff < 0:
                increasing = False

        # Count as safe if the report meets criteria
        if increasing or decreasing:
            safe += 1

    print(safe)