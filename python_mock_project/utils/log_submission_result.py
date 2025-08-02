import csv
import os
from datetime import datetime
from typing import Optional, List, Dict, Any
import json

class FormTestLogger:
    def __init__(self, log_file_path: str = "reports/test_submission_log.csv"):
        """
        Initialize TestLogger
        
        Args:
            log_file_path: Path to CSV log file
        """
        self.log_file_path = log_file_path
        self.start_time = None
        self.end_time = None
        self.test_status = "pending"
        self.missing_fields = []
        self.user_data = {}
        
        # Ensure reports directory exists
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
        
        # Create CSV file with headers if it doesn't exist
        if not os.path.exists(log_file_path):
            self._create_csv_file()
    
    def _create_csv_file(self):
        """Create CSV file with headers"""
        headers = [
            "browser_start_time", 
            "browser_end_time",
            "duration_seconds",
            "test_status",
            "missing_fields"
        ]
        
        with open(self.log_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
    
    def start_test(self, user_data: Dict[str, Any]):
        """
        Mark test start time and store user data
        
        Args:
            user_data: Dictionary containing user data for the test
        """
        self.start_time = datetime.now()
        self.user_data = user_data
        self.test_status = "running"
        print(f"Test started at: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def end_test(self, status: str = "success", missing_fields: List[str] = None, error_message: str = ""):
        """
        Mark test end time and set final status
        
        Args:
            status: Test status ("success" or "fail")
            missing_fields: List of missing/failed fields
            error_message: Error message if test failed
        """
        self.end_time = datetime.now()
        self.test_status = status
        self.missing_fields = missing_fields or []
        
        duration = (self.end_time - self.start_time).total_seconds()
        print(f"Test ended at: {self.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Test duration: {duration:.2f} seconds")
        print(f"Test status: {status}")
        
        if missing_fields:
            print(f"Missing fields: {', '.join(missing_fields)}")
        
        # Write to CSV
        self._write_to_csv(error_message)
    
    def _write_to_csv(self, error_message: str = ""):
        """Write test results to CSV file"""
        if not self.start_time or not self.end_time:
            print("Warning: Test times not properly set")
            return
        
        duration = (self.end_time - self.start_time).total_seconds()
        
        row_data = [
            self.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            self.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            f"{duration:.2f}",
            self.test_status,
            ', '.join(self.missing_fields) if self.missing_fields else ""
        ]
        
        # Write to CSV
        with open(self.log_file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(row_data)
        
        print(f"Test results logged to: {self.log_file_path}")
    
    def validate_form_data(self, user_data: Dict[str, Any]) -> tuple[bool, List[str]]:
        """
        Validate if all required form fields have data
        
        Args:
            user_data: Dictionary containing user data
            
        Returns:
            Tuple of (is_valid, missing_fields_list)
        """
        required_fields = {
            'first_name': 'First Name',
            'last_name': 'Last Name', 
            'email': 'Email',
            'gender': 'Gender',
            'mobile': 'Mobile Number',
            'date_of_birth': 'Date of Birth',
            'subjects': 'Subjects',
            'hobbies': 'Hobbies',
            'address': 'Current Address',
            'state': 'State',
            'city': 'City'
        }
        
        missing_fields = []
        
        for field_key, field_name in required_fields.items():
            value = user_data.get(field_key)
            
            # Check if field is missing or empty
            if not value:
                missing_fields.append(field_name)
            # Special check for lists (subjects, hobbies)
            elif isinstance(value, list) and len(value) == 0:
                missing_fields.append(field_name)
        
        is_valid = len(missing_fields) == 0
        return is_valid, missing_fields


def log_test_result(start_time: datetime, end_time: datetime, 
                   status: str, missing_fields: List[str] = None,
                   log_file_path: str = "reports/test_submission_log.csv"):
    """
    Standalone function to log test results (alternative to class usage)
    
    Args:
        start_time: Test start datetime
        end_time: Test end datetime  
        status: Test status ("success" or "fail")
        missing_fields: List of missing/failed fields
        log_file_path: Path to CSV log file
    """
    logger = FormTestLogger(log_file_path)
    logger.start_time = start_time
    logger.end_time = end_time
    logger.test_status = status
    logger.missing_fields = missing_fields or []
    logger._write_to_csv()

# if __name__ == "__main__":
    