# first time using regex... had to ask chatGPT tbh
import re

with open("day3.txt", "r") as f:
        # w3schools had txt variable so I did too
        txt = f.read()

        # this is the pattern we are looking for: mul(x,y).
        # need \ before () because () are used to capture and group (\d),
        # so we need to break that to find the text "()"
        # the "+" symbol means there can be one or more digits, refer to w3
        pattern = r"mul\((\d+),(\d+)\)"
        
        # find all the matches from txt file
        matches = re.findall(pattern, txt)

        total_sum = 0

        # for each match, we should have captured two numbers, 
        # hence setting x and y to indexes 0 and 1, respectively
        for match in matches:
                x = int(match[0])
                y = int(match[1])

                total_sum += x*y
        
        print(total_sum)
