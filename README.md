# Print-directory-Tree

## Description

This script prints a directory tree structure, ignoring items specified in an `ignore.json` file. It is useful for visualizing the structure of a directory while excluding unnecessary files and directories.

## Features

- Recursively prints the directory tree structure.
- Ignores files and directories specified in an `ignore.json` file.
- Provides a clear visual hierarchy with indentation and tree symbols.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the script files.
2. Ensure you have Python installed on your system.

## Usage

1. Place the `main.py` script and `ignore.json` file in the same directory.
2. Open a terminal and navigate to the directory containing `main.py`.
3. Run the script using the following command:

    ```sh
    python main.py
    ```

## Configuration

- [ignore.json](ignore.json): A JSON file containing a list of file and directory names to ignore. Example:

    ```json
    {
        "ignore_names": [
            "node_modules",
            ".git",
            "__pycache__"
        ]
    }
    ```

## Example

If your directory structure is as follows:

```
/home/mm/Desktop/Print-directory-Tree
├── .gitignore
├── ignore.json
├── main.py
└── README.md
```

Running the script with the provided `ignore.json` will output:

```
/home/mm/Desktop/Print-directory-Tree
├── main.py
└── README.md
```

## Troubleshooting

- Ensure that the `ignore.json` file is correctly formatted as JSON.
- Verify that the directory path provided to the script is valid.
- Check for any error messages printed by the script for additional guidance.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by various directory tree visualization tools.
- Thanks to the open-source community for their contributions.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.