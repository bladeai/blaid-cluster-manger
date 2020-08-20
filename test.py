from clusters import ClusterCollection

if __name__ == '__main__':
    # Create cluster using cluster collection
    clusters = ClusterCollection()

    print(clusters)

    print(clusters.get_all)

    clusters.create({
        "id": 12345,
        "create_script_command": ["bash", "-c", "./create.sh"],
        "shutdown_script_command": ["bash", "-c", "./delete.sh"],
    })

    print(clusters.get_by_id(12345))

    # [
    #     {
    #         "create_script_command": ["bash", "-c", "./create.sh"],
    #         "shutdown_script_command": ["bash", "-c", "./delete.sh"],
    #     }
    # ]
    #
    # # Get Cluster by ID
    # cluster = clusters.get_all[0]
    #
    # print(clusters.get_by_id(cluster.id))
    #
    # # TEST CREATE
    # # Call startup to execute create script
    # print(cluster.startup())
    #
    # # Print current cluster state
    # print(cluster.state)
    #
    # # # TEST SHUTDOWN
    # # # Call shutdown to execute delete script
    # print(cluster.shutdown())
    # #
    # # # Print current cluster state
    # print(cluster.state)
