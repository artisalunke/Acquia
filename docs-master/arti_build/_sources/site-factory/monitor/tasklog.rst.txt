.. include:: /common/global.rst

Task logs in |acquia-product:edg|
=================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/monitor/tasklog/*

Task logs, also known as *Work Pool* logs or *Work In Progress* (wip)
logs, are detailed records of all of the actions that your Factory is
performing. These include, but are not limited to, background tasks for
website management and domain management, and tasks initiated by users
(such as code deploys and website installations).

Tasks are assigned to groups, enabling you to both view all tasks of a
particular type and identify recurring problems.

|acquia-product:edg| offers several levels of task log retention, which
you can configure by using the `Task log
settings </site-factory/monitor/tasklog/settings>`__ webpage.

Accessing task logs in |acquia-product:edg|
-------------------------------------------

To access an overview of task logs, complete the following steps:

#. Sign in to the |acquia-product:edg| interface.
#. In the admin menu, click **Administration**.
#. In the **Logs** section, click the **Task log** link.

The **At a glance** section provides the following information about the
website update process:

|Task log at a glance|

-  **Not Started** - Number of tasks currently queued
-  **In Progress** - Number of tasks currently in progress or waiting to
   complete
-  **Error** - Number of tasks that did not complete due to an error —
   click the number to view a detailed list of errors
-  **Warning** - Number of tasks that completed with warnings — click
   the number to view a detailed list of warnings
-  **Completed** - Number of tasks that completed with no issues

Task groups
-----------

To help you identify patterns or recurring issues with your
subscription, tasks are assigned to groups. Although groups usually
contain multiple tasks of a specific type, occasionally tasks may be
related by how they are called, rather than the function that they
perform. For example, the tasks in the ``DrushCommand`` group can
contain cache-rebuilding tasks due to the tasks being executed by Drush.

When you `view task logs in |acquia-product:edg| <#access>`__, you can
filter to a single group of tasks by clicking **Group** in the **At a
Glance** section, and then selecting the group of tasks that you want to
view.

|Select a group to view it|

To clear your filter selection and view all tasks, click **Reset**.

Viewing detailed information about a task
-----------------------------------------

To view more details about a task, complete the following steps:

#. `Go to the Task log webpage <#access>`__, and then identify the task
   you want to examine in more detail.
#. To display statistics about this task, click the **Information** icon
   next to the start time of the task to display statistics about this
   task.

   |Task statistics|

   The task's statistics include the following values:

   -  **ID** - A unique identifier for this task.
   -  **Object ID** - A link to all lines in the log file for this task.
   -  **Parent** - If spawned by another task, the parent task's *Object
      ID*.
   -  **Group Name** - The group to which this task belongs, used with
      *Concurrency* to protect resources.
   -  **Added** - A UNIX timestamp showing when this task was created.
   -  **Wake** - If this task may not proceed at this time, a UNIX
      timestamp indicating when this task may resume.
   -  **Taken** - A lock that indicates if the task is currently being
      processed.
   -  **Completed** - A UNIX timestamp showing when this task completed.
      This item is blank if the task is still in progress.
   -  **Priority** - The numerical importance of this task, between
      ``1`` and ``3``, with smaller numbers having higher priority. The
      default value is ``2``. *Internal use only.*
   -  **Lease** - The number of seconds this task is expected to take.
      If exceeded, the task may be restarted. Defaults to 180.
   -  **Max run-time** - The number of seconds this task will be locked,
      with *Taken*.
   -  **Concurrency** - The number of tasks from this group that may be
      executed at the same time.

   Note

   When `contacting Acquia Support </support#contact>`__ about a task,
   be sure to include the **ID** or the **Object ID**.

#. To view detailed logs for a task, click its **Actions** menu, and
   then click **View Logs**.

.. _pause:

Pausing or terminating tasks
----------------------------

If necessary, you can pause or terminate tasks to help you reconcile or
troubleshoot issues. To pause or terminate a task from the
|acquia-product:edg| interface, complete the following steps:

#. `Go to the Task log settings webpage <#access>`__.
#. In the **At a Glance** section, click the **In Progress** link.

   |In Progress link|

#. Identify the task that you want to pause or terminate.
#. Click the task's **Actions** menu, and then click either **Pause** or
   **Terminate**, as needed.

   |Actions select box options|

#. In the confirmation window that appears, click **Ok**.

Important

Terminating a task can cause unpredictable results up to and including
data loss. `Contact Acquia Support </support#contact>`__ if you need
assistance.

.. _restart:

Restarting tasks
----------------

If a task failure was due to a potentially temporary issue, failed tasks
may provide a **Restart** option. Restarting a task will repeat the
actions performed in the original task.

Important

Restarting a failed task may cause unpredictable results, up to and
including data loss. `Contact Acquia Support </support#contact>`__ if
you need assistance.

To restart a task from the |acquia-product:edg| interface, complete the
following steps:

#. `Go to the Task log settings webpage <#access>`__.
#. In the **At a Glance** section, click the **In Progress** link.

   |In Progress link|

#. Identify the task that you want to restart.
#. | Click the task's **Actions** menu, and then click **Unpause**:

   |Unpause a task|

#. In the confirmation window that appears, click **Ok**.

.. _softpause:

Soft-paused tasks
-----------------

If tasks are in progress at the beginning of a maintenance window,
|acquia-product:edg| will *soft-pause* the tasks until the maintenance
work is complete, allowing current tasks to complete without allowing
additional tasks to start until the soft-pause is removed. When tasks
are soft-paused, a message will be displayed at the top of the webpage
when signing in to the |acquia-product:sfi|, such as the following:

``The following classes are currently soft paused: Acquia\SfBackup\SiteArchiveD8, Acquia\SfBackup\SiteArchiveV2, Acquia\SfBackup\SiteArchiveV2D8, Acquia\SfBackup\SiteRestoreD8, Acquia\SfSiteCollection\SiteGuardSite, Acquia\SfSiteCollection\SiteGuardSiteCollection, Acquia\SfSite\DomainModifyV2, Acquia\SfSite\SiteDuplicateD8, Acquia\SfSite\SiteInstallD8.``

Soft-paused tasks will be resumed after maintenance is complete. For
more information about a soft-paused task, or if you need assistance in
restarting a soft-paused task, `contact Acquia
Support </support#contact>`__.

.. |Task log at a glance| image:: https://cdn4.webdamdb.com/1280_s03CEn5z9961.png?1526475626
   :width: 600px
   :height: 187px
.. |Select a group to view it| image:: https://cdn4.webdamdb.com/1280_2ePJvSopo6D5.png?1526475610
   :width: 559px
   :height: 170px
.. |Task statistics| image:: https://cdn4.webdamdb.com/1280_UeDl2aXAY95.png?1526475789
   :width: 903px
   :height: 191px
.. |In Progress link| image:: https://cdn3.webdamdb.com/1280_AAcNxfc0qKF8.png?1526475552
   :width: 553px
   :height: 358px
.. |Actions select box options| image:: https://cdn2.webdamdb.com/1280_OsvJzIhzB31.png?1526476096
   :width: 268px
   :height: 239px
.. |Unpause a task| image:: https://cdn3.webdamdb.com/1280_cHMDUOPTCgA0.png?1526476128
   :width: 274px
   :height: 221px
