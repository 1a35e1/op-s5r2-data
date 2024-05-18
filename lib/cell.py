import re

def extract_criteria_data(text):
    """
    Extracts the criteria data from the text and returns a list of dictionaries
    
    :param text: The text to extract the criteria data from
    :return: A list of dictionaries containing the criteria data
    """
    
    # Initialize an empty list to store the extracted dictionaries
    criteria_list = []

    # Use regular expression to find all lines starting with "Criteria:"
    criteria_lines = re.findall(r'Criteria: (.*?) - Average: ([\d\.]+) \|\| Total: (\d+)', text)

    # Iterate through the found lines and create dictionaries
    for line in criteria_lines:
        criteria_dict = {
            "name": line[0].strip(),
            "average": float(line[1]),
            "total": int(line[2])
        }
        criteria_list.append(criteria_dict)

    return criteria_list

