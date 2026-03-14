Student Report Parser Using Python

Overview
This project is a Python program that reads student information from a single input string and generates a complete academic report. The program extracts student names and subject marks, organizes them into structured data, calculates averages, assigns grades, and determines the class topper.

The project focuses on practicing core Python skills such as string parsing, list manipulation, loops, and conditional logic.

Technologies Used
Python

Input Format
The program expects student data in the following format.

Number of students
Student information string

Example input

3
Uday 86:78:98, Aman 67:20:94, Naman 75:82:91

Each student entry contains a name followed by three subject marks separated by colons.

Program Features
Extracts student names and marks from a single formatted string
Stores marks for each subject separately
Groups subject marks for each student
Calculates average marks for every student
Assigns grades based on performance
Computes overall class average
Identifies the class topper
Counts the number of passed and failed students

Grading System

Average greater than or equal to 90 results in Grade A
Average greater than 75 and less than 89 results in Grade B
Average greater than 60 and less than 74 results in Grade C
Average less than 60 results in Grade D

Program Workflow

The program first reads the number of students
Student information is split into individual records
Each record is divided into student name and marks
Marks are separated into Maths, Science, and English
Marks are grouped for each student
Average marks are calculated for every student
Grades are assigned based on the calculated averages
Class statistics such as class average and topper are computed

Learning Outcome

This project strengthens understanding of

String manipulation in Python
List processing and indexing
Loop based data processing
Function based program structure
Basic statistical calculations

These concepts are foundational for data processing tasks that appear frequently in data analysis and data science.

Author

Uday Bhaskar
Aspiring Data Science learner working with Python and data analysis concepts.
