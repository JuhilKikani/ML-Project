import sys
from src.logger import logging  # Import your custom logging setup

# Function to generate detailed error messages including filename, line number, and error message
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() # Get the traceback object from the error
    file_name = exc_tb.tb_frame.f_code.co_filename # Extract the file name where the exception occurred
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)) # Format a detailed error message
    
    return error_message

# Define a custom exception class that gives more helpful debugging information
class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
            super().__init__(str(error)) # Call the base class constructor to initialize the exception
            self.error_message = error_message_detail(error, error_detail) # Generate a detailed error message using the helper function
    
    # Define what should be returned when str() is called on this object (i.e., when printed)
    def __str__(self):
        return self.error_message
