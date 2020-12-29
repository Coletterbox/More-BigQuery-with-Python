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
- I think I was just trying to do things I didn't actually need to do.
- I have skipped straight to making a new Python file.

----

```
pip install jupyter_dashboards
jupyter dashboards quick-setup --sys-prefix
jupyter nbextension install --py jupyter_dashboards --sys-prefix
jupyter nbextension enable --py jupyter_dashboards --sys-prefix
conda install jupyter_dashboards -c conda-forge
```
To initialize this nbextension in the browser every time the notebook (or other app) loads:
```
jupyter nbextension enable jupyter_dashboards --py --sys-prefix
```

----

- would prefer if key was not hardcoded
- fix dates - date as int causes issues
