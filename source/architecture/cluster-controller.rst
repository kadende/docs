ClusterController
=================

This is a stateless app that its called with a cluster id.
With the cluster id it gets the cluster configuration and cluster resources from the store.

cluster configuration is the spec that was given by the user, and cluster
resources is all the resources that cluster controller has created.

Its main job is to maintain the size and health of a cluster.


A cluster configuration contains a group of clusters. Each cluster is a group of resources of the
same resource type.

Sample cluster configuration
        .. literalinclude:: ../_static/cluster_configuration_samples/basic_cluster.yml

Fields that cluster configuration has:
    1. id (Optional field)
        This would be the pk of the cluster configuration in
        the store.

        If not defined a generic one would be generated.

    2. version (Mandatory field)
        This contains the version of the cluster

    3. name (Mandatory field) - should be unique
        This contains the name of the cluster.

    4. groups (Mandatory field)
        this is a list of one or more group.

        Fields in a group:
            - resourcePlugin
                This defines the plugin that's going to create
                the resource.

                It requires the following fields:
                    - name
                    - version (optional defaults to latest)
                    - url (optional if you want to define your own plugin)


            - resourceProperties
                This defines properties that are going to be used by
                the resourcePlugin to create resource.

                The fields are determined and validated by the plugin you selected.

Cluster controller workflow
----------------------------

   .. raw:: html
      :file: ../_static/cluster_controller_workflow.html


Flow:
    1. Given cluster id
        We get cluster configuration and cluster resources from the store.

    2. Loop.
        We then loop each group.

        In each loop we do the flowing.
            - Get all the resources via tags and return those whose status is active.
              check the instance that we have got are the ones in our cluster resource

              Will archive this by calling resourcePlugin describe method.

            - Delete those instance that are not in our cluster resources.

            - check if the number of the resources matches the number of the cluster group.
              create/delete to maintain the cluster size.

            - Store all events in the store to be used by the ui.
