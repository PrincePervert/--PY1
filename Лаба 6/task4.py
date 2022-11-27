import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename, 'r') as f:
        list_ = []
        for index, line in enumerate(f, 1):
            fields = line.strip(new_line).split(delimiter)
            if index == 1:
                headers = fields
                continue
            list_.append({})
            for i, _ in enumerate(headers):
                list_[-1][headers[i]] = fields[i]
        return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
