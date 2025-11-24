# Functional Requirements

# 1. Input Module
	1.	The system will ask the user to enter the number of days they want to record study activity.
	2.	The system will let the user enter multiple subjects for each day.
	3.	The system will let the user enter the number of minutes spent on each subject.
	4.	The system will check that:
	•	subject names are not empty
	•	study time is a positive integer
	5.	The system will let the user stop adding subjects for a day by typing the exit keyword (done).
	6.	The system will repeat this input collection process for all days the user requests.

⸻

# 2. Processing Module
	1.	The system will store each day’s study records in a structured format.
	2.	The system will calculate the total minutes studied for each day.
	3.	The system will identify:
	•	the subject with the most study time for the day
	•	the subject with the least study time for the day
	4.	The system will correctly manage days where only one subject was studied.
	5.	The system will prepare a structured data summary for the output module.

⸻

# 3. Output Module
	1.	The system will display all subjects studied each day along with the minutes spent.
	2.	The system will show the total study time for each day.
	3.	The system will clearly indicate the most studied and least studied subjects.
	4.	The system will present results in a clean, readable format with headings.
	5.	The system will handle special cases such as:
	•	days with only one subject
	•	invalid inputs

⸻

# 4. Main System Module
	1.	The system will control the overall program flow.
	2.	The system will ask the user how many days they want to track.
	3.	The system will repeatedly call:
	•	the Input Module to collect the day’s study data
	•	the Processing Module to analyze the collected data
	•	the Output Module to display the results
	4.	The system will manage each day separately within a loop.
	5.	The system will ensure that all modules run only when main.py is executed directly (using the if __name__ == "__main__" guard).
	6.	The system will integrate all components to ensure the complete Input → Processing → Output cycle.

⸻

# Non-Functional Requirements

# 1.	Usability
	•	The system should be simple for any user to operate without technical knowledge.
	
	•	All prompts should be easy to understand.
	
# 2.	Reliability
	•	The program should run without crashing during normal use.
	
	•	Input validation should prevent incorrect data from breaking the program.
	
# 3.	Performance
	•	The system should respond immediately to user input.
	
	•	Processing daily study data should take less than a second, even with multiple subjects.
	
# 4.	Maintainability
	•	The code should be organized into separate modules (Input, Processing, Output, Main) so it’s easy to update or expand later.
	
	•	Variable names and functions should be readable and meaningful.
	
# 5.	Portability
	•	The program should run on any system that supports Python 3 (Windows, macOS, or Linux).
	
	•	No special libraries should be required.
	
# 6.	Data Integrity
	•	The program should store and calculate study times accurately.
	
	•	No data from one day should interfere with another day’s records.
	
