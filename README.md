# Expense-Tracker
flowchart TD
    A[Start] --> B[Open ExpenseTracker App]
    B --> C[User Inputs Expense Details]
    C --> D{Is Data Valid?}
    D -->|Yes| E[Add Expense to List]
    D -->|No| F[Show Error Message]
    E --> G[Update Expense Table]
    G --> H[Clear Input Fields]
    H --> B
    F --> B
    
    B --> I[User Clicks "Pie Chart"]
    I --> J[Generate Pie Chart]
    J --> K[Display Pie Chart]
    K --> B
    B --> L[End]
