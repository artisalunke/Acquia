.. include:: /common/global.rst

Configuring task log settings
=============================

|acquia-product:edg| offers several levels of task log retention, which
are `configured <#configure>`__ in the Task log settings page of the
Factory interface.

.. _levels:

Logging levels and definitions
------------------------------

|acquia-product:edg| will retain the log messages for a task that match
or exceed the configured logging priority until the task completes.
Whether the task ends in failure or success determines which logs are
kept after the task ends:

-  *Failed tasks* - No logs are truncated, and logs are captured and
   kept based on the configured settings.
-  *Successful tasks* - Some logs are captured and kept, based on the
   configured settings.

The following logging levels are listed from most serious (``FATAL``) to
least serious (``TRACE``):

+-----------------------+-----------------------+-----------------------+
| Name                  | Description           | Priority              |
+=======================+=======================+=======================+
| ``FATAL``             | An unrecoverable      | 1 (most)              |
|                       | error                 |                       |
+-----------------------+-----------------------+-----------------------+
| ``ERROR``             | A recoverable error — | 2                     |
|                       | it may be possible to |                       |
|                       | retry the operation   |                       |
|                       | and proceed           |                       |
+-----------------------+-----------------------+-----------------------+
| ``ALERT``             | System events that    | 3                     |
|                       | are unusual, but are  |                       |
|                       | not errors (similar   |                       |
|                       | to ``NOTICE``\ in     |                       |
|                       | PHP)                  |                       |
|                       | *Examples: A user     |                       |
|                       | pauses a task, or a   |                       |
|                       | task receives info    |                       |
|                       | from an asynchronous  |                       |
|                       | process*              |                       |
+-----------------------+-----------------------+-----------------------+
| ``FLOW``              | Changes in state made | 4                     |
|                       | as part of normal     |                       |
|                       | operations            |                       |
+-----------------------+-----------------------+-----------------------+
| ``WARN``              | A non-essential part  | 5                     |
|                       | of a task did not     |                       |
|                       | complete as expected, |                       |
|                       | although the overall  |                       |
|                       | task succeeded        |                       |
|                       | *Example: Errors in   |                       |
|                       | user-created hooks*   |                       |
+-----------------------+-----------------------+-----------------------+
| ``INFO``              | Actions taken as part | 6                     |
|                       | of normal operations  |                       |
+-----------------------+-----------------------+-----------------------+
| ``DEBUG``             | Diagnostic            | 7                     |
|                       | information           |                       |
|                       | potentially useful to |                       |
|                       | both website          |                       |
|                       | maintainers and       |                       |
|                       | Acquia Support        |                       |
+-----------------------+-----------------------+-----------------------+
| ``TRACE``             | More verbose          | 8 (least)             |
|                       | diagnostic            |                       |
|                       | information,          |                       |
|                       | generally useful only |                       |
|                       | to Acquia developers  |                       |
+-----------------------+-----------------------+-----------------------+

When determining which logs to keep, |acquia-product:edg| will keep the
logs for the selected level and for all levels greater than the
selection. For example, selecting the ``ALERT`` level for logging will
keep all log messages with a status of ``ALERT``, ``ERROR``, and
``FATAL``.

For more information about the types of logging available and how to
access them, see `Logging in
|acquia-product:edg| </site-factory/manage/logs>`__.

.. _configure:

Configuring log message retention
---------------------------------

To configure how |acquia-product:edg| retains generated log messages,
complete the following steps:

#. Sign in to the Factory interface with either the *`release
   engineer </site-factory/users/admin/release-engineer>`__* or
   *`developer </site-factory/users/admin/developer>`__* role.
#. In the admin menu, click **Administration**, and then click the
   **Task log settings** link.
#. Use the following lists to configure the log filtering for your
   |acquia-product:edg|-hosted websites, based on the available `logging
   levels <#levels>`__:

   -  **Logging level for successful tasks** - The default threshold of
      log retention after a task completes successfully — *Recommended
      value: ``WARN``*
   -  **Logging level for completed tasks** - The default threshold of
      log retention, with log messages with a status less than the
      configured threshold not being saved — *Recommended value:
      ``INFO`` (unless you are investigating problems with your
      website)*

#. Click **Save configuration**.
