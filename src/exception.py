import sys
import logging

logger = logging.getLogger(__name__)

def error_message_detail(error, error_detail:sys):
    _, _, exec_tb = error_detail.exc_info()
    filename = exec_tb.tb_frame.f_code.co_filename
    line_num = exec_tb.tb_lineno
    error_msg = f"Error occured in python file name {filename} line number {line_num} error message {str(error)}"
    return error_msg

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_msg = error_message_detail(error_message, error_detail)
    
    def __str__(self) -> str:
        return self.error_msg
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logger.error("division by zero")
        raise CustomException(e, sys)
