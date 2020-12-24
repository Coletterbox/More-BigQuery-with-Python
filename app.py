from google.cloud import bigquery

client = bigquery.Client()

testQuery = """
    SELECT * FROM `apprenticeship-299321.sample_data.datatable`
    LIMIT 10
"""

results = client.query(testQuery)

for row in results:
    print(str(row))