
def timeInWords (hour,minute):
# For hours and minutes, arrays were created in which the number of each index was written in words.
     hoursInWords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                     "twelve"]

     minutesInWords = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
                       "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
                       "twenty one","twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
                       "twenty eight", "twenty nine", "half"]

# Strings were created according to the conditions that the time is full hour, before half, at half, and after half.
     if minute==0:
        print(hoursInWords[hour] + " o'clock")

     elif minute<30:
        print(minutesInWords[minute] + " minutes past " + hoursInWords[hour])

     elif minute>30:
        # If the minute passes halfway, it's converted so we can name it.
        minute=60-minute
        print(minutesInWords[minute]+ " minutes to " + hoursInWords[hour+1])

     elif minute==30:
        print(minutesInWords[minute] + " minutes past " + hoursInWords[hour])

     else:
         print('Unexpected error occurred.')
         exit()

# After creating our function, we get inputs for hours and minutes, respectively.
h = int(input())

# If a value between 1 and 23 is not entered, a message and code is given to the output.
if h < 1 or h > 23:
     print('The code exits because you did not enter a number range between 1 and 23.')
     exit()

# Converting 24 hour time to 12 hour time.
if (h > 12):
    h = h - 12

m = int(input())

# If a value between 0 and 59 is not entered, a message and code is given to the output.
if m < 0 or m > 59:
    print('The code exits because you did not enter a number range between 0 and 59.')
    exit()

# Function called.
timeInWords(h,m)













