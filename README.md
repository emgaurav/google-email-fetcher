# Active User Email Fetcher 

This Python script fetches a list of all active user email addresses from a Google Workspace domain. It utilizes the Google Admin SDK API and is intended for compliance auditing or similar purposes.

## Requirements

* **Google Cloud Platform Project:** This script requires an active Google Cloud Platform (GCP) project.

* **Admin SDK API Enabled:**  Ensure the Admin SDK API is enabled within your GCP project. Visit: https://console.cloud.google.com/apis/library/admin.googleapis.com

* **Service Account:**  A service account with the following scope is needed:
    * `https://www.googleapis.com/auth/admin.directory.user.readonly` 

* **Python Libraries:** Please install these libraries using pip:
    * `google-api-python-client`
    * `google-auth-httplib2`
    * `google-auth-oauthlib`

## Configuration

1. **Download Service Account Credentials:** Download the JSON credentials file for your service account from your GCP project.

2. **Modify `script.py`:** Locate the script (you may rename `script.py` to suit your project). Update the following variables:
    * `SERVICE_ACCOUNT_FILE`:   Provide the path to your downloaded JSON credentials file.
    * `admin@domain.com`: Replace with an admin user in your Google Workspace domain.

## Usage

1. Execute the script: 
   ```
   python script.py  

## Output:
- The script generates progress updates in your console/terminal.
- A file named active_user_emails.txt will be created, containing a list of active user email addresses.
