import csv
import sys
import re


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit('usage: python dna.py CSV txt')

    csvfile = sys.argv[1]
    txtfile = sys.argv[2]
    data= []
    dnas = []
    match = {}
    # TODO: Read database file into a variable
    with open(csvfile, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    with open(txtfile, 'r') as tfile:
        text = tfile.read()

    row1 = reader.fieldnames
    n = len(data)
    m = len(row1)

    for i in range(1,m,1):
        lm = longest_match(text, row1[i])
        match[row1[i]] = (lm)

    count = 0
    for j in range(n):
        for k in range(1,m,1):
            r = row1[k]
            if int(data[j][r]) == int(match[r]):
                count+=1
            if int(data[j][r]) != int(match[r]):
                count = 0
            if count == m-1:
                print(data[j]['name'])
                exit(0)
    print('No Match')













    # TODO: Read DNA sequence file into a variable

    # TODO: Find longest match of each STR in DNA sequence

    # TODO: Check database for matching profiles

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
