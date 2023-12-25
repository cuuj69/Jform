#!/usr/bin/python3

class Modal5:
    def __init__(self, json_data):
        self.json_data = json_data

    def apply_custom_restructuring(self, rules):
        if not isinstance(self.json_data, (dict, list)):
            print('Custom restructuring only works on JSON objects and arrays.')
            return

        # Parse and split the user-defined rules
        instructions = rules.split(';')

        for instruction in instructions:
            # Parse each instruction (e.g., "move key1 before key2")
            action, *targets = instruction.strip().split()

            if action == 'move':
                if len(targets) == 4 and targets[1] == 'before':
                    source_key, _, target_key = targets[0], targets[1], targets[3]
                    self.move_key_before(source_key, target_key)
                    print(f'Moved "{source_key}" before "{target_key}" successfully.')

                elif len(targets) == 4 and targets[1] == 'after':
                    source_key, _, target_key = targets[0], targets[1], targets[3]
                    self.move_key_after(source_key, target_key)
                    print(f'Moved "{source_key}" after "{target_key}" successfully.')

            elif action == 'nest':
                if len(targets) == 4 and targets[1] == 'inside':
                    key_to_nest, _, target_key = targets[0], targets[1], targets[3]
                    self.nest_key_inside(key_to_nest, target_key)
                    print(f'Nested "{key_to_nest}" inside "{target_key}" successfully.')

            elif action == 'flatten':
                if len(targets) == 1:
                    key_to_flatten = targets[0]
                    self.flatten_key(key_to_flatten)
                    print(f'Flattened "{key_to_flatten}" successfully.')

            else:
                print(f'Invalid action: {action}')

        print('Custom restructuring applied successfully.')

    def move_key_before(self, source_key, target_key):
        if not isinstance(self.json_data, dict):
            print('Moving keys is only supported for JSON objects.')
            return

        if source_key not in self.json_data or target_key not in self.json_data:
            print(f'Keys "{source_key}" or "{target_key}" not found in the JSON object.')
            return

        source_value = self.json_data.pop(source_key)
        target_index = list(self.json_data.keys()).index(target_key)

        self.json_data = dict(
            list(self.json_data.items())[:target_index] +
            [(source_key, source_value)] +
            list(self.json_data.items())[target_index:]
        )

    def move_key_after(self, source_key, target_key):
        if not isinstance(self.json_data, dict):
            print('Moving keys is only supported for JSON objects.')
            return

        if source_key not in self.json_data or target_key not in self.json_data:
            print(f'Keys "{source_key}" or "{target_key}" not found in the JSON object.')
            return

        source_value = self.json_data.pop(source_key)
        target_index = list(self.json_data.keys()).index(target_key)

        self.json_data = dict(
            list(self.json_data.items())[:target_index + 1] +
            [(source_key, source_value)] +
            list(self.json_data.items())[target_index + 1:]
        )

    def nest_key_inside(self, key_to_nest, target_key):
        if not isinstance(self.json_data, dict):
            print('Nesting keys is only supported for JSON objects.')
            return

        if key_to_nest not in self.json_data or target_key not in self.json_data:
            print(f'Keys "{key_to_nest}" or "{target_key}" not found in the JSON object.')
            return

        source_value = self.json_data.pop(key_to_nest)
        self.json_data[target_key] = {key_to_nest: source_value}

    def flatten_key(self, key_to_flatten):
        if not isinstance(self.json_data, dict):
            print('Flattening keys is only supported for JSON objects.')
            return

        if key_to_flatten not in self.json_data or not isinstance(self.json_data[key_to_flatten], dict):
            print(f'Key "{key_to_flatten}" not found or not a nested object in the JSON object.')
            return

        nested_data = self.json_data.pop(key_to_flatten)
        self.json_data.update(nested_data)
