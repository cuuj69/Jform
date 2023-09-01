import json

class Modify:
    intro = "Welcome to jform v1"
    #info

    def __init__(self):
        #options
        self.__modals = {
            '1': 'stringified',
            '2': 'sorted',
            '3': 'reverse sorted',
            '4': 'view structure',
            '5': 'custom restructuring'
        }
        self.json_data = None  # Initialize JSON data here

    def main(self):
        print(self.intro)
        print('Available modals:')
        for key, value in self.__modals.items():
            print(f'{key}: {value}')#display the available modals

        user_choice = input('Enter your choice (1/2/3/4/5): ')
        if user_choice in self.__modals:
            modal_function = getattr(self, f'modal_{user_choice}')
            if user_choice in ['4', '5']:
                modal_function()
            else:
                if self.json_data:
                    result = modal_function()
                    print(f'Result of {self.__modals[user_choice]} operation:')
                    print(result)
                else:
                    print('Please load JSON data first.')
        else:
            print('Invalid choice. Please select a valid option.')

    def load_json(self):
        try:
            json_file = input('Enter the path to your JSON file: ')
            with open(json_file, 'r') as file:
                self.json_data = json.load(file)
                print('JSON data loaded successfully.')
        except Exception as e:
            print(f'Error loading JSON data: {e}')

    def modal_1(self):
        if self.json_data:
            return json.dumps(self.json_data, indent=4)  # Perform stringification
        else:
            print('Please load JSON data first.')

    def modal_2(self):
        if self.json_data:
            return json.dumps(self.json_data, indent=4, sort_keys=True)  # Perform sorting
        else:
            print('Please load JSON data first.')

    def modal_3(self):
        if self.json_data:
            return json.dumps(self.json_data, indent=4, sort_keys=True, reverse=True)  # Perform reverse sorting
        else:
            print('Please load JSON data first.')

    def modal_4(self):
        if self.json_data:
            print('JSON structure:')
            self.view_json_structure(self.json_data)
        else:
            print('Please load JSON data first.')

    def modal_5(self):
        if self.json_data:
            print('Custom restructuring: (e.g., key1 before key2)')
            restructuring_rule = input('Enter restructuring rule: ')
            # Parse and apply the restructuring rule to the JSON data
            # Implement this part based on your specific requirements
            print('Custom restructuring applied successfully.')
        else:
            print('Please load JSON data first.')

    def view_json_structure(self, json_obj, level=0):
        if isinstance(json_obj, dict):
            for key, value in json_obj.items():
                print('  ' * level + str(key))
                self.view_json_structure(value, level + 1)
        elif isinstance(json_obj, list):
            for item in json_obj:
                self.view_json_structure(item, level + 1)

if __name__ == '__main__':
    modifier = Modify()
    modifier.load_json()  # Load JSON data before applying operations
    modifier.main()
