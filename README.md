# Corporate Financial Performance Dashboard

This repository contains a Power BI project analyzing financial performance across multiple global segments. The goal was to transform raw flat-file data into a professional Star Schema data model to enable high-performance time-intelligence reporting.

## Project Overview

* **Tool Used:** Microsoft Power BI (Desktop & Query Editor)
* **Dataset:** Financial Sample (Sales, Profit, Segments, Countries)
* **Goal:** Build an executive "Header & Grid" dashboard to visualize Year-over-Year (YoY) growth and profitability drivers.
* **[Download .pbix file](./Corporate_Financial_Dashboard.pbix)**

<img width="800" alt="Corporate Dashboard Preview" src="dashboard-preview.png" />

## Technical Implementation

### 1. Data Modeling (Star Schema)
Transformed a single flat table into a optimized **Star Schema** to improve query performance and logical separation.

* **Dimension Creation:** Created dedicated dimension tables by duplicating the source, removing duplicates, and generating **Surrogate Index Keys**.
* **Fact Table:** Renamed the original table to `SALES_FACT` and replaced descriptive text columns with Foreign Keys via **Merge Queries** in Power Query.
* **Cardinality:** Established **One-to-Many (1:*)** relationships between Dimensions and the Fact table.

### 2. Advanced DAX & Time Intelligence
Instead of relying on the source data's date column, I implemented a dynamic **Date Dimension** using DAX.

* **Dim_Date Logic:** Used `CALENDAR`, `ADDCOLUMNS`, `YEAR`, `MONTH`, and `FORMAT`.
    * *Reasoning:* Creating a calendar from the Fact table causes "missing dates" (e.g., weekends with zero sales), which breaks Time Intelligence functions. The DAX `CALENDAR` function ensures a continuous timeline.
* **Measure Table:** Created a dedicated `_Measures` table to organize calculations.

### 3. Key Measures & Formulas
Implemented explicit measures using best-practice functions for error handling and filter context manipulation.

* **Profit Margin %:**
    ```dax
    Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)
    ```
    * *Note:* Used `DIVIDE` instead of `/` to automatically handle "Divide by Zero" errors.
* **Sales Last Year:**
    ```dax
    Sales Last Year = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Dim_Date[Date]))
    ```
* **YoY Growth %:**
    ```dax
    Sales YoY Growth % = DIVIDE([Total Sales] - [Sales Last Year], [Sales Last Year], 0)
    ```

### 4. Dashboard Layout
Designed using the **"Header & Grid"** layout for executive readability:
* **Header:** Top-row KPI Cards (`Sales`, `Profit`, `Growth`) aligned with Dropdown Slicers (`Region`, `Product`) to maximize screen real estate.
* **Grid:** Side-by-side comparison of **Monthly Trends** (Line Chart) and **Segment Profitability** (Clustered Bar Chart).

---

## Notes
* **Data Source:** Microsoft Financial Sample.
* **ETL Strategy:** All text-based columns were removed from the Fact table after merging to reduce file size and improve processing speed.
* **Provided here for learning and demonstration purposes.**
