import boto3

def check_ec2_security_groups():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()
    security_groups = response['SecurityGroups']
    
    vulnerable_groups = []
    for group in security_groups:
        # Check if security group allows unrestricted inbound access
        ip_permissions = group['IpPermissions']
        for permission in ip_permissions:
            if '0.0.0.0/0' in [ip_range.get('CidrIp') for ip_range in permission.get('IpRanges', [])]:
                vulnerable_groups.append(group)
                break
    
    return vulnerable_groups

def check_s3_bucket_permissions():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = response['Buckets']
    
    vulnerable_buckets = []
    for bucket in buckets:
        bucket_name = bucket['Name']
        acl_response = s3.get_bucket_acl(Bucket=bucket_name)
        bucket_acl = acl_response['Grants']
        
        for grant in bucket_acl:
            # Check if the bucket has any public access
            grantee = grant.get('Grantee', {})
            if grantee.get('Type') == 'Group' and grantee.get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                vulnerable_buckets.append(bucket_name)
                break
    
    return vulnerable_buckets

def check_rds_public_access():
    rds = boto3.client('rds')
    response = rds.describe_db_instances()
    instances = response['DBInstances']
    
    vulnerable_instances = []
    for instance in instances:
        # Check if the RDS instance is publicly accessible
        is_public = instance.get('PubliclyAccessible', False)
        if is_public:
            vulnerable_instances.append(instance['DBInstanceIdentifier'])
    
    return vulnerable_instances

def main():
    # AWS credentials setup
    aws_access_key_id = 'YOUR_ACCESS_KEY' #provide your key
    aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'  #provide your key
    region_name = 'us-east-1'  # Replace with your specific region
    
    # Configure AWS session
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
    boto3.setup_default_session(session)

    # Check EC2 security groups
    vulnerable_ec2_groups = check_ec2_security_groups()
    print("Vulnerable EC2 Security Groups:")
    for group in vulnerable_ec2_groups:
        print(f"Group ID: {group['GroupId']}")
    
    # Check S3 bucket permissions
    vulnerable_s3_buckets = check_s3_bucket_permissions()
    print("\nVulnerable S3 Buckets:")
    for bucket in vulnerable_s3_buckets:
        print(f"Bucket Name: {bucket}")
    
    # Check RDS public access
    vulnerable_rds_instances = check_rds_public_access()
    print("\nVulnerable RDS Instances:")
    for instance in vulnerable_rds_instances:
        print(f"DB Instance ID: {instance}")

if __name__ == '__main__':
    main()
