# Terraform State Reader

This Python script is designed for a hackathon project at env0 to read and analyze Terraform state files. It provides functionalities to list all resources within the state file, check the existence of a specific resource, and list all managed resources.

## Features

- **List Resources**: Lists all resources defined within the Terraform state file.
- **Check Resource Existence**: Checks if a specific resource exists within the Terraform state file.
- **List Managed Resources**: Lists all resources that are managed by Terraform.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your machine.
- The `pydantic` library installed. You can install it using pip3:

```bash
pip3 install -r requirements
```

- A valid Terraform state file named `state_file.tfstate.json` located in the same directory as the script.

## Setup

Clone this repository to your local machine using:
```bash
git clone <repository-url>
```

Navigate into the project directory:
```bash
cd <project-directory>
```

Ensure you have the Terraform state file (`state_file.tfstate.json`) in the root of the project directory.

## Usage

To run the script, execute the following command in your terminal:

```bash
python3 main.py
```

## Output

The script will print:

- A list of all resources in the Terraform state file.
- A boolean indicating whether the 'GITHUB_APP_CLIENT_SECRET' resource exists.
- A list of all managed resources within the state file.