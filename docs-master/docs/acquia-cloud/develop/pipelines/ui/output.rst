.. include:: /common/global.rst

Viewing job output
==================

The **Job Detail** page for the pipelines feature provides detailed
information about jobs that are either currently processing or have
already completed their execution.

.. _access:

Viewing job output
------------------

To view detailed information about your |acquia-product:ac| pipelines
jobs in |acquia-product:ac|, from your application click **Pipelines**
from its left menu, and then scroll down the page to the **Activity**
table in the **Jobs** section.

|Activity table example|

To view information about a specific job, in the **Activity** table,
click the name of the job you want to view.

For information on how to view a list of all recent jobs, see `Viewing
pipelines job history </acquia-cloud/develop/pipelines/ui/history>`__.

.. _summary:

Understanding the job summary table
-----------------------------------

The job summary table provides an overview of the settings for a job,
and includes the following information:

|Job summary table|

-  **Destination environment** – The |acquia-product:ac| environment to
   which this job will deploy code.
-  **Job Duration** – The duration for which this job ran.
-  **Started at** – The date and time when the job started.
-  **Job Trigger** – The event that triggered this job. Possible
   triggers include the following:

   -  **Branch commit** – A new commit was made to the repository.
   -  **Pull request** – A pull request was submitted or updated

-  **Branch** – The Git branch used to run this job.
-  **Requested by** – The user who initiated this job.

.. _logs:

Reading job logs
----------------

The **Logs** section on your job's detail page provides the full output
of all of the logging that relates to your job. To increase legibility,
only the title of each step is displayed by default. Click the title of
a step to reveal all logs for that step.

|Select a step to view its logs|

When you expand a job, |acquia-product:ac| displays additional details,
as in this example of the full **Finalization** step:

``Finalization   + echo "Exiting step composer." Killing background jobs  Changes will be pushed to pipelines-build-2 [example@svn0000.prod.hosting.acquia.com:example.git]  Your deployment branch is: demobranch To example@svn-0000.prod.hosting.acquia.com:example.git    000000..322ca6a  pipelines-build-2 -> pipelines-build-2  Successfully completed.``

.. note:: If you have questions about any error messages displayed in your job logs, `contact Acquia Support </support#contact>`__.

.. _rerun:

Rerunning a job
---------------

After you have encountered and corrected an error that caused a job to
fail, use the following these steps to run the job a second time:

#. Find and click the job that you want to run again in the **Activity**
   table.
#. Click the **Rerun Job** icon. |Rerun job|
#. Click **Yes**.

.. |Activity table example| image:: https://cdn2.webdamdb.com/md_k86Hsfatqm23.png?1526475455
   :alt: Activity table example
.. |Job summary table| image:: https://cdn4.webdamdb.com/md_MUD5RrrfZD02.png?1526475603
   :alt: Job summary table
.. |Select a step to view its logs| image:: https://cdn2.webdamdb.com/310th_sm_QsTwsECtkoZ3.png?1526475451
   :alt: Select a step to view its logs 
.. |Rerun job| image:: https://cdn2.webdamdb.com/100th_sm_20bzzEJQ8lx1.png?1526475574
   :width: 50px
   :alt: Rerun job