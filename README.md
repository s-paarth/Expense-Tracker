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
    A[User Starts Application] --> B{Select an Action}
    B --> C[Add Expense]
    B --> D[View Expenses by Category]
    B --> E[Generate Pie Chart]
    
    C --> F[Input Date, Category, Amount, Description]
    F --> G[Validate Input]
    G -->|Valid| H[Add to Expense List]
    G -->|Invalid| I[Show Error Message]
    H --> J[Display on Expense Table]
    
    D --> K[Group Expenses by Category]
    K --> L[Show Totals in Table]
    
    E --> M[Fetch Expense Data]
    M --> N[Generate Pie Chart]
    N --> O[Display Pie Chart]
    
    J --> B
    L --> B
    O --> B



