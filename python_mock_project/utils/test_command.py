#!/usr/bin/env python3
"""
Test Runner for Form Submission Automation Tests

This module provides a command-line interface to run form submission tests
with various configurations and options.

Usage examples:
    python utils/test_runner.py run --count 30
    python utils/test_runner.py run --count 10 --delay 2
    python utils/test_runner.py single --verbose
    python utils/test_runner.py stats
    python utils/test_runner.py clean
"""

import argparse
import subprocess
import sys
import os
import time
import json
from datetime import datetime
from typing import List, Dict, Any
import csv

# Add the parent directory to sys.path to import from utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestRunner:
    """Main test runner class for managing form submission tests."""
    
    def __init__(self):
        self.test_file_path = "tests/test_form_submission.py"
        self.log_file_path = "reports/test_submission_log.csv"
        self.reports_dir = "reports"
        
        # Ensure reports directory exists
        os.makedirs(self.reports_dir, exist_ok=True)
    
    def run_single_test(self, verbose: bool = False) -> Dict[str, Any]:
        """
        Run a single test execution.
        
        Args:
            verbose: Whether to display verbose output
            
        Returns:
            Dictionary containing test result information
        """
        start_time = datetime.now()
        
        # Prepare pytest command
        cmd = ["python", "-m", "pytest", self.test_file_path, "-v"]
        if not verbose:
            cmd.extend(["-q", "--tb=short"])
        
        print(f"Starting test at {start_time.strftime('%H:%M:%S')}")
        
        try:
            # Run the test
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=os.getcwd()
            )
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            # Determine test status
            status = "PASSED" if result.returncode == 0 else "FAILED"
            
            test_result = {
                "start_time": start_time,
                "end_time": end_time,
                "duration": duration,
                "status": status,
                "return_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
            
            if verbose:
                print(f"Test completed in {duration:.2f}s - Status: {status}")
                if result.stdout:
                    print("STDOUT:", result.stdout)
                if result.stderr:
                    print("STDERR:", result.stderr)
            else:
                print(f"Test {status} in {duration:.2f}s")
            
            return test_result
            
        except Exception as e:
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            print(f"Error running test: {str(e)}")
            return {
                "start_time": start_time,
                "end_time": end_time,
                "duration": duration,
                "status": "ERROR",
                "error": str(e)
            }
    
    def run_multiple_tests(self, count: int, delay: float = 0, verbose: bool = False) -> List[Dict[str, Any]]:
        """
        Run multiple test executions.
        
        Args:
            count: Number of tests to run
            delay: Delay in seconds between test runs
            verbose: Whether to display verbose output
            
        Returns:
            List of test result dictionaries
        """
        print(f"\nStarting {count} test runs...")
        print(f"Delay between runs: {delay}s")
        print("=" * 50)
        
        results = []
        passed_count = 0
        failed_count = 0
        
        for i in range(1, count + 1):
            print(f"\nTest Run {i}/{count}")
            print("-" * 30)
            
            result = self.run_single_test(verbose)
            results.append(result)
            
            if result["status"] == "PASSED":
                passed_count += 1
            else:
                failed_count += 1
            
            # Add delay between tests (except for the last one)
            if delay > 0 and i < count:
                print(f"Waiting {delay}s before next test...")
                time.sleep(delay)
        
        # Print summary
        print("\n" + "=" * 50)
        print("TEST EXECUTION SUMMARY")
        print("=" * 50)
        print(f"Total Tests: {count}")
        print(f"Passed: {passed_count} ({passed_count/count*100:.1f}%)")
        print(f"Failed: {failed_count} ({failed_count/count*100:.1f}%)")
        
        total_duration = sum(r["duration"] for r in results)
        avg_duration = total_duration / count
        print(f"Total Duration: {total_duration:.2f}s")
        print(f"Average Duration: {avg_duration:.2f}s")
        
        return results
    
    def show_stats(self) -> None:
        """Display statistics from the test log file."""
        if not os.path.exists(self.log_file_path):
            print(f"No log file found at {self.log_file_path}")
            return
        
        try:
            with open(self.log_file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                records = list(reader)
            
            if not records:
                print("No test records found in log file.")
                return
            
            total_tests = len(records)
            successful_tests = sum(1 for r in records if r.get('test_status') == 'success')
            failed_tests = total_tests - successful_tests
            
            durations = []
            for record in records:
                try:
                    duration = float(record.get('duration_seconds', 0))
                    durations.append(duration)
                except (ValueError, TypeError):
                    continue
            
            print("\nTEST STATISTICS")
            print("=" * 40)
            print(f"Total Tests: {total_tests}")
            print(f"Successful: {successful_tests} ({successful_tests/total_tests*100:.1f}%)")
            print(f"Failed: {failed_tests} ({failed_tests/total_tests*100:.1f}%)")
            
            if durations:
                avg_duration = sum(durations) / len(durations)
                min_duration = min(durations)
                max_duration = max(durations)
                
                print(f"\nTIMING STATISTICS")
                print(f"Average Duration: {avg_duration:.2f}s")
                print(f"Fastest Test: {min_duration:.2f}s")
                print(f"Slowest Test: {max_duration:.2f}s")
            
            # Show recent failures
            recent_failures = [r for r in records[-10:] if r.get('test_status') != 'success']
            if recent_failures:
                print(f"\nRECENT FAILURES (Last 10 tests)")
                for failure in recent_failures:
                    missing_fields = failure.get('missing_fields', '')
                    timestamp = failure.get('browser_start_time', 'Unknown')
                    print(f"  • {timestamp}: {missing_fields or 'Unknown error'}")
            
        except Exception as e:
            print(f"Error reading log file: {str(e)}")
    
    def clean_reports(self) -> None:
        """Clean up old reports and screenshots."""
        try:
            if os.path.exists(self.reports_dir):
                files_removed = 0
                for filename in os.listdir(self.reports_dir):
                    file_path = os.path.join(self.reports_dir, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        files_removed += 1
                
                print(f"Cleaned up {files_removed} files from {self.reports_dir}/")
            else:
                print(f"Reports directory {self.reports_dir}/ does not exist.")
                
        except Exception as e:
            print(f"Error cleaning reports: {str(e)}")
    
    def validate_environment(self) -> bool:
        """Validate that the test environment is properly set up."""
        print("🔍 Validating test environment...")
        
        issues = []
        
        # Check if test file exists
        if not os.path.exists(self.test_file_path):
            issues.append(f"Test file not found: {self.test_file_path}")
        
        # Check if pytest is available
        try:
            subprocess.run(["python", "-m", "pytest", "--version"], 
                         capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            issues.append("pytest is not installed or not accessible")
        
        # Check if utils modules can be imported
        try:
            from utils.data_generator import generate_user_profile
            from utils.log_submission_result import FormTestLogger
        except ImportError as e:
            issues.append(f"Cannot import utils modules: {str(e)}")
        
        if issues:
            print("Environment validation failed:")
            for issue in issues:
                print(f"  • {issue}")
            return False
        else:
            print("Environment validation passed!")
            return True


def handle_run_command(args) -> None:
    """Handle the 'run' subcommand."""
    runner = TestRunner()
    
    if not runner.validate_environment():
        sys.exit(1)
    
    if args.count > 1:
        runner.run_multiple_tests(
            count=args.count,
            delay=args.delay,
            verbose=args.verbose
        )
    else:
        runner.run_single_test(verbose=args.verbose)


def handle_single_command(args) -> None:
    """Handle the 'single' subcommand."""
    runner = TestRunner()
    
    if not runner.validate_environment():
        sys.exit(1)
    
    runner.run_single_test(verbose=args.verbose)


def handle_stats_command(args) -> None:
    """Handle the 'stats' subcommand."""
    runner = TestRunner()
    runner.show_stats()


def handle_clean_command(args) -> None:
    """Handle the 'clean' subcommand."""
    runner = TestRunner()
    runner.clean_reports()


def handle_validate_command(args) -> None:
    """Handle the 'validate' subcommand."""
    runner = TestRunner()
    if runner.validate_environment():
        print("All checks passed! Ready to run tests.")
    else:
        sys.exit(1)


def create_argument_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Test Runner for Form Submission Automation Tests",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s run --count 30                 # Run 30 tests
  %(prog)s run --count 10 --delay 2       # Run 10 tests with 2s delay
  %(prog)s single --verbose               # Run one test with verbose output
  %(prog)s stats                          # Show test statistics
  %(prog)s clean                          # Clean up reports directory
  %(prog)s validate                       # Validate environment setup
        """
    )
    
    # Create subparsers
    subparsers = parser.add_subparsers(
        dest='command',
        help='Available commands',
        metavar='COMMAND'
    )
    
    # Run command (multiple tests)
    run_parser = subparsers.add_parser(
        'run',
        help='Run multiple tests with specified count'
    )
    run_parser.add_argument(
        '--count',
        type=int,
        default=1,
        help='Number of tests to run (default: 1)'
    )
    run_parser.add_argument(
        '--delay',
        type=float,
        default=0,
        help='Delay in seconds between test runs (default: 0)'
    )
    run_parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    run_parser.set_defaults(func=handle_run_command)
    
    # Single command
    single_parser = subparsers.add_parser(
        'single',
        help='Run a single test'
    )
    single_parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    single_parser.set_defaults(func=handle_single_command)
    
    # Stats command
    stats_parser = subparsers.add_parser(
        'stats',
        help='Show test statistics from log file'
    )
    stats_parser.set_defaults(func=handle_stats_command)
    
    # Clean command
    clean_parser = subparsers.add_parser(
        'clean',
        help='Clean up reports and screenshots'
    )
    clean_parser.set_defaults(func=handle_clean_command)
    
    # Validate command
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validate test environment setup'
    )
    validate_parser.set_defaults(func=handle_validate_command)
    
    return parser


def main():
    """Main entry point for the test runner."""
    parser = create_argument_parser()
    args = parser.parse_args()
    
    # If no command specified, show help
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Execute the appropriate command
    try:
        args.func(args)
    except KeyboardInterrupt:
        print("\nTest execution interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()