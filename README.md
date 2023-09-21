# Integrated Analytics with Azure Synapse

This repository contains a step-by-step guide and code snippets for integrated analytics using Azure Synapse Analytics. This project is designed to help you explore the capabilities of Azure Synapse Analytics, a powerful tool for data analytics and processing.

## Prerequisites

Before you begin, ensure that you have the following prerequisites:

- **Azure Subscription:** You should have an active Azure subscription with admin-level access.
- **Azure Synapse Analytics Workspace:** Provision an Azure Synapse Analytics Workspace resource in your Azure subscription using [Azure Portal](https://portal.azure.com). Make sure to give it a unique name for this project.

## Problem Statement 1 - Ingesting Data

Your first task is to explore the Azure Synapse Analytics workspace and ingest data into it. Here's a high-level overview of the steps:

1. **Provision Azure Synapse Analytics:** Using Azure Portal, provision an Azure Synapse Analytics resource.

2. **Ingest Data:** Ingest data into the Synapse Analytics workspace. We'll use a built-in copy task to do this. The data source is provided below.

   - Source Dataset: [products.csv](https://raw.githubusercontent.com/MicrosoftLearning/DP-900T00A-Azure-Data-Fundamentals/master/Azure-Synapse/products.csv)
   - Destination Type: ADLS Gen 2 (use an existing storage account)

3. **Data Transformation:** Configure the data ingestion settings, such as file format, delimiters, and compression type.

4. **Task Configuration:** Set task name, description, and other settings as needed.

5. **Run Task:** Execute the data ingestion task.

## Problem Statement 2 - Querying Data

Once the data is ingested, you'll perform data analysis and querying using SQL scripts. Here's what you need to do:

1. **Explore Data Hub:** Access the ingested data in the Azure Synapse workspace.

2. **SQL Query:** Write SQL queries to analyze the data. Start by finding the TOP 100 rows from the data.

3. **Fix Column Names:** Ensure that the column names are meaningful by adding `HEADER_ROW = TRUE` before `AS [result]` in your SQL script.

4. **Customize Query:** Update the SQL script to select the category and count as `ProductNumbers` (or any name you prefer).

5. **Publish Script:** Save and publish the updated SQL script with a descriptive name, e.g., "Count Products by Category."

6. **Visualize Data:** Use the Develop hub to run the script as a Built-in SQL pool and visualize the result using a column chart.

## Problem Statement 3 - Data Analysis with Apache Spark

In this task, you'll analyze the data using Apache Spark. Follow these steps:

1. **Create Spark Pool:** In the Manage hub, create a new Spark pool with the specified settings.

2. **Python Notebook:** Create a new notebook in the Synapse workspace, set the language to PySpark (Python), and load the data into a DataFrame.

3. **Run Python Code:** Execute Python code in the notebook to analyze the data using the Spark pool.

4. **Visualize Data:** Visualize the results in the notebook using the same chart settings as in Problem Statement 2.

## Validation Use Cases

- Azure Synapse workspace is successfully created.
- Data is ingested using HTTP and stored in ADLS Gen 2.
- Data analysis is performed using both SQL pool and Spark pool.
- Code snippets for data analysis are provided.
- Resources are cleaned up and deleted after completing the tasks.

## Cleanup

After completing the project or for any testing purposes, make sure to discard all changes and delete the Azure resources to avoid unnecessary costs.

---

Feel free to follow the step-by-step instructions and use the provided code snippets to explore Azure Synapse Analytics and perform integrated data analytics. If you encounter any issues or have questions, please refer to the documentation or reach out for assistance.

For more information or support, contact:

- Your Name
- Email: karishmapasha11318@gmail.com
- LinkedIn: https://www.linkedin.com/in/karishmapasha11318

Enjoy exploring Azure Synapse Analytics for integrated data analytics!
