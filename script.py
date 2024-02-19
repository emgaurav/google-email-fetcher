import httplib2
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

# Configuration 
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user.readonly'] 
SERVICE_ACCOUNT_FILE = '</path/to/your_json_file>' 
MAX_RESULTS_PER_REQUEST = 500  # Adjust as needed

# Authentication
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.create_delegated('admin@domain.com') # Admin with necessary permissions
http = delegated_credentials.authorize(httplib2.Http())
service = discovery.build('admin', 'directory_v1', http=http) 

# Fetching Active Users and Emails
def fetch_users_chunk(page_token=None):
    request = service.users().list(customer='my_customer', 
                                   query="isSuspended=false", 
                                   fields='nextPageToken,users(primaryEmail)',
                                   maxResults=MAX_RESULTS_PER_REQUEST,
                                   pageToken=page_token)
    users_result = request.execute()
    users = users_result.get('users', [])
    email_chunk = [user['primaryEmail'] for user in users]
    next_page_token = users_result.get('nextPageToken')
    return email_chunk, next_page_token

def fetch_all_users():
    email_list = []
    next_page_token = None

    while True:
        email_chunk, next_page_token = fetch_users_chunk(next_page_token)
        email_list.extend(email_chunk)
        print(f"Fetched {len(email_list)} users so far...")

        if not next_page_token:
            break

    # Writing to the text file
    with open('active_user_emails.txt', 'w') as output_file:
        for email in email_list:
            output_file.write(email + '\n')

if __name__ == '__main__':
    fetch_all_users()
