import sys
class NetworkSecurityException(Exception):
    def __init__(self,error_messsage,error_details:sys):
        self.error_message=error_messsage
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured inn python script name [{0}] line number [{1}] error message [{2}]".format(self.file_name,self.lineno,str(self.error_message))
