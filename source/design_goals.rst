
Design goals
=============

Kadende cluster management is being inspired by amazon autoscaling group, infrakit(https://github.com/docker/infrakit), coorp (http://coopr.io/),
and docker cloud ( which was terminated )

Its not meant to do the work of other orchestrator like swarm and kubernetes its infact meant to work with them.

Then main goal that cluster management is trying to solve is provisioning a group on nodes in any cloud provider
and maintain the size of the cluster. And do health checks on the cluster.

What to run on the cluster is upto you i.e if you decide to run servers there or even swarm or kubernetes
its all up to the user


Design Goals.

1. Making it easy to provision a group of nodes of the same kind and maintain the cluster size

    Keep on doing health checks on the cluster if its down, terminate and create new one to maintain cluster size

    With docker-cloud it was easy to create a cluster in the providers that they supported, this worked well but you
    had to maintain the cluster size yourself, in-case the node was not reachable docker-cloud notified the user but
    they didn't maintain the cluster by themselves


    With Terraform you could archive this, provisioning a group of nodes in with any cloud provider even with you own
    data-center. But to doing health check and maintain the cluster is not the easiest solution. You might have to
    use terraform Enterprise to archive this.

    With infrakit you can achieve all of this but everything is based on cli and not apis. Was a bit difficult to host
    it in the cloud. Then their plugin architecture makes it possible to write any provider in any language but it
    does not scale well to multiple clusters and multiple nodes. i.e the plugins needs to be run high availability and
    still run infrakit in high availaibiliy.

    With coorp (http://coopr.io/) you can archive this but I didn't find it to be user friendly



2. User to have total control of how to configure his nodes and how to do health checks.

    With docker-cloud health checks are done via agent installed in the nodes reporting to cluster management.
    And you don't have any option of adding your custom healthcheck. You don't have control of customizing what will be
    installed when the cluster is being provisioned


    The rest coopr, terraform and infrakit support this.


3. Be able to run it in high available i.e capability of supporting multiple clusters and nodes

    You could archive this with docker-cloud (since it wasn't self managed)


4. Should work with any provider


5. Support for user management

    coor and docker-cloud support this the rest don't.
