### 1. **Q1**:  
   a) **Define software quality. List & explain core components of quality.** [5 Marks]

**Software Quality**: Software quality refers to the degree to which software meets specified requirements, user needs, and expectations. It ensures the software is free of defects and works reliably under various conditions.

**Core Components of Quality**:
1. **Functionality**: How well the software performs the tasks it is designed to do. It ensures that the system behaves correctly and performs all specified functions.
2. **Reliability**: The ability of software to perform its required functions under stated conditions for a specified time without failure.
3. **Usability**: Ease of use and learnability of the software. A well-designed user interface, helpful documentation, and intuitive navigation contribute to this.
4. **Efficiency**: The software's ability to make optimal use of system resources like memory, CPU, and network bandwidth.
5. **Maintainability**: How easily the software can be modified, including fixing bugs, updating features, and adapting to new requirements.
6. **Portability**: The ease with which the software can be transferred from one environment to another, such as from Windows to Linux.

---

   b) **What are the constraints of software product quality assessment?** [5 Marks]

Constraints in assessing software product quality:
1. **Subjectivity**: Different stakeholders may have different views on what constitutes quality.
2. **Incompleteness of Requirements**: Undefined or unclear requirements can make it challenging to assess quality.
3. **Complexity**: Complex software systems with interdependent modules make assessing overall quality difficult.
4. **Testing Limitations**: Not all defects are detectable, and exhaustive testing is often not possible due to resource constraints.
5. **Time and Budget**: Limited time and budget can constrain the thoroughness of quality assessment, resulting in prioritization of certain areas over others.

---

   c) **Explain the defect life cycle with a diagram.** [5 Marks]

**Defect Life Cycle** (also known as **Bug Life Cycle**): The defect life cycle refers to the progression of a defect through various stages, from discovery to resolution. 

1. **New**: The defect is identified and reported.
2. **Assigned**: The defect is assigned to the development team for analysis and resolution.
3. **Open**: The developer begins working on fixing the defect.
4. **Fixed**: The developer resolves the defect.
5. **Retest**: The tester verifies that the defect has been fixed.
6. **Closed**: The tester confirms the defect is resolved and closes it.
7. **Reopened**: If the issue persists after fixing, it is reopened.

**Diagram**:  
New → Assigned → Open → Fixed → Retest → Closed (or Reopened if necessary)

---

### OR

### 2. **Q2**:  
   a) **Examine the relationship between quality & productivity.** [5 Marks]

There is a direct relationship between **quality** and **productivity**:
- **Quality improvements** reduce the number of defects, leading to less rework and shorter development cycles, thus improving productivity.
- High-quality products tend to require fewer updates and patches post-deployment, allowing developers to focus on new features rather than bug fixing.
- Conversely, poor quality increases the time spent on debugging, reduces productivity, and leads to higher maintenance costs.
- In software, achieving high quality often leads to higher customer satisfaction, fewer complaints, and more effective use of resources, all of which enhance overall productivity.

---

   b) **Explain the PDCA cycle.** [5 Marks]

The **PDCA Cycle** (Plan-Do-Check-Act), also known as the **Deming Cycle**, is a method for continuous improvement in quality management.

1. **Plan**: Identify the problem, set goals, and plan actions for improvement.
2. **Do**: Implement the planned solution or test it in a small-scale experiment.
3. **Check**: Monitor and measure the effectiveness of the solution. Compare results with the objectives set in the planning phase.
4. **Act**: If the solution is successful, implement it on a larger scale. If not, adjust the plan and repeat the cycle.

---

   c) **Plan software quality control with respect to college attendance software.** [5 Marks]

For a **College Attendance Software**, the quality control plan should focus on ensuring accuracy, reliability, and security:

1. **Functionality Testing**: Ensure the software records attendance accurately and generates reports as required.
2. **Usability Testing**: Test the ease of use for administrators and teachers entering attendance data.
3. **Reliability Testing**: Ensure the system handles multiple users and large amounts of data without errors or crashes.
4. **Security Testing**: Ensure student data privacy is maintained and unauthorized access is prevented.
5. **Performance Testing**: Ensure the software processes attendance data quickly and generates reports in a timely manner.
6. **Maintainability**: Plan for regular updates and bug fixes to keep the software up-to-date.

---

### 3. **Q3**:  
   a) **Write test cases for login validation.** [5 Marks]

**Test Case 1: Valid Login**
- **Description**: Verify if the user can log in with valid credentials.
- **Steps**:
  1. Enter a valid username.
  2. Enter a valid password.
  3. Click on the 'Login' button.
- **Expected Result**: User is successfully logged in.

**Test Case 2: Invalid Password**
- **Description**: Verify if the user is denied access with a valid username but an invalid password.
- **Steps**:
  1. Enter a valid username.
  2. Enter an incorrect password.
  3. Click on the 'Login' button.
- **Expected Result**: User is shown an error message.

**Test Case 3: Blank Fields**
- **Description**: Verify if the user is denied access when leaving username or password blank.
- **Steps**:
  1. Leave the username or password field blank.
  2. Click on the 'Login' button.
- **Expected Result**: User is prompted to fill in the required fields.

---

   b) **What are the entry & exit criteria of testing?** [5 Marks]

**Entry Criteria**: These are the preconditions that must be met before testing can begin:
1. Requirements and design documents are completed and reviewed.
2. Test environment is set up and ready.
3. Test data is prepared.
4. All necessary test cases are written.

**Exit Criteria**: These are the conditions that must be met to conclude testing:
1. All test cases have been executed.
2. No high-severity bugs remain open.
3. Test coverage is satisfactory.
4. Final test report is completed and reviewed.

---

   c) **Analyse test policy & test strategy in test documentation.** [5 Marks]

**Test Policy**: A high-level document that defines the company's approach to software testing. It outlines the goals of testing, the general testing approach, and key responsibilities of the testing team. A test policy is typically long-term and remains stable across projects.

**Test Strategy**: A more detailed document outlining how testing will be performed for a specific project. It includes testing levels (unit, integration, system), testing types (manual, automated), and resource allocation. The test strategy may vary depending on the project’s specific needs.
