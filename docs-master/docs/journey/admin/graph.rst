.. include:: /common/global.rst

Deploying graphs
================

After you've visually tested a graph, you can deploy it into an
environment. To learn more about environments in |acquia-product:aj|,
read `Creating and managing environments </journey/admin/env>`__.

Viewing graphs
--------------

To view the graphs that are available for deployment, and to also view
any currently deployed graphs, complete the following steps:

#. In the top menu, click **Admin**.
#. In the left menu, click **Projects**.
#. Find your project in the project list, and then click its project
   name.
#. In the project's detail view, click **Deployments**.

|Deployment view|

The **Deployable Graphs** view will display all deployable graphs in
each environment. A deployable graph is any valid graph that has a
listener node; if a graph does not have a listener, |acquia-product:aj|
will not display the graph in the list. The currently-active version of
the graph, selected from the **Versions** tab, will be deployed.

If the environment does not have valid connections, then the **Invalid
Connections** message will be displayed.

If the listener graph is using the |graph api|_, then the endpoint will be
different for the chosen environment, allowing you to deploy to a higher
production environment while continuing development in your
non-production environment.

.. |graph api| replace:: \ |acquia-product:aj| \ Graph API
.. _graph api: /journey/adaptors/graph-api

Starting and stopping a graph
-----------------------------

To deploy a graph, start it by clicking its deploy icon |Deploy icon|.

Your graphs will continue to execute until you click the halt icon |Halt
icon|.

Deployment alerts
-----------------

After you deploy a graph, |acquia-product:aj| will email any execution
problems it encounters to contacts in the **Contacts** detail view of
the **Project Admin** page. For information about adding contacts, see
`the documentation for Contacts </journey/Contacts>`__.

Deployment alert emails have the following format:

::
  Subject: Acquia Journey 2016 Deployment Event Alert
  Date: January 18, 2017 at 1:10:50 AM EST
  To: <Contact>
  From: <no-reply@acquia.com>
  This is an automated email from Acquia Journey.
  There was a Deployment State Change, from: Running to Critical, for the graph detailed below.
  <ERROR MESSAGE>
  Deployment Details:
  Graph Name: <Graph Name>
  Version: <Version or Current>
  Project: <Project Name>
  Environment: <Environment Name>
  Organization: <Organization Name>

.. |Deployment view| image:: https://cdn2.webdamdb.com/1280_cyOiEzWuf792.png?1527090818
   :width: 753px
   :height: 551px
.. |Deploy icon| image:: https://cdn3.webdamdb.com/1280_UYeo83n0Bp13.png?1527090824
   :width: 46px
   :height: 28px
.. |Halt icon| image:: https://cdn3.webdamdb.com/1280_EYNG0Z5Mf1k6.png?1527090832
   :width: 46px
   :height: 28px
