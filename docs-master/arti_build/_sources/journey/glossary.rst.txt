.. include:: /common/global.rst

|acquia-product:aj| glossary
============================

|acquia-product:aj| has several terms that have specific definitions
based on their use in the product.

+-----------------------------------+-----------------------------------+
| Term                              | Definition                        |
+===================================+===================================+
| Hub                               | The |acquia-product:aj| Hub can   |
|                                   | be accessed from any browser. We  |
|                                   | recommend Chrome, Firefox or      |
|                                   | Safari.                           |
+-----------------------------------+-----------------------------------+
| Journey Mapper                    | Using the Journey Mapper, you can |
|                                   | craft a high level customer       |
|                                   | journey, identifying channels and |
|                                   | decisions, which link directly to |
|                                   | the execution of the journey.     |
+-----------------------------------+-----------------------------------+
| Metrics                           | Built into the software is a way  |
|                                   | to measure the efficiency of the  |
|                                   | Journey at different steps. Basic |
|                                   | Metrics measure counts or         |
|                                   | currency amounts and Compound     |
|                                   | Metrics display a percentage of   |
|                                   | any combination of Basic Metrics. |
+-----------------------------------+-----------------------------------+
| Version                           | At each major milestone when      |
|                                   | working on a Project, we          |
|                                   | recommend creating a Version. You |
|                                   | can test or deploy (run) any      |
|                                   | version of a Project.             |
+-----------------------------------+-----------------------------------+
| Environment                       | Environments are defined usually  |
|                                   | as 'Development',                 |
|                                   | 'UserAcceptance' and              |
|                                   | 'Production'. You can make as     |
|                                   | many environments in a Project as |
|                                   | you need. In a new Project, there |
|                                   | is a 'default' environment        |
|                                   | automatically created and it can  |
|                                   | be renamed at anytime.            |
+-----------------------------------+-----------------------------------+
| Connections                       | |acquia-product:aj| Connections   |
|                                   | are the definitions of all the    |
|                                   | connections in a Project: for     |
|                                   | example connections to a          |
|                                   | particular database, web service  |
|                                   | API or to Twitter.                |
+-----------------------------------+-----------------------------------+
| Node                              | The colorful icons represent      |
|                                   | decisions or actions on a         |
|                                   | connection. Every node send,      |
|                                   | receives, transforms or returns   |
|                                   | data.                             |
+-----------------------------------+-----------------------------------+
| Adaptor                           | Once a Connection is made, an     |
|                                   | Adaptor defines an action on that |
|                                   | connection: for example replying  |
|                                   | to a Tweet using a Twitter        |
|                                   | connection.                       |
+-----------------------------------+-----------------------------------+
| Link                              | Links connects Nodes. The         |
|                                   | standard links are the 'goto' and |
|                                   | 'error'. You can also have        |
|                                   | conditional nodes with Basic or   |
|                                   | Advanced operations before moving |
|                                   | to the next node.                 |
+-----------------------------------+-----------------------------------+
| Graph                             | This is the actual executable     |
|                                   | representation of the journey.    |
|                                   | Graphs are made up of Nodes and   |
|                                   | Links.                            |
+-----------------------------------+-----------------------------------+
| Deployments                       | This consists of all Graphs in    |
|                                   | the Project that have a Listener  |
|                                   | and can be 'deployed' or run. The |
|                                   | Graphs are grouped under each     |
|                                   | Environment in that Project. The  |
|                                   | Deployments screen gives the      |
|                                   | status of each Graphs: Starting,  |
|                                   | Running, Stopping, Warning or     |
|                                   | Critical.                         |
+-----------------------------------+-----------------------------------+
