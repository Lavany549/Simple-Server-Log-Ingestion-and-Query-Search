# Log Management System

## Assumptions

-  Logs are injected into the server in the form of single entry (`log_data.json`) or multiple entries (`bulk_log_data.json`). This is provided in the second code snippet of `main.ipynb` file.
- `server.py` has two functionalities: receiving the log_data and pushing it into `logs.csv` file.
- Queries are given manually. Each time, a single or multiple queries are given with the number of queries mentioned before.
   -  Example:
      -  4
      -  Find all logs with the level set to "error".
      -  Search for logs with the message containing the term "Failed to connect".
      -  Retrieve all logs related to resourceId "server-1234".
      -  Filter logs between the timestamp "2023-09-10T00:00:00Z" and "2023-09-15T23:59:59Z".
- As there is only a single form of .json entries, a standard .csv file has been considered as a substitute for a database (DB).
- All the output is to be displayed and is saved as entries in `Queryn.csv` files for each query.

   *Note: Nothing is mentioned in the document regarding the output.*

## Dependencies

Install the required dependencies using the following commands in the `main.ipynb` file:

```bash
%pip install qdrant-client
%pip install nltk
%pip install -U sentence-transformers
%pip install langdetect
%pip install flask
%pip install flask_restful
%pip install pandas
%pip install requests
%pip install random
%pip install json
 ```
## Environment
- **Jupyter Notebook in VSCode**
- **Python Version Used:** 3.7.9
## Architecture
![Architecture](/images/architecture.jpg)

## Procedure to Run the Code

1. **Run the Server:**
   - Open the terminal and execute the following command:
     ```bash
     python server.py
     ```
   - This command runs the server locally on port 3000.

2. **Ingest Log Data:**
   - Open the `main.ipynb` file.
   - **Step 1:**
     - Modify the code in the 2nd code snippet.
     - Insert your data as a JSON file or parts of a JSON file.(Or upload it as log_data.json/bulk_log_data.json file according to the need)
     - This code ingests the JSON log_data into the server. Execute by pressing Ctrl+Enter.
   - **Step 2:**
     - The 3rd code snippet takes queries, finds the filters, and searches in the `logs.csv` file.
     - Returns the output for each query. Execute by pressing Ctrl+Enter.

## Features Implemented

- **Search Capabilities:**
  - Implemented search within specific date ranges.
  - Utilized regular expressions for search.
  - Allowed combining multiple filters.

- **Real-time Log Ingestion:**
  - Provided real-time log ingestion and searching capabilities.

- **Scalability:**
  - Adaptable to increasing volumes of logs/queries.
  - Efficient in returning search results.

- **Performance:**
  - System is capable of ingesting massive volumes.
