from clusters import ClusterCollection

if __name__ == '__main__':
    # Create cluster using cluster collection
    clusters = ClusterCollection([
        {
            "id": 1,
            "create_script_command": ["bash", "-c", "./create.sh"],
            "shutdown_script_command": ["bash", "-c", "./delete.sh"],
        }
    ])

    # Get Cluster by ID
    cluster = clusters.get_by_id(1)

    # # TEST CREATE
    # # Call startup to execute create script
    # print(cluster.startup())
    #
    # # Print current cluster state
    # print(cluster.state)




    # # TEST SHUTDOWN
    # # Call shutdown to execute delete script
    # print(cluster.shutdown())
    #
    # # Print current cluster state
    # print(cluster.state)
