.. include:: /common/global.rst

Viewing tasks
=============

The Task Log on the **Environments** page lists all tasks performed on
each of your environments during the last seven days. By viewing recent
completed tasks, you can diagnose which changes may have caused behavior
(good or bad) you are seeing on your website. For each task, the Task
Log displays the status, a description, and the start date and time.

|Task Log|

For any task, you can click the down arrow to see details of the task.
The details include a task ID, user ID, start and completion time,
status, and log entry.

|Task detail|

For tasks initiated in the |acquia-product:ui|, the user ID displayed is
the ID of the logged-in Acquia user. For code commits, the user ID
displayed is ``vcs.commit``. For Drush Cloud commands, the user ID
displayed is the Unix user that runs the command.

.. _complete:

Task completion status
~~~~~~~~~~~~~~~~~~~~~~

Completed tasks are assigned one of the following states:

-  **Done** – The task completed as expected
-  **Error** – A problem occurred with the task in |acquia-product:ac|
-  **Failed** – A problem occurred when using the |acquia-product:api|,
   a custom script, or other software or service

.. _older:

Viewing older tasks
-------------------

To view tasks older than the last seven days, you can use the Drush
Cloud or Cloud API commands. For example, to view tasks in your
Development environment using Drush Cloud:

#. Connect to your |acquia-product:ac| server using SSH.
#. Authenticate to the Cloud API, using ``drush ac-api-login`` with your
   Cloud API credentials. For information about how to get your Cloud
   API credentials, see `Cloud API
   authentication </acquia-cloud/api/auth>`__.

   ``drush @mysite.dev ac-api-login --username=fed987cba654 --password=123abc456def``

#. Enter a command like this:

   ``drush @mysite.dev ac-task-list``

By default, the ``ac-task-list`` command returns only the last seven
days of tasks and no more than 50 tasks. You can modify this default
behavior by using the ``limit`` or ``days`` arguments in the command.
For example:

-  Get the last 30 days of tasks:

   ``curl -s -u user:pass https://cloudapi.acquia.com/v1/sites/realm:mysite/tasks.json?days=30``

-  Get the last 200 tasks:

   ``curl -s -u user:pass https://cloudapi.acquia.com/v1/sites/realm:mysite/tasks.json?limit=200``

In any case, the command returns a maximum of 1000 tasks.

To view the details of a task, you can use the Drush ``ac-task-info``
command, which takes the ID of the task as an argument (or the
corresponding Cloud API command). For example, for details about a task
with the ID 1234567:

``drush @mysite.dev ac-task-info 1234567``

.. |Task Log| image:: https://cdn4.webdamdb.com/1280_AQNFpM8df1I9.png?1527264732
   :width: 749px
   :height: 583px
.. |Task detail| image:: https://cdn3.webdamdb.com/1280_ExD61Wdza1q7.png?1526475958
   :width: 677px
   :height: 247px
