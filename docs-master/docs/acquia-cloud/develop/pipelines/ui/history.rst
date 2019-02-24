.. include:: /common/global.rst

Viewing pipelines job history
=============================

The **Job List** page for |acquia-product:ac| displays the pipeline jobs in progress or recently completed.

Information about your current and completed pipeline jobs is located in the **Activity** table.

How to access job lists
-----------------------

To view information about your |acquia-product:ac| pipelines in |acquia-product:ac|, complete the following steps:

#. `Sign in to the Acquia Cloud interface <https://cloud.acquia.com>`__.
#. Select the application that you want to use.
#. In the left menu, click **Pipelines**.

|acquia-product:ac| will display information about the application's pipelines jobs.

.. _contents:

Understanding the job lists interface
-------------------------------------

The **Activity** table includes information about each of your recently completed jobs in a table, with the most recent job displayed first.

|Activity table example|

-  **Status** |--| Indicates the success or failure of the job
-  **Job** |--| Internal, reference name for the job
-  **Branch** |--| The Git branch used to execute this job
-  **Commit** |--| The commit reference from your Git repo
-  **Duration** |--| The amount of time the job took (or is taking) to complete
-  **Completed** |--| How long ago the job finished
-  **Actions** |--| If available, click the globe icon to open the environment related to the job

.. note::

   If you have any questions about the output from a job, `contact Acquia Support </support#contact>`__.

Viewing individual job output
-----------------------------

For more detailed information about any job in the **Activity** table, click its name in the **Job** column. For more information about reading and understanding job output, see `Viewing job output </acquia-cloud/develop/pipelines/ui/output>`__.

.. |Activity table example| image:: https://cdn3.webdamdb.com/1280_k86Hsfatqm23.png?1526475455g
   :width: 600px
   :height: 256px
