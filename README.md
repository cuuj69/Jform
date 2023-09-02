# JForm

**JForm** is a Python tool for working with JSON data, providing various functionalities such as serialization, sorting, custom restructuring, and more. This tool aims to simplify common tasks related to JSON manipulation.

## Features

- **Serialization:** Serialize JSON data by either keys, values, or both.
- **Sorting:** Sort JSON data alphabetically.
- **Custom Restructuring:** Apply custom restructuring rules to JSON data.
- **View Structure:** View the current structure of JSON data.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cuuj69/jform.git
   cd jform

2. Create a virtual environment(optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate #On Windows, use 'venv\Scripts\activate'

3. Install the required dependencies:
   ```bash
   pip install -requirements.txt

### Usage

1. Run the `main.py` script to start JForm:
   ```bash
   python main.py

2. Follow the on-screen instructions to load your JSON data and select from available modals.
  
3. Use the provided options to perform JSON operations.

### Modals

JForm provides the following modals:

* Serialize: Serialize JSON data by keys, values, or both.

* Sorted: Sort JSON data alphabetically.

* Reverse Sorted: Sort JSON data in reverse alphabetical order.

* View Structure: View the current structure of JSON data.

* Custom Restructuring: Apply custom restructuring rules to JSON data.

### Custom Restructuring Commands

The custom restructuring modal allows you to apply custom restructuring rules to your JSON data. Here's the command format:

* `move key1 before key2: Move key1 before key2`.
* `move key1 after key2: Move key1 after key2`.
* `nest key1 inside key2: Nest key1 inside key2`.
* `flatten key1: Flatten (un-nest) key1`.

For example, to move "address" before "name" and then flatten "address":

- For example, to move "address" before "name" and then flatten "address":
    ```bash
    move address before name; flatten address
    
### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

### Acknowledgments

- OpenAI GPT-3

### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

### Authors

William Jefferson Mensah
