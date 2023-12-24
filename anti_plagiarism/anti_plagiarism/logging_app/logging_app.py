import logging as lg
from datetime import datetime


class MyFormatter(lg.Formatter):
    def format(self, record):
        log_msg = f"{datetime.now()} {record.funcName}_function {record.levelname.upper()} {record.msg}"
        return log_msg


class DebugAndInfoFilter(lg.Filter):
    def filter(self, record):
        return record.levelno <= lg.INFO


class CriticalAndErrorFilter(lg.Filter):
    def filter(self, record):
        return record.levelno >= lg.WARNING


def get_logger(name, error_file_path, info_file_path):
    tmp_logger = lg.getLogger(name)
    tmp_logger.setLevel(lg.DEBUG)
    debug_and_info_handler = lg.FileHandler(info_file_path)
    debug_and_info_handler.addFilter(DebugAndInfoFilter())
    debug_and_info_handler.setLevel(lg.DEBUG)
    debug_and_info_handler.setFormatter(MyFormatter())
    critical_and_error_handler = lg.FileHandler(error_file_path)
    critical_and_error_handler.addFilter(CriticalAndErrorFilter())
    critical_and_error_handler.setLevel(lg.ERROR)
    critical_and_error_handler.setFormatter(MyFormatter())
    tmp_logger.addHandler(debug_and_info_handler)
    tmp_logger.addHandler(critical_and_error_handler)
    return tmp_logger


model_logger = get_logger("model_logger", "logging_app/model_errors.log", "logging_app/model_info.log")
tree_visitors_logger = get_logger("tree_visitors_logger", "logging_app/tree_visitors_errors.log",
                                  "logging_app/tree_visitors_info.log")
anti_plagiarism_logger = get_logger("anti_plagiarism_logger", "logging_app/anti_plagiarism_errors.log",
                                    "logging_app/anti_plagiarism_info.log")
anti_plagiarism_streamlit_logger = get_logger("anti_plagiarism_streamlit_logger",
                                              "logging_app/anti_plagiarism_streamlit_errors.log",
                                              "logging_app/anti_plagiarism_streamlit_info.log")
