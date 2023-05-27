# AWS-Configuration-Review-Tool

The provided code is a Python script that utilizes the boto3 library, which is the AWS SDK for Python. It allows you to interact with various AWS services programmatically. The script aims to perform a configuration review and vulnerability assessment of selected AWS services, namely EC2 instances, S3 buckets, and RDS instances. Further Services will be Attached Later.

To perform a vulnerable configuration review of AWS services using Python, you can utilize the AWS SDK (boto3) to retrieve the necessary information and perform checks against known security best practices. Please make sure you have installed the boto3 library before proceeding.

# Here's a breakdown of the code and its usage:

1.The script starts by importing the boto3 library, which needs to be installed beforehand.

2.It defines several functions that are responsible for retrieving information and performing vulnerability checks on different AWS services:
    - `check_ec2_security_groups()`: Retrieves the EC2 security groups and checks if any of them allow unrestricted inbound access from any IP address (0.0.0.0/0).
    - `check_s3_bucket_permissions()`: Retrieves the S3 buckets and checks if any of them have public access permissions granted to all users.
    - `check_rds_public_access()`: Retrieves the RDS instances and checks if any of them are publicly accessible.
    
3.The main() function is the entry point of the script. It sets up the AWS credentials (access key and secret access key) and the desired AWS region.

4.Inside the main() function, the vulnerability checks are performed for each AWS service using the respective functions mentioned above.

5.The script prints the vulnerable configurations found for each service:
    - For EC2 instances, it prints the vulnerable security group IDs.
    - For S3 buckets, it prints the names of the vulnerable buckets.
    - For RDS instances, it prints the identifiers of the publicly accessible instances.

# Usage:--

1.Ensure that you have Python installed on your system.

2.Install the boto3 library by running the following command:
  ``` pip install boto3 ```

3.Replace the placeholders 'YOUR_ACCESS_KEY' and 'YOUR_SECRET_ACCESS_KEY' with your actual AWS access key and secret access key.

4.Adjust the region_name variable according to your desired AWS region.

5.Run the script.

6.The script will retrieve the relevant information and perform vulnerability checks for the selected AWS services. It will then display any vulnerable configurations found for EC2 instances, S3 buckets, and RDS instances.


# Happy Coding ! 📸
