import json
import csv
generate_data = []
with open('rawdata.csv', 'r') as f:
    raw_data = csv.reader(f)
    for list in raw_data:
        generate_data.append(list)
end = generate_data[len(generate_data)-1]
with open('expdata.json',"r") as f1:
    add_data = json.load(f1)
    for i in range(len(add_data)-1):
        print(add_data[i]['date'])
        if add_data[i]['date'] == '2021/08/31':####bug可能需要手动
            break;

    for j in range(i+1,len(add_data)-1):
        generate_data.append([add_data[j]['date'],str(float(end[1])+(float(add_data[j]['cnt'])-float(add_data[j-1]['cnt']))/60.0)])
        end = generate_data[len(generate_data) - 1]
    f = open('generate.csv', 'w',newline='')

    with f:
        w = csv.writer(f)
        for row in generate_data:
            w.writerow(row)
