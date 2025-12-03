import json

# Parses the JSON file in given path and sorts website details, services and other information
# Based on what's provided by whatweb

def parse_json(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                website_details = data[0]
                services = []
                other_info = {}
                if "plugins" in website_details:
                    plugins_list = website_details["plugins"]
                    for key in plugins_list:
                        if "version" in plugins_list[key]:
                            services.append(key + " " + plugins_list[key]["version"][0])
                        elif "string" in plugins_list[key]:
                            other_info[key] = plugins_list[key]["string"][0]
                return website_details, services, other_info
    except Exception as e:
        # Handle other general errors
        raise e