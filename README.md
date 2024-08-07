# University Admissions Procedure

This project is a Python-based application for managing university admissions. It processes student applications, sorts them based on test scores and priorities, and selects the best candidates for each department.

## Features

- **Receive Applicants**: Reads applicant data from a file and creates a list of `Student` objects.
- **Sort Applicants**: Sorts applicants based on their test scores and names.
- **Select Best Candidates**: Selects the best candidates for each department based on their test scores and priorities.
- **Print Admitted Students**: Prints the list of admitted students for each department.
- **Send Admitted Students List to Files**: Saves the list of admitted students for each department to separate files.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd <project-directory>
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python university_admissions.py
    ```
2. Follow the prompts to input the number of students to be accepted per department and provide the `applicants.txt` file with the applicant data.

## File Structure

- `university_admissions.py`: Main script for managing university admissions.
- `student.py`: Contains the `Student` class definition.
- `util/set_logging.py`: Contains the logging configuration.
- `applicants.txt`: Input file containing applicant data.

## Logging

The application uses the `logging` module to log debug and info messages. The log messages provide detailed information about the application's execution flow and can be used for debugging purposes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
