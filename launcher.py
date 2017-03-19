import boto3
from pathlib import Path
from click import command, option
from os import system

@command()
@option("--commit_file_path", help="Path for the commit file produced by codecommit.py")
@option("--version_label", help="version label")
def main(commit_file_path, version_label):


	#TODO: Check for existence of file

	print("Before running this script, ensure that you have the latest revision of the mojio-amazon repository from github.\n")

	bean_client = boto3.client('elasticbeanstalk')

	with open(commit_file_path, 'r') as f:
		commit_id = f.readline()


	SourceLocate = str('mojio-amazon/' + commit_id).strip('\n').strip('\t')

	print(SourceLocate)

		
	response = bean_client.create_application_version(
    ApplicationName='mojio-test',
    VersionLabel='{0}'.format(version_label),
    Description='app',
	Process=True,
	AutoCreateApplication=True,
    SourceBuildInformation={
        'SourceType': 'Git',
        'SourceRepository': 'CodeCommit',
        'SourceLocation': '{0}'.format(SourceLocate)#'mojio-amazon/c0d215f442dc33829682850a8e53b7283d5564b5'
    }
	)


if __name__ == "__main__":
	main()
