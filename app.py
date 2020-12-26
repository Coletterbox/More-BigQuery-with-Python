from google.cloud import bigquery

client = bigquery.Client()

testQuery = """
    SELECT * FROM `apprenticeship-299321.sample_data.datatable`
    LIMIT 10
"""

query = """
    SELECT * FROM `apprenticeship-299321.sample_data.datatable`
"""

results = client.query(query)

for row in results:
    print(str(row))