"""
The inputs are
1. path/file of the input dataset
2. path/file to save the output for occupations
3. path/file to save the output for states
4. column number of visa class
5. column number of status
6. column number of occupations
7. column number of states of jobs
The 7 inputs are splited by ' '
"""
import sys
inputs =  sys.argv
FILE_NAME = inputs[1]

OUTPUT_OCC = inputs[2]
OUTPUT_STATE = inputs[3]

COL_visa = int(inputs[4])
COL_status = int(inputs[5])
COL_occ = int(inputs[6])
COL_state = int(inputs[7])

# Build the dictionary to store the accumulative count of each occupation and states
occupation_stat = {}
state_stat = {}
total_certified = 0
total_incidence = 0

with open(FILE_NAME) as f:
    next(f)
    for row in f:
        data = row.split(';')
        if (data[COL_visa].split(' ')[0] in ['H-1B', 'H-1B1','E-3']) and data[COL_status]=='CERTIFIED':
            total_certified += 1
            try:
                occupation_stat[data[COL_occ]] += 1
            except KeyError:
                occupation_stat[data[COL_occ]] = 1
            try:
                state_stat[data[COL_state]] += 1
            except KeyError:
                state_stat[data[COL_state]] = 1

# Use the built-in sorting function for dictionary to get the top 10 states
# To tackle the tie cases, set counts as the keys of the dictionary, the corresponding state as the value.
states_top10 = {}

for state in sorted(state_stat, key=state_stat.__getitem__, reverse=True):
    try:
        list_state = states_top10[state_stat[state]]
        if len(states_top10[state_stat[state]])>0:
            states_top10[state_stat[state]].append(state)
    except KeyError:
        states_top10[state_stat[state]] = [state]

    if len(states_top10)>9:
        break

try:
    f = open(OUTPUT_STATE, 'w+')
    f.seek(0)
    f.truncate()
except FileNotFoundError:
    pass

print("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE", file = open(OUTPUT_STATE, "a"))

n = 0
for count in sorted(states_top10, reverse=True):
    states = sorted(states_top10[count])
    for s in states:
        n += 1
        print("{};{};".format(s, count)+'%.1f'%(round(100*count/total_certified,1))+"%", file = open(OUTPUT_STATE, "a"))
        if n>9:
            break
    if n>9:
        break

# Use the built-in sorting function for dictionary to get the top 10 occupations.
# To tackle the tie cases, set counts as the keys of the dictionary, the corresponding occupation as the value.
occupation_top10 = {}

for occup in sorted(occupation_stat, key=occupation_stat.__getitem__, reverse=True):
    try:
        list_occup = occupation_top10[occupation_stat[occup]]
        if len(occupation_top10[occupation_stat[occup]])>0:
            occupation_top10[occupation_stat[occup]].append(occup.replace("\"","").replace("\"",""))
    except KeyError:
        occupation_top10[occupation_stat[occup]] = [occup.replace("\"","").replace("\"","")]
    if len(occupation_top10)>9:
        break

try:
    f = open(OUTPUT_OCC, 'w+')
    f.seek(0)
    f.truncate()
except FileNotFoundError:
    pass

print("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE", file = open(OUTPUT_OCC, "a"))
n = 0
for count in sorted(occupation_top10, reverse=True):
    occups = sorted(occupation_top10[count])
    for o in occups:
        n += 1
        print("{};{};".format(o, count)+'%.1f'%(round(100*count/total_certified,1))+"%",file = open(OUTPUT_OCC, "a"))
        if n>9:
            break
    if n>9:
        break
