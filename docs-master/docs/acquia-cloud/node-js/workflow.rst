.. include:: /common/global.rst

Deploying build artifacts in your Node.js environment
=====================================================

|acquia-product:ac| Node.js applications have two types of environments:
*development* and *production*. These environments leverage
`pipelines </acquia-cloud/develop/pipelines>`__ for building
applications and adding them to your environments.

When you have a build artifact, you can deploy it from one environment
to another in a `workflow similar to your </acquia-cloud/develop/pipelines>`__ 
|acquia-product:ac| environment.

The **Code** elements of the |acquia-product:ac| Environments webpage
provide a user interface for deploying build artifacts from your
repository to your application's environments. When you commit an
artifact to your repository, |acquia-product:ac| updates the environment
running that build artifact. You must then deploy that artifact to make
it available for use.

.. important::

      You should make and test changes to your application in your Development
      environment only. Do not make or test changes in your Production
      environment. If you make a change that breaks your application in the
      Production environment, you might bring your live application down. If
      this happens, your application will fail to start, and will retry on a
      regular basis. Failures `are logged </acquia-cloud/monitor/logstream>`__.

Complete the following steps when you're ready to deploy a build
artifact to an environment:

#. Check out your repository to your local computer.
#. Use the pipelines feature to create a build artifact — artifacts are
   not deployed by |acquia-product:ac|.
#. Deploy your artifact, either in the `same
   environment <#deploy-same>`__ or `between environments <#move>`__.

.. note::

In general, Node.js applications should have little downtime due to
deployment. Although artifacts can take several seconds to build and
deploy, application processes are rotated with new deployment code, with
the platform waiting for your service to be listening before switching
to the next process.

.. _deploy-same:

Deploying a build artifact in the same environment.
---------------------------------------------------

Use one of the following methods to deploy a build artifact in the same
environment:

- Using the **Environments** page
   To switch the code deployed in an environment from one artifact to
   another, using the **Environments** page, complete the following
   steps:

   #. In the **Code** element for the environment, click the code switch
      button.

      |Switch build artifacts button|

   #. In the **Switch artifact** dialog box, select an artifact, and
      then click **Continue**.
   #. In the **Switch artifact** confirmation dialog box, click
      **Switch**.

   When you select build artifact to deploy, that code is retrieved from
   your repository and deployed to the appropriate environment on the
   web servers. The deploy task appears in the `Activity task
   list </acquia-cloud/monitor/tasks>`__.
- From the **Environment Overview** page
   You can deploy an artifact on an environment or copy an artifact from
   one environment to another using the Overview page of an environment.
   To switch the code deployed in an environment from one artifact to
   another, using the Overview page, complete the following steps:

   #. On the **Environments** page, click the name of the environment to
      open that environment's **Overview** page.
   #. On the **Overview** page for the environment, click **Switch**.
   #. In the **Switch artifact** dialog box, select a build artifact,
      and then click **Continue**.
   #. In the **Switch artifact** confirmation dialog box, click
      **Switch**.

.. _move:

Moving code from one environment to another
-------------------------------------------

To move code from one environment to another, use one of the following
processes, depending on your location in the |acquia-product:ac|
interface:

- From the **Environments page**

  #. Drag a **Code** element from **Dev** to **Prod**.
     A **Deploy artifact** confirmation appears.
  #. Click **Deploy**.

     |Deploying an artifact to production|

- From the **Environment Overview** page

  To copy code from one environment to another (creating a new tag and
  deploying it) using the Overview page:

  #. On the **Environments** page, click the name of the environment to
     open that environment's **Overview** page.
  #. On the **Overview** page for the environment, click **Deploy**.
  #. In the **Deploy artifact** dialog box, select the artifact to
     copy, and then click **Continue**.
  #. In the **Deploy artifact** confirmation dialog box, click
     **Deploy**.

.. _revert:

Reverting code
--------------

To revert code to an earlier version, complete the following steps:

#. In the **Code** element for the environment, click the code switch
   button.
#. In the **Switch artifact** dialog box, select the tag for the version
   to which you want to revert, and then click **Continue**.
#. In the **Switch artifact** confirmation dialog box, click **Switch**.

When you deploy a previous build artifact, |acquia-product:ac| retrieves
the code snapshot from your repository and then deploys it on the
appropriate environment on the web servers.

.. |Switch build artifacts button| image:: https://cdn2.webdamdb.com/1280_kcnbrk0T7C05.png?1526475935
   :width: 718px
   :height: 326px
.. |Deploying an artifact to production| image:: https://cdn4.webdamdb.com/1280_AUcNL1n21Tr6.png?1526476044
   :width: 600px
   :height: 354px
