import boto3

def main():

	bean_client = boto3.client('elasticbeanstalk')
	code_client = boto3.client('codecommit')



	repo_info = code_client.get_repository(
   		repositoryName='mojio-amazon'
	)

	print(repo_info)



	response = bean_client.create_application_version(
    	ApplicationName='my-app',
    	AutoCreateApplication=True,
    	Description='my-app-v1',
    	Process=True,
    	SourceBuildInformation={
        	'SourceType': 'Git',
        	'SourceRepository': 'CodeCommit',
        	'SourceLocation': 'mojio-amazon'
    	},
		VersionLabel='v1',
	)

	print(response)


if __name__ == "__main__":
	main()
