.. include:: /common/global.rst

Managing cron tasks using the management console
================================================

Websites use cron to perform maintenance tasks that help them ensure
that they remain healthy. Because websites need these maintenance tasks
to run regularly, it's helpful to have cron run on a recurring,
automated schedule. To enable you to control the frequency of cron's
execution on your websites, |acquia-product:edg| provides a Cron job
page, allowing you to create, modify, and delete scheduled cron jobs.

|Cron job page|

The cron jobs that you create are specific to the environment and stack
in which they exist. For example, if you create a cron job on your
Testing environment, that job will not exist on your Production
environment unless you manually create the same job in that environment,
using the same command line and schedule.

Your created cron jobs will be executed in batches to prevent your
server from overloading, and there is no guarantee that cron jobs will
first run on specific websites. While cron jobs are executing for an
environment, your `task logs </site-factory/monitor/tasklog>`__ will
display one or more **CronController** message entries.

Creating a new cron job
-----------------------

To create a new cron job for your Factory environment, complete the
following steps:

#. Sign in to the |acquia-product:sfi| using an account with the
   |platform admin|_ role.
#. In the admin menu, click **Administration**, and then, under **Site
   Factory management**, click the **Cron** link.

   The Cron jobs page displays and lists any preconfigured cron jobs in
   your Site Factory environment.

#. Click **Add Cron job**.

   |Create a cron job|

#. Enter a descriptive **Name** for your new cron job.
#. Be sure that the **Enabled** check box is selected. If you clear this
   check box, |acquia-product:edg| will create the cron job, but will
   not execute the job based on its defined interval until the job is
   enabled.
#. If your |acquia-product:edg| has more than one
   `stack </site-factory/tiers/stacks>`__, select the stacks that this
   cron job should apply to.
#. In the **Scope** section, select from the following options based on
   your needs:

   -  **Sites with custom domains only**
   -  **Sites without custom domains only**
   -  **All sites**

#. In the **Drush command** field, enter the command that you want to
   schedule for execution. For example, to schedule cron to run on your
   websites, enter ``cron`` in the field. Do not include a ``--uri``
   option or Drush aliases, as these will be added by
   |acquia-product:edg|. For information about additional, advanced
   options that are available for this field, see 
   `Evaluating PHP in cron jobs <#evaluating-php-in-cron-jobs>`__
#. In the **Interval** field, enter how often you want to run the
   command using the 
   `cron time string format </articles/cron-time-string-format>`__.

   .. note::  

      -  We suggest that you run cron based on a 12-hour interval (for
         example, ``* */12 * * *``).
      -  Running cron jobs too frequently can affect performance.

#. Based on your Drush command and its interval, enter a value for the
   **Percentage of threads to use**. We recommend entering ``60`` for
   this field because it effectively balances the cron job's utilization
   against any other cron jobs you may have already created for the
   environment.
#. Click **Continue**.


Modifying or removing cron jobs
-------------------------------

You can manage all of your created cron jobs from the **Cron jobs**
page, including editing or deleting cron jobs.

Editing cron jobs
~~~~~~~~~~~~~~~~~

To edit an existing cron job, complete the following steps:

#. Sign in to the |acquia-product:sfi| using an account with the
   |platform admin|_ role.
#. In the admin menu, click **Administration**, and then, under **Site
   Factory management**, click **Cron jobs** link.
#. Find the cron job that you want to edit, and then in its **Actions**
   list, click **Edit job**.
#. Modify the values for the cron job to meet your needs, and then click
   **Continue**.

The Cron jobs page displays your cron job with its new, revised values.

Deleting cron jobs
~~~~~~~~~~~~~~~~~~

To delete a cron job value, complete the following steps:

#. Sign in to the |acquia-product:sfi| using an account with the
   |platform admin|_ role.
#. In the admin menu, click **Administration**, and then, under **Site
   Factory management**, click **Cron jobs**.
#. Find the cron job that you want to delete, and then in its
   **Actions** list, click **Delete job**.
#. To confirm the deletion of the cron job, click **Delete**.


Adding logging to cron jobs
---------------------------

You can add logging to an individual cron job by specifying the output,
as described in 
`Scheduled job output </acquia-cloud/manage/cron#output>`__.


Evaluating PHP in cron jobs
---------------------------

.. container:: message-status

   **ADVANCED** - Poorly-formatted custom cron jobs can cause cron jobs to fail.

You can evaluate PHP as part of executing a cron job by placing a
``php-eval`` command in the Drush field (assuming that all command-line
arguments are escaped properly). For example, the following ``php-eval``
statement tests for a non-production environment, and executes a command
if a module is installed in that environment:

.. code-block:: php

   php-eval \"if (\\\$_ENV[\"AH_SITE_ENVIRONMENT\"] != \\\"01live\\\" && module_exists(\"nprode_import\")) nprode_import_start_import();\"

|acquia-product:edg| will include the necessary ``--uri`` option and
Drush alias.

For PHP statements that are too complicated to execute in a single
``php-eval`` statement, you can use one of the following approaches to
execute your custom scripts with a cron job:

-  *Convert the commands to a PHP file*, and then execute the file using
   Drush with the ``php-script`` command, setting the ``--script-path``
   variable to the full path for your script.
-  *Convert your command into smaller individual commands,* creating
   cron jobs to run each command in sequence. Before attempting this
   approach, `contact Acquia Support </support#contact>`__ with details
   about your proposed cron jobs to determine if your environment
   supports enough concurrency for this approach to be successful.

.. |Cron job page| image:: https://cdn3.webdamdb.com/1280_wfhPuljw109.png?1526475463
   :width: 749px
   :height: 242px
.. |Create a cron job| image:: https://cdn2.webdamdb.com/1280_cKH9lA7FOmx2.png?1526476122
   :width: 748px
   :height: 959px

.. |platform admin| replace:: *platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin