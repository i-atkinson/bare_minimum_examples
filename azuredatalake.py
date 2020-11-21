from azure.storage.filedatalake import DataLakeServiceClient

storage_account_name="account_name"
storage_account_key="account_key"
container_name="container_name"
directory_name="directory_name"
file_name="file_name"
file_contents="file_contents"

#Data Lake
service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
        "https", storage_account_name), credential=storage_account_key)

#Container
file_system_client=service_client.get_file_system_client(container_name)

#Directory
file_system_client.create_directory(directory_name)
#or
file_system_client.get_directory_client(directory_name)

#Upload file
file_client=directory_client.create_file(file_name)
file_client.append_data(data=file_contents, offset=0, length=len(file_contents))
file_client.flush_data(len(file_contents))