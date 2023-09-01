import json
from serialize import Serialize
from custom import Modal5

class Modify:
    intro = "Welcome to jform v1"

    def __init__(self):
        self.__modals = {
            '1': 'serialize',
            '2': 'sorted',
            '3': 'reverse sorted',
            '4': 'view structure',
            '5': 'custom restructuring'
        }
        self.json_data = None
        self.serializer = None
        self.modal_function = None # modal_function defined

    def main(self):
        print(self.intro)
        print('Available modals:')
        for key, value in self.__modals.items():
            print(f'{key}: {value}')

        user_choice = input('Enter your choice (1/2/3/4/5): ')
        if user_choice in self.__modals:
            if user_choice == '1':
                self.load_json()
                self.serializer = Serialize(self.json_data)
                self.display_json_data()
                keys_to_serialize = self.get_keys_to_serialize()
                self.perform_serialization(keys_to_serialize)
            else:
                modal_function = getattr(self, f'modal_{user_choice}')
            
                if self.json_data:
                    result = modal_function()
                    if result is not None:
                        self.write_json_to_file(result)
                else:
                    print('Please load JSON data first.')
        else:
            print('Invalid choice. Please select a valid option.')

    def load_json(self):
        try:
            json_file = input('Enter the path to your JSON file: ')
            with open(json_file, 'r') as file:
                self.json_data = json.load(file)
                self.serializer = Serialize(self.json_data)
                print('JSON data loaded successfully')
        except Exception as e:
            print(f'Error loading JSON data: {e}')
            
    def display_json_data(self):
        if self.json_data:
            print('JSON Data:')
            print(self.serializer.get_json_data_as_string())
        else:
            print('Please load JSON data first.')

    def get_keys_to_serialize(self):
        keys_input = input('Enter keys to serialize (e.g., key1 key2 key3): ')
        keys_to_serialize = keys_input.split()
        return keys_to_serialize

    def perform_serialization(self, keys_to_serialize):
        if self.json_data:
            print('Choose serialization type:')
            print('1: Full Serialize (Key and Values)')
            print('2: Value Serialize (Values Only)')
            serialization_type = input('Enter your choice (1/2): ')
            if serialization_type == '1':
                result = self.serializer.serialize_keys(keys_to_serialize)
            elif serialization_type == '2':
                result = self.serializer.serialize_values(keys_to_serialize)
            else:
                print('Invalid serialization type.')
                return

            print('Serialized JSON:')
            print(result)

            # Save the updated JSON to a file
            self.write_json_to_file(result)
        else:
            print('Please load JSON data first.')

    def modal_2(self):
        if self.json_data:
            sorted_json = json.dumps(self.json_data, indent=4, sort_keys=True, separators=(',',':'))
            return sorted_json
        else:
            print('Please load JSON data first')
    
    def modal_3(self):
        if self.json_data:
            sorted_json = json.dumps(self.json_data, indent=4, sort_keys=True, separators=(',', ':'))
            reversed_json = json.loads(sorted_json)
            reversed_json = {k: reversed_json[k] for k in reversed(reversed_json)}
            return json.dumps(reversed_json, indent=4, separators=(',', ':'))
        else:
            print('Please load JSON data first')
            
    def modal_4(self):
        if self.json_data:
            self.display_json_data()
        else:
            print('Please load JSON data first.')

    def modal_5(self):
        if self.json_data:
            print('Custom restructuring: (e.g., key1 before key2)')
            restructuring_rule = input('Enter restructuring rule: ')
            modal5 = Modal5(self.json_data)
            modal5.apply_custom_restructuring(restructuring_rule)
            print('Custom restructuring applied successfully.')
        else:
            print('Please load JSON data first.')
        
    def write_json_to_file(self, json_str):
        output_file = input('Enter the path to save the updated JSON file: ')
        try:
            with open(output_file, 'w') as file:
                file.write(json_str)
            print(f'Updated JSON data saved to {output_file} successfully.')
        except Exception as e:
            print(f'Error saving JSON data: {e}')

if __name__ == '__main__':
    modifier = Modify()
    modifier.load_json()
    modifier.main()
