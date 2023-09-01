import json

class Serialize:
    def __init__(self, json_data):
        self.json_data = json_data

    def get_json_data_as_string(self):
        return json.dumps(self.json_data, indent=4, ensure_ascii=False, sort_keys=True)

    def serialize_keys(self, keys_to_serialize):
        def serialize_key(obj, keys):
            if isinstance(obj, dict):
                for key, val in obj.items():
                    if key in keys:
                        obj[key] = f'"{val}"'  # Keep the double quotes
                    elif isinstance(val, (dict, list)):
                        serialize_key(val, keys)
            elif isinstance(obj, list):
                for item in obj:
                    serialize_key(item, keys)

        data_copy = self.json_data.copy()
        serialize_key(data_copy, keys_to_serialize)
        return json.dumps(data_copy, indent=4, ensure_ascii=False, sort_keys=True)


    def serialize_values(self, keys_to_serialize):
        def replace_value(obj):
            if isinstance(obj, dict):
                for key, val in obj.items():
                    if isinstance(val, (dict, list)):
                        replace_value(val)
                    elif isinstance(val, str) and key in keys_to_serialize:
                        obj[key] = f'"{val}"'
            elif isinstance(obj, list):
                for item in obj:
                    if isinstance(item, dict):
                        replace_value(item)

        data_copy = self.json_data.copy()
        replace_value(data_copy)
        return json.dumps(data_copy, indent=4, ensure_ascii=False, sort_keys=True)
