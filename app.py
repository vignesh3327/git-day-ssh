import subprocess

# EKS cluster configuration
cluster_name = "test"
region = "us-east-2"
node_type = "t2.medium"
nodes = 7

# Build eksctl command
command = [
    "eksctl", "create", "cluster",
    "--name", cluster_name,
    "--region", region,
    "--node-type", node_type,
    "--nodes", str(nodes)
]

try:
    print("Creating EKS cluster...")
    
    # Run command
    result = subprocess.run(
        command,
        check=True,
        text=True,
        capture_output=True
    )
    
    print("Cluster created successfully!")
    print(result.stdout)
    
except subprocess.CalledProcessError as e:
    print("Error while creating cluster")
    print(e.stderr)
