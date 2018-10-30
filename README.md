# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instruction](README.md#run-instructions)

# Problem

Create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

# Approach

Programming Language: Python

The approach consists of two steps: first, while reading the data line by line from IO files, create a dictionary to store the accumulative count for each occupation and state; second, use Python built-in sort function for dictionary to get the top 10 occupations and top 10 states.

In the second step, to handle the tie cases, set the counts as the keys of the result dictionaries, and the corresponding states (occupations) as the value of the dictionaries. In case of tie, the states (occupations) can be sorted in the same key.


# Run Instructions

The code accept 7 inputs.
1. path/file of the input dataset
2. path/file to save the output for occupations
3. path/file to save the output for states
4. the number of column which to store visa classes
5. the number of column which to show if the application has been certified
6. the number of column which to store the occupations
7. the number of column which to store the states
The 7 inputs are splitted by ' '.

For example, to get the top 10 Occupations and top 10 States for certified visa applications for 2014 by dataset H1B_FY_2014.csv. The terminal command is

'python H1Bstat.py ./input/H1B_FY_2014.csv ./output/top_10_occupations.txt ./output/top_10_states.txt 5 2 15 22'
