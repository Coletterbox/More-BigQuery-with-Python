from google.cloud import bigquery

client = bigquery.Client()

# SCHEMA:
# date	            INTEGER	    NULLABLE	
# channelGrouping	STRING	    NULLABLE	
# deviceCategory	STRING	    NULLABLE	
# sessions	        INTEGER	    NULLABLE	
# conversions	    INTEGER	    NULLABLE	

testQuery = """
    SELECT * FROM `apprenticeship-299321.sample_data.datatable`
    LIMIT 10
"""

query = """
    SELECT * FROM `apprenticeship-299321.sample_data.datatable`
"""

query1 = """
    SELECT COUNT(*) FROM `apprenticeship-299321.sample_data.datatable`
"""

query2 = """
    SELECT deviceCategory, COUNT(*)
    FROM `apprenticeship-299321.sample_data.datatable`
    GROUP BY deviceCategory
"""

query3 = """
    SELECT channelGrouping, COUNT(*)
    FROM `apprenticeship-299321.sample_data.datatable`
    GROUP BY channelGrouping
"""

query4 = """
    SELECT date, COUNT(*)
    FROM `apprenticeship-299321.sample_data.datatable`
    GROUP BY date
    ORDER BY date ASC
"""

# conversion rate for device category
# conversion rate for channel grouping
# conversion rate for date? maybe that's not useful

results = client.query(query4)

for row in results:
    print(str(row))