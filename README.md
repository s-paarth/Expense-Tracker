# Expense-Tracker
## Team no. 15
## Objective
The primary goal of the ExpenseTracker project is to:

 - Track and manage personal expenses effectively.
 - Categorize expenses for better financial awareness.
 - Provide visual insights into spending habits through aesthetically pleasing pie charts.
## How It Was Achieved
### Modular Design:

Split responsibilities into two classes:
 - ExpenseManager for handling the data.
 - ExpenseTrackerApp for creating the GUI and user interactions.
### Core Features Implemented:

 - Add expenses with attributes like date, category, amount, and description.
 - Display all recorded expenses in a table for easy review.
 - Visualize expense distribution by category using a pie chart.
### Optimized User Interface:

 - Created input fields dynamically with labels to avoid repetitive code.
 - Used ttk.Treeview for a responsive, clean table view of expenses.
### Aesthetic Enhancements for Pie Chart:

 - Used matplotlib to generate visually appealing pie charts.
 - Displayed percentage breakdown for each category on the chart.
 - Ensured the pie chart is circular and uses distinct colors for clarity.
## Outcome
### Functional Expense Tracker Application:

 - Users can add, review, and visualize expenses effortlessly.
 - The pie chart provides a quick overview of spending patterns.
### Code Efficiency:

### Kept the code concise and under 120 lines by:
 - Removing unnecessary features.
 - Consolidating repetitive logic.
 - Avoiding overly verbose comments.
### User-Friendly Interface:

 - Intuitive input fields and responsive components.
 - Easy-to-read pie chart for financial insights.
   
```mermaid
graph TD
    %% Style Definitions
    classDef startEnd fill:#f9c6c9,stroke:#d72323,stroke-width:3,color:#000;
    classDef process fill:#ffe0b5,stroke:#f3a953,stroke-width:2,color:#000;
    classDef decision fill:#d4f1f4,stroke:#0077b6,stroke-width:2,color:#000,stroke-dasharray: 5 5;
    classDef action fill:#caf0f8,stroke:#0096c7,stroke-width:2,color:#000;
    classDef highlight fill:#ade8f4,stroke:#023e8a,stroke-width:3,color:#000,stroke-dasharray: 5 5;

    %% Nodes
    A((🏁 Start)):::startEnd --> B{📂 Select Action}:::decision
    B --> C[✍️ Add Expense]:::process
    B --> D[📊 View by Category]:::process
    B --> E[📈 Generate Pie Chart]:::process
    
    %% Add Expense Flow
    C --> F((💬 Input Details)):::action
    F --> G{🛡️ Validate Input}:::decision
    G -->|✔️ Valid| H[✔️ Add to Expense List]:::process
    G -->|❌ Invalid| I((❗ Show Error)):::highlight
    H --> J[📋 Display in Expense Table]:::action

    %% View by Category Flow
    D --> K[📑 Group Expenses by Category]:::process
    K --> L((📋 Display Totals)):::action

    %% Generate Pie Chart Flow
    E --> M[📥 Fetch Expense Data]:::process
    M --> N[📊 Create Pie Chart]:::process
    N --> O((📈 Show Chart)):::highlight

    %% Feedback Loops
    J --> B
    L --> B
    O --> B

    %% Styles
    linkStyle default stroke:#0077b6,stroke-width:2,color:#000;
    style A fill:#f4f9f4,stroke:#2a9d8f,stroke-width:3;
    style B fill:#a8dadc,stroke:#457b9d,stroke-width:3,stroke-dasharray: 5 5;



