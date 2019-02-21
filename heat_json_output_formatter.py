""" 
This script format the output of heat output-show command into usable json format.
The idea is to format the output based on our needs, since 'heat output-show --format json' 
command does not provide valid json 
heat --insecure output-show ${STACK_NAME} --format json --all | more > deployment_tool_stack_output.json
"""

import json
import os
import ast

# Format the first outcome from output and convert it to a readable json file
temp_file = "json_output_tmp.json"
f1 = open('./deployment_tool_stack_output.json', 'r')
f2 = open(temp_file, 'w+')
previous_line = ''

f2.write('[')
for line in f1:
    temp = line
    if previous_line.strip() == '}' and temp.strip() == '{':
        f2.write(',' + line.strip())
    elif temp.strip() == '}{':
        f2.write('},{')
    else:
        f2.write(line.strip())
    previous_line = line
f2.write(']')
f2.close()
f1.close()

# With json load it will verify that the change gives valid json
with open(temp_file) as formatted_file:
    config = json.load(formatted_file)

json_list = json.loads(json.dumps(config))

for idx, element in enumerate(json_list):
    element[element['output_key']] = element['output_value']
    del element['output_value']
    del element['output_key']
    del element['description']

data = 'valid.json'
with open(data, 'w') as outfile:
    json.dump(json_list, outfile, indent=4, sort_keys=True)

# Creation of separate json and yaml files

valid_file ='./valid.json'
with open(valid_file) as formatted_file:
    formmatted = json.load(formatted_file)

jsonstring  = ''

with open('all-envs-and-hosts.yml', 'w+') as outfile:
    outfile.write('env: ' + '\n')
    outfile.write('  '+'deployment1: ' + '\n')
    i = 0
    for line in formmatted:
        line = str(line)
        if i == 0:
            jsonstring = jsonstring + line.replace("'", "\"").replace("{", "").replace("}", "")
        else:
            jsonstring = jsonstring + ',' + line.replace("'", "\"").replace("{", "").replace("}", "")
        i = i + 1
        line = line.replace("'", "").replace("{", "").replace("}", "").replace(':', ': [')
        line = line + "]"
        outfile.write('    '+line+'\n')

with open('all-envs-and-hosts.json', 'w+') as jsonfile:
    jsonfile.write('{' + jsonstring + '}')
    
os.remove('./valid.json')
os.remove('./json_output_tmp.json')

