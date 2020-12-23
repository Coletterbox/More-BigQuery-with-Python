# More BigQuery with Python

- Project ID: apprenticeship-299321
- Open Cloud Shell
```
gcloud auth list
gcloud config list project
```
- If not already set:
```
gcloud config set project apprenticeship-299321
```
```
[redacted]@cloudshell:~ (apprenticeship-299321)$ gcloud services list
ERROR: (gcloud.services.list) User [[redacted]@gmail.com] does not have permission to access projects instance [
apprenticeship-299321] (or it may not exist): The caller does not have permission
[redacted]@cloudshell:~ (apprenticeship-299321)$ gcloud services enable bigquery.googleapis.com
ERROR: (gcloud.services.enable) PERMISSION_DENIED: The caller does not have permission
```
```
export PROJECT_ID=$(gcloud config get-value core/project)
gcloud iam service-accounts create bigquery-sa \
  --display-name "bigquery service account"
```
```
ERROR: (gcloud.iam.service-accounts.create) User [[redacted]@gmail.com] does not have permission to access proje
cts instance [apprenticeship-299321] (or it may not exist): Permission iam.serviceAccounts.create is required to perf
orm this operation on project projects/apprenticeship-299321.
```
- https://cloud.google.com/docs/authentication/getting-started ("Creating a service account")
- "You don't have permission to create a new service account and key."
