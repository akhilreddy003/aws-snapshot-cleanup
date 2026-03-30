import boto3
from datetime import datetime, timedelta, timezone

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    try:
        snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
        
        now = datetime.now(timezone.utc)
        cutoff_date = now - timedelta(days=365)

        for snapshot in snapshots:
            snapshot_id = snapshot['SnapshotId']
            start_time = snapshot['StartTime']

            if start_time < cutoff_date:
                try:
                    print(f"Deleting snapshot: {snapshot_id}")
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                except Exception as e:
                    print(f"Error deleting {snapshot_id}: {str(e)}")

        return {
            'statusCode': 200,
            'body': 'Snapshot cleanup completed'
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        raise e