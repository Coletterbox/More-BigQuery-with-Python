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

testQuery1 = """
    SELECT * FROM `apprenticeship-299321.sample_data.datatable`
    LIMIT 100
"""

query = """
    SELECT * FROM `apprenticeship-299321.sample_data.datatable`
    ORDER BY date ASC
"""

query1 = """
    SELECT COUNT(*) FROM `apprenticeship-299321.sample_data.datatable`
"""

query2 = """
    SELECT deviceCategory, COUNT(*) AS deviceCategoryCount
    FROM `apprenticeship-299321.sample_data.datatable`
    GROUP BY deviceCategory
    ORDER BY deviceCategoryCount ASC
"""

query3 = """
    SELECT channelGrouping, COUNT(*) AS channelGroupingCount
    FROM `apprenticeship-299321.sample_data.datatable`
    GROUP BY channelGrouping
    ORDER BY channelGroupingCount ASC
"""

query4 = """
    SELECT date, COUNT(*)
    FROM `apprenticeship-299321.sample_data.datatable`
    GROUP BY date
    ORDER BY date ASC
"""

query5 = """
    SELECT deviceCategory, AVG(conversions) as averageConversionsPerDeviceCategory
    FROM `apprenticeship-299321.sample_data.datatable`
    GROUP BY deviceCategory
    ORDER BY averageConversionsPerDeviceCategory
"""

# TODO: conversions in relation to sessions probably makes more sense than just using the figure for conversions
# conversion rate for device category
# conversion rate for channel grouping
# conversion rate for date? maybe that's not useful

# TODO: clean up
# currentQuery = query5
currentQuery = query

results = client.query(currentQuery)

for row in results:
    print(str(row))