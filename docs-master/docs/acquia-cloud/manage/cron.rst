.. include:: /common/global.rst

Using scheduled jobs to maintain your application
=================================================

To help your application to run more efficiently, you should conduct
regular website maintenance. You can automate maintenance tasks or jobs
to run at scheduled intervals using the **Scheduled Jobs** page in the
|acquia-product:ui|.

.. admonition::  Note for |acquia-product:edg| subscribers

   For information about cron and scheduling tasks on |acquia-product:edg|,
   see `Managing cron tasks using the management
   console </site-factory/manage/tasks/factory>`__.

Scheduled jobs are specific to the environment that they are created in.
While you cannot create a job that executes a command across multiple
environments based on the same schedule, you can create a job for each
environment, with each of these jobs using the same command line and
schedule.

You should use the **Scheduled Jobs** page for scheduled jobs, rather
than the default Drupal cron or any of the contributed cron modules,
such as `Elysia Cron <http://drupal.org/project/elysia_cron>`__ or
`Ultimate Cron <http://drupal.org/project/ultimate_cron>`__. Compared to
other cron solutions, using the **Scheduled Jobs** page is more reliable
and provides extensive and integrated logging for |acquia-product:ac|
applications.

.. _drupal:

Disabling Drupal cron
---------------------

By default, Drupal cron (also known as *poor man's cron*) is enabled for
websites. However, Acquia recommends that you disable Drupal cron and
instead rely on |acquia-product:ac| for running scheduled jobs. Using
|acquia-product:ac| for scheduled jobs ensures that cron jobs are run on
the schedule that you specify, while default Drupal cron is instead
triggered by application activity and only when the application is
visited. Disabling Drupal cron both improves reliability and avoids the
performance reduction on page requests.

To disable Drupal cron, complete the following steps:

#. Sign in to your Drupal website as an administrator.
#. Go to **Configuration > System > Cron**
   (``http://[site_URL]/admin/config/system/cron``).
#. In the **Run cron every** list, click **Never**.
#. Click **Save configuration**.

.. _creating:

Creating scheduled jobs
-----------------------

.. admonition:: Dedicated cron servers on |acquia-product:ace|

  Some |acquia-product:ace| subscriptions have a dedicated cron server
  because of the particular performance needs of their applications. To
  set up a scheduled job on a dedicated cron server, `contact Acquia
  Support </support#contact>`__.

To create a new cron job for an environment, complete the following
steps:

#. `Sign in <https://cloud.acquia.com/>`__ to the |acquia-product:ui|.
#. Select an application and an environment.
#. Click **Scheduled Jobs**.
#. Click **Add Job** to add a scheduled job.

   |Add a scheduled job|

#. In the **Create a new scheduled job on [env]** dialog, enter a
   descriptive name for the job in the **Job name** field.
#. | In the **Command** field, enter the command that you want to have
     |acquia-product:ac| regularly run for the environment. You can
     enter any commands that are allowed from an SSH connection to the
     environment. A command cannot be longer than 255 characters. If you
     need to execute a command longer than that, you should incorporate
     it into a `shell script <#shell>`__ that you run as a scheduled
     job.

   .. note::  

      Remember that ``%`` is a special character in cron commands and if
      your command uses it, you must use a backslash (``\``) to escape it.
      For example: ``your_log_file_$(date +\%F).log``.

   | For some common cron examples that you can use in this field, see
     the `Using cron command examples <#example>`__ section on this
     page.
   | You should test commands using SSH in your |acquia-product:ac|
     environment to make sure they work before adding them as automated
     cron commands.

   |Enter information about the scheduled job|

#. Select how often you want to run the command from the menus in the
   **Command frequency** section:

   -  Every minute
   -  Every hour, at a number of minutes past the hour
   -  Every day, at a certain time
   -  Every week, at a certain day of the week and time of day
   -  Every month, at a certain day of the month and time of day
   -  Every year, at a certain month, day of the month, and time of day

   | All times are UTC.
   | As an alternative, you can enter the cron frequency as a string.
     For more information, see `Cron time string
     format <%5Bacquia-product:kb%5Darticles/cron-time-string-format>`__.

   .. note::  

      Running cron too frequently can affect performance.

#. Click **Add**.

After you create a new job, |acquia-product:ac| displays the job in the
list of scheduled jobs for the environment in which it was created.

.. _output:

Scheduled job output
~~~~~~~~~~~~~~~~~~~~

When a scheduled job runs, and the output is not redirected to
``stdout``, the cron user sends an email to the application user on the
same server. This email is saved in ``/var/mail``.

.. important:: 

  If the messages are never picked up or cleared, this eventually fills
  the disk, which can cause serious problems, including possibly bringing
  your application down.

To avoid issues, scheduled jobs should always include a logging
statement. For example, you could use the following statement, replacing
``[site]`` with your environment name, ``[env]`` with the environment,
and ``[site_URL]`` with the base URL to the website you want to execute
cron on:

.. code-block:: none

   drush @[site].[env] -dv -l http://[site_URL] cron &>> /var/log/sites/${AH_SITE_NAME}/logs/$(hostname -s)/drush-cron.log

In this example,
``&>> /var/log/sites/${AH_SITE_NAME}/logs/$(hostname -s)/drush-cron.log``
logs the cron output to a ``drush-cron.log`` file in the server's logs
directory, where it will be rotated along with the other logs in that
directory. The log file will be rotated only if it is named
``drush-cron.log``. For more information, see `About |acquia-product:ac|
logging </acquia-cloud/monitor/logs>`__.

To improve usability, you can also add a timestamp to the log messages,
replacing ``[site]`` with your environment name, ``[env]`` with the
environment, and ``[site_URL]`` with the base URL to the website you
want to execute cron on:

.. code-block:: none

   drush @[site].[env] -dv -l http://[site_URL] cron 2>&1 | awk '{print "["strftime("\%Y-\%m-\%d \%H:\%M:\%S \%Z")"] "$0}' &>> /var/log/sites/${AH_SITE_NAME}/logs/$(hostname -s)/drush-cron.log

.. _managing:

Managing scheduled jobs
-----------------------

Each job that you create on the **Scheduled Jobs** page has links to
help you manage the job, which allow you to do the following:

-  **Disable** – Stops the scheduled job from running until you click
   **Enable**. Disabled jobs move to the **Disabled** list that follows
   the **Enabled** list.
-  **Edit** – Opens a window that allows you to change the attributes of
   the scheduled job. After you make your changes, click **Edit**.
-  **Remove** – Opens a window that deletes the scheduled job when you
   click **Remove**. If you remove a scheduled job, you cannot recover
   it, and you must manually recreate it to restore the job.

.. note::  

   You cannot edit or remove administrative jobs that you did not create
   for your environments, including automatic backups.

.. _memory:

Cron and memory limits
~~~~~~~~~~~~~~~~~~~~~~

Two approaches in using drush cron are to `use the |acquia-product:ac|
wrapper script for drush cron <#wrapper>`__ or to `execute drush cron
directly <#direct>`__. These approaches have different memory limits.
When you use the Acquia cron wrapper, the cron job uses the `PHP memory
limit </acquia-cloud/manage/php#php-mem>`__ for your environment (by
default, 128MB). When you use cron directly, it uses the command line
process memory limit, which is 512MB. If you find that your cron jobs
fail to complete, try defining them to use drush cron directly to take
advantage of this higher memory limit. For related information, see
`Debugging cron <%5Bacquia-product:kb%5Darticles/debugging-cron>`__.

.. _example:

Cron command examples
---------------------

Use the following examples as you create scheduled jobs for your
application's environments.

.. _drush-cron:

Using drush cron
~~~~~~~~~~~~~~~~

To use drush cron for enhanced cron performance, select from the
following methods:

-  `Use the Acquia Cloud wrapper script for drush
   cron <#wrapper>`__
-  `Execute drush cron directly <#direct>`__

In each of these examples:

-  ``[site]`` is the name of your application on |acquia-product:ac|.
-  ``[env]`` is your environment (usually one of ``dev``, ``test``, or
   ``prod``).
-  ``[site_URL]`` is your environment's URL (as listed on the **Cloud >
   Domains** page). If you are using Drupal multisite, your cron jobs
   are specific to each website in the multisite installation. Use the
   URL of the website in the installation that you wish to target.

.. _wrapper:

Use the Acquia Cloud wrapper script for drush cron
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use a cron command like this:

.. code-block:: bash

   /usr/local/bin/cron-wrapper.sh [site].[env] http://[site_URL]

Note that you do not need to append a ``cron_key`` to the website URL.
The output of drush cron is logged to a file with a name like
``/var/log/sites/[site].[env]/logs/[server]/drush-cron.log``. For
example, if your site name was ``example``, the log file for the prod
environment might be named
``/var/log/sites/example.prod/logs/web-9876/drush-cron.log``.

.. _direct:

Execute drush cron directly
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

   drush @[site].[env] -dv -l http://[site_URL] cron &>> /var/log/sites/${AH_SITE_NAME}/logs/$(hostname -s)/drush-cron.log


In this example,
``&>> /var/log/sites/${AH_SITE_NAME}/logs/$(hostname -s)/drush-cron.log``
logs the cron output to a ``drush-cron.log`` file in the server's logs
directory. As already noted, cron jobs should always include a logging
statement, as in this example.

For instances where you want a single hook, you can also execute a
specific cron hook directly. The command structure will vary based on
your Drupal version and module. For example:

.. code-block:: none

   drush -v ev "mymodule_cron();"  &>> /var/log/sites/${AH_SITE_NAME}/logs/$(hostname -s)/drush-cron.log

The previous command will log output to the standard log files, ensuring
that log rotation and maintenance continues.

.. _shell:

Executing a shell script
~~~~~~~~~~~~~~~~~~~~~~~~

You can create scheduled jobs to execute shell scripts that you have
written.

For this example we will assume that you have added
``scripts/my-script.sh`` to your repository.

.. code-block:: none

   /var/www/html/[site].[env]/scripts/my-script.sh

where ``[site].[env]`` is your site name and environment.

.. note::  

   We highly recommend that you add your shell scripts to your source code
   repository. We also recommend adding a ``library`` or ``scripts`` folder
   to your repository in the same directory as ``acquia-utils`` and
   |docroot|_.

.. |docroot| replace:: ``[docroot]``
.. _docroot: /articles/docroot-definition

.. _related:

Related topic
-------------

-  `Debugging cron <%5Bacquia-product:kb%5Darticles/debugging-cron>`__

.. |Add a scheduled job| image:: https://cdn3.webdamdb.com/1280_IUpvl7t7J5N9.png?1526475577

.. |Enter information about the scheduled job| image:: https://cdn4.webdamdb.com/1280_IWyVPF1UJFA5.png?1526475958
