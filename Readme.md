Project: AWS Snapshot Cleanup Lambda
🔧 IaC Tool Chosen: Terraform

Terraform was chosen for:

Simplicity
Reusability
Strong AWS support
Industry standard for DevOps roles

Deployment Steps

# Package Lambda
cd lambda
bash package.sh

# Deploy Infra
cd ../terraform
terraform init
terraform apply

Infrastructure Created

VPC
Private Subnet
Security Group
IAM Role + Policy
Lambda Function
EventBridge Rule (daily trigger)

Lambda VPC Configuration

Lambda runs inside VPC using:

Subnet ID → private subnet
Security Group → outbound internet allowed

Assumptions

Region: us-east-1
Snapshots owned by account only
Lambda has internet access (via NAT if needed)

Monitoring

CloudWatch Logs:
/aws/lambda/snapshot-cleaner
Metrics:
Invocations
Errors
Duration
