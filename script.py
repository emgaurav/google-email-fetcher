import httplib2
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

# Configuration 
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user.readonly'] 
SERVICE_ACCOUNT_FILE = '</path/to/your_json_file>' 

# Authentication
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = credentials.create_delegated('admin@domain.com') # Admin user email with necessary permissions
http = delegated_credentials.authorize(httplib2.Http())
service = discovery.build('admin', 'directory_v1', http=http) 

# Fetching Active Users and Emails
def fetch_all_users():
    email_list = []
    request = service.users().list(customer='my_customer', 
                                   query="isSuspended=false", 
                                   fields='nextPageToken,users(primaryEmail)')
    count = 0 

    while request is not None:
        users_result = request.execute()

        users = users_result.get('users', [])
        email_list.extend([user['primaryEmail'] for user in users])
        count += len(users) 
        print(f"Fetched {count} users so far...")

        request = service.users().list_next(request, users_result)

    # Writing to the text file
    with open('active_user_emails.txt', 'w') as output_file:
        for email in email_list:
            output_file.write(email + '\n')

if __name__ == '__main__':
    fetch_all_users()  # No need to fetch and store all_emails anymore
