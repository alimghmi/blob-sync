# blob-sync

blob sync is a Python application designed to fetch file metadata from Azure Blob Storage and store it in an MSSQL database. This project is particularly useful for creating an index of specific file types (e.g., PDFs) stored in Azure Blob Storage.

## Features
- Fetch file metadata from Azure Blob Storage.
- Filter files based on extension (default is set to .pdf).
- Store file metadata in an MSSQL database.
- Customizable for various file types and database schemas.

## Usage
- Install the required packaghes:
    ```
    pip install -r requirements.txt
    ```

- Create a .env file according to .env.sample

- To run the application, execute the following command:

    ```
    python main.py
    ```

## Contributing

Contributions to blob sync are welcome. Please ensure you follow the guidelines:

- Fork the repository.
- Create a new branch for each feature or improvement.
- Send a pull request from each feature branch to the main branch.
  
## License
Include details about the license or state that the project is licensed under the MIT License.