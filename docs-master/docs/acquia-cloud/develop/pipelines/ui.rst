.. include:: /common/global.rst

Managing your pipelines in the |acquia-product:ac| interface
============================================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/pipelines/ui/*

|acquia-product:ac| provides you the ability to start and track your
different pipeline jobs with both an application in the user interface
and a command-line interface.

Accessing the pipelines user interface
--------------------------------------

To view information about your pipelines in |acquia-product:ac|,
complete the following steps:

#. Sign in to the |acquia-product:ac| interface with an account that has
   `the **Execute pipelines**
   permission </acquia-cloud/teams/roles#edit>`__.
#. Select the application that you want to use.
#. In the left menu, click **Pipelines**.

The first time you visit the page, you can select from one of the
following options:

-  Select a source for your repository
-  Start a pipeline job
-  View the available environments

Follow-on visits to the page (after you have configured your repository
connection) will display a list of the logged pipeline jobs.

Managing your repository connection
-----------------------------------

|acquia-product:ac| displays information about your repository
connection, including its URL and several common Git commands. To
examine or change your the repository connected to your application, on
the `**Pipelines** page <#access>`__ click **More Links**.

|More Links icon|

You can then click **View Connection Info**, which allows you to change
to a different repository for your application. To do this, click the
**Configure** link, select the type of repository that you want to use,
and then complete its configuration based on your repository. For
information about using this process to connect to external code
repositories, see `Connecting an application to an external Git
repo </acquia-cloud/develop/pipelines/connect>`__.

Webhooks
~~~~~~~~

|acquia-product:ac| users using Acquia's native Git installation can
enable or disable webhooks in the **Configure** page by selecting the
desired option from the **Webhooks** list.

#. Sign in to your |acquia-product:ac| account.
#. Select an application.
#. Click **Pipelines**.
#. Click **More links > View Application Info**.
#. In the **Webhooks** section, click **Enable** or **Disable** as
   required.

|acquia-product:ac| will display a confirmation dialog box in the upper
right of the webpage.

.. _activity:

Reviewing job activity
----------------------

The **Job List** page for |acquia-product:ac| provides an overview of
the pipeline jobs that are both currently processing or have already
completed. The webpage will regularly update to include any new jobs, or
to reflect the status of any on-going or newly completed jobs. To learn
more about the overview page, see `Viewing pipelines job
history </acquia-cloud/develop/pipelines/ui/history>`__.

Detailed information about any job listed on the **Job List** page can
be found by clicking on the job's name in in the **Job** column. To
learn more about reading detailed job information, see `Viewing job
output </acquia-cloud/develop/pipelines/ui/output>`__.

Starting a pipeline job
-----------------------

To start a new pipeline job from the |acquia-product:ac| interface,
complete the following steps:

#. Select the application for which you want to start a pipelines job.
#. In the left menu, click **Pipelines**.
#. Click **Start Job**.

   |Start Job icon|

   |acquia-product:ac| will display a **How to start a job** dialog.

#. In the **Branch Name** field, enter the name of the branch that
   contains the `build definition
   file </acquia-cloud/develop/pipelines/yaml>`__ that you want to use.
#. Click **Start**.

You may execute a maximum of two jobs at one time.

.. |More Links icon| image:: https://cdn4.webdamdb.com/310th_sm_UIzMSRVRQXA0.png?1526475481
   :width: 273px
   :height: 78px
.. |Start Job icon| image:: https://cdn2.webdamdb.com/310th_sm_sskId2i7C1A0.png?1526475442
   :width: 260px
   :height: 71px
