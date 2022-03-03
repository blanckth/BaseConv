#!/usr/bin/python
# Convert The BASE of the Number From another base
import sys

alphaNumArr = [["A", 10], ["B", 11], ["C", 12], ["D", 13],
               ["E", 14], ["F", 15], ["G", 16], ["H", 17],
               ["I", 18], ["J", 19], ["K", 20], ["L", 21],
               ["M", 22], ["N", 23], ["O", 24], ["P", 25],
               ["Q", 26], ["R", 27], ["S", 28], ["T", 29],
               ["U", 30], ["V", 31], ["W", 32], ["X", 33],
               ["Y", 34], ["Z", 35]]


def manUal():
    intro = '\n\n\tThe Alpha Numerical Base Changer in range [2,36] Program written in - P y t h o n - by Salar Muhammadi.\n\n'
    brLine = '8'*88
    mAn = '\n\n\nManual : ./baseChanger.py [Number] [Base of Number(Default : 10)] [Change to Base] \n'
    eX = '\nExample : python baseChanger.py 6119 13 16\n'
    eXres = '\nResult : Number : 6119 from base 13 to 16 is : 343D\n'
    eX2 = '\nExample : python baseChanger.py 6119 2\n'
    eXres2 = '\nResult : Number : 6119 from base 10(Default) to 2 is : 1011111100111\n'
    eX3 = '\nExample : python baseChanger.py SalarMuhammadi 36 13 \n'
    eXres3 = '\nResult : Number : SALARMUHAMMADI from base 36 to 13 is : 33BC410BC8A07B8CB9C5\n'
    eX4 = '\nExample : python baseChanger.py ABC0A08585036C6CC6329 13 26 \n'
    eXres4 = '\nResult : Number : ABC0A08585036C6CC6329 from base 13 to 26 is : 4JI9579D633JNDK7M\n'
    eX5 = '\nExample : python baseChanger.py 17E7 16 10 \n'
    eXres5 = '\nResult : Number : 17E7 from base 16 to 10 is : 6119\n'
    print(
        f"\n\n\t{brLine}{intro}{brLine}{mAn}{eX}{eXres}{eX2}{eXres2}{eX3}{eXres3}{eX4}{eXres4}{eX5}{eXres5}")

# Check The Number wether it match the base


def chkBase(num, base):
    # If Number has not Alphabet Representation
    if base <= 10:
        for i in str(num):
            if(int(i) >= base):
                return False
        return True
    # Alphabetical Method Check Base
    else:
        mFind = False
        for i in str(num):
            # Else its True because we have the range larger than any number
            if not i.isnumeric():
                # Search the List of alpha numerical
                for a in range(base-10):
                    if i.upper() == alphaNumArr[a][0]:
                        mFind = True
                        break
                if not mFind:
                    return False
        return True

# Method to Change the number From any base to General Base 10


def baseToTen(num, base):
    revNum = str(num)[::-1]
    tenBaseNum = 0
    placeCounter = 0
    for z in revNum:
        if z.isnumeric():
            tenBaseNum += (int(z) * (base ** placeCounter))
            placeCounter += 1
        else:
            for a in range(base-10):
                if z.upper() == alphaNumArr[a][0]:
                    rn = int(alphaNumArr[a][1])
                    tenBaseNum += rn * (base ** placeCounter)
                    placeCounter += 1
                    break
    return tenBaseNum


# Method to Change Any Number From base 10 to Any base in the range of [2,36]


def tenToBase(num, base):
    convertedNum = ''
    tenBase = num
    while tenBase > 0:
        tbR = tenBase % base
        if tbR < 10:
            convertedNum += str(tbR)
        else:
            repTBR = alphaNumArr[tbR-10][0]
            convertedNum += str(repTBR)
        tenBase //= base
    return convertedNum[::-1]

# Method to combine methods and Convert any BASE to Another one


def baseChanger(num, base, conv):
    number = num
    if base != 10:
        number = baseToTen(number, base)
        if conv == 10:
            return number
    number = tenToBase(number, conv)
    return number

# Main Program Function


def main():
    # Count of Input Argumant of the Program
    sysArgLen = len(sys.argv)
    # HELP Option with just Run the Program
    if sysArgLen < 2:
        manUal()  # HELP
        sys.exit(0)
    # Argument Error For Low or higher than the range of args count [2,3]
    elif sysArgLen > 4 or sysArgLen < 3:
        print("\nNumber and the Base to convert is Required!")
        manUal()
        sys.exit(0)
    mainNum = sys.argv[1]  # First Argument for Main Number
    # check wether the Number is Alpha Numerical or not
    if not mainNum.isalnum():
        print("\nThe Number is not Valid!")
        manUal()
        sys.exit(0)
    # Three Argument Method
    if sysArgLen == 4:
        try:
            baseNum = int(sys.argv[2])  # Second Args for Base of Number
            convBase = int(sys.argv[3])  # Third Args for Convert Base
            # check the base(s) Range
            if baseNum > 36 or baseNum < 2 or convBase > 36 or convBase < 2:
                print("\nThe Base must be a number between [2 , 36] !")
                manUal()
                sys.exit(0)
        # Error if the base(s) is not Digit
        except:
            print("\nThe Base must be a number between [2 , 36] !")
            manUal()
            sys.exit(0)
        if baseNum <= 10:
            try:
                mainNum = int(mainNum)
            except:
                print("\nNumber must be digit in the base lower than or equal 10")
                manUal()
                sys.exit(0)
    # Two Argument Method
    elif sysArgLen == 3:
        try:
            convBase = int(sys.argv[2])  # Second Args for Convert Base
            # check the base Range
            if int(convBase) > 36 or int(convBase) < 2:
                print("\nThe Base must be a number between [2 , 36] !")
                manUal()
                sys.exit(0)

            baseNum = 10  # Default Base to General 10
        except:
            print("\nThe Base must be a number between [2 , 36] !")
            manUal()
            sys.exit(0)
        try:
            mainNum = int(mainNum)
        except:
            print("\nNumber must be digit in the base of 10")
            manUal()
            sys.exit(0)
    # Check the Number to match the base : the Numbers Digits and represented value must be lower than the base it self
    if not chkBase(mainNum, baseNum):
        print("\nThe Number is not match with Base !")
        manUal()
        sys.exit(0)
    # Convert The Number
    finalNumber = baseChanger(mainNum, baseNum, convBase)
    # Print the result
    print('\n Number : ' + str(mainNum) + ' from base ' +
          str(baseNum) + ' to ' + str(convBase) + ' ==> ' + str(finalNumber))
    print()


# the program.
if __name__ == "__main__":
    main()
