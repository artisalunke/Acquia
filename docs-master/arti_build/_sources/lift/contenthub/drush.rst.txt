.. include:: /common/global.rst

Using Drush with |acquia-product:ch| for Drupal 7
==================================================

|acquia-product:ch| includes several `Drush <https://www.drupal.org/project/drush>`__ commands for both `normal <#cmd>`__ product use and for more `advanced <#dev>`__ administration. You can use the commands to administer your content from the command line.

.. note::

   For more information about Drush, see `Intro to Drush <%5Bacquia-product:kb%5Darticles/drush-intro>`__.

Drush commands
--------------

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Command
     - Description
   * - content-hub-connect_
     - Connect to |acquia-product:ch|
   * - content-hub-compare_
     - Compares the version of an entity from a local source and a remote source and prints the differences
   * - content-hub-delete_
     - Deletes a single entity from the |acquia-product:ch|
   * - content-hub-diagnostic_
     - Perform diagnostic checks on the |acquia-product:ch|
   * - content-hub-disconnect_
     - Disconnect the client from the |acquia-product:ch|
   * - content-hub-export_
     - Export a local entity to the |acquia-product:ch|
   * - content-hub-export-block_
     - Export a core custom block to |acquia-product:ch|
   * - content-hub-list_
     - List content entities that exist in the |acquia-product:ch|
   * - content-hub-local_
     - Prints an entity (in CDF format) from a local source (a Drupal website)
   * - content-hub-purge_
     - Deletes all entities from the |acquia-product:ch| (deprecated in |acquia-product:ch| 1.18.0 or greater)
   * - content-hub-regenerate-secret_
     - Regenerates the shared secret used for webhook verification
   * - content-hub-remote_
     - Prints an entity (in CDF format) from a remote source (the |acquia-product:ch|)
   * - content-hub-update-secret_
     - Updates the shared secret used for webhook verification
   * - content-hub-webhook_
     - Perform a webhook management operation
   * - queue-list_
     - General Drush command that returns additional |acquia-product:ch|-related results
   * - queue-run_
     - General Drush command that accepts additional |acquia-product:ch|-related arguments


Drush commands for developers
-----------------------------

The following commands are restricted by the user's access key:

.. important:: Using these commands can remove data from |acquia-product:ch|.

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Command
     - Description
   * - content-hub-logs_
     - View historic entity logs from |acquia-product:ch|
   * - content-hub-mapping_
     - Shows Elastic Search field mappings from |acquia-product:ch|
   * - content-hub-purge_
     - Deletes all entities from the |acquia-product:ch| (available in version 1.30 or greater)
   * - content-hub-reindex_
     - Reindex all entities in |acquia-product:ch|
   * - content-hub-restore_
     - Restores the backup taken by a previous execution of the content-hub-purge command



Command details
---------------

``content-hub-connect``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connects to |acquia-product:ch|.

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| -  ``ch-connect``                 | -  ``hostname`` - The             |
| -  ``ch-c``                       |    |acquia-product:ch| hostname   |
|                                   |    to connect to                  |
|                                   | -  ``api_key`` - The API key to   |
|                                   |    connect with                   |
|                                   | -  ``secret`` - The secret key to |
|                                   |    connect with                   |
|                                   | -  ``client_name`` - The client   |
|                                   |    name to register the website   |
|                                   |    with                           |
+-----------------------------------+-----------------------------------+

``content-hub-compare``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compares the version of an entity from a local source and a remote
source and prints the differences.

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ch-comp``                       | ``entity-type``                   |
|                                   | ``entity-id`` - The UUID of the   |
|                                   | entity                            |
+-----------------------------------+-----------------------------------+

``content-hub-delete``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deletes a single entity from the |acquia-product:ch|.

+---------------+----------------------------------------+
| Alias         | Arguments                              |
+===============+========================================+
| ``ch-delete`` | ``entity-id`` - The UUID of the entity |
+---------------+----------------------------------------+

``content-hub-diagnostic``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perform certain diagnostics on the |acquia-product:ch|.

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| -  ``ch-diagnostic``              | *none*                            |
| -  ``ch-diag``                    |                                   |
+-----------------------------------+-----------------------------------+

``content-hub-disconnect``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disconnect the client from the |acquia-product:ch|.

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| -  ``ch-discon``                  | *none*                            |
| -  ``ch-disconnect``              |                                   |
+-----------------------------------+-----------------------------------+

``content-hub-export``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Export a local entity to the |acquia-product:ch|.

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| -  ``ch-ex``                      | You can pass an array of options  |
| -  ``ch-export``                  | to control the export:            |
|                                   |                                   |
|                                   | -  ``include-dependencies`` -     |
|                                   |    This option also exports       |
|                                   |    dependent entities (they are   |
|                                   |    excluded by default)           |
+-----------------------------------+-----------------------------------+

``content-hub-export-block``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Export a core custom block to the |acquia-product:ch|

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| -  ``ch-ex-block``                | ``bid`` - The block ID to export  |
| -  ``ch-export-block``            |                                   |
| -  ``ch-exb``                     |                                   |
+-----------------------------------+-----------------------------------+

``content-hub-logs``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(*Developer only*) - View historic entity logs from |acquia-product:ch|

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Alias
     - Arguments
   * - ``ach-logs``
     - This command takes the following arguments:

       - ``api`` - The |acquia-product:ch| API key
       - ``secret`` - Your secret key

       You can pass an array of options to control the output:

       - ``query`` - The Elastic Search query to search for in the logs; example: ``{"query": {"match_all": {}}}``
       - ``size`` - The number of log entries to be listed
       - ``from`` - The offset to start isting the log entries — used for pagination


``content-hub-list``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List content entities that exist in the |acquia-product:ch|.

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ch-list``                       | You can pass an array of options  |
|                                   | to control the output:            |
|                                   |                                   |
|                                   | -  ``limit`` - The number of      |
|                                   |    entities to be listed          |
|                                   | -  ``start`` - The offset to      |
|                                   |    start listing the entities     |
|                                   |    (useful for pagination)        |
|                                   | -  ``origin`` - The client's      |
|                                   |    origin UUID                    |
|                                   | -  ``language`` - Filter entities |
|                                   |    by language — for example,     |
|                                   |    ``en``                         |
|                                   | -  ``attributes`` - The           |
|                                   |    attributes to display for all  |
|                                   |    listed entities                |
|                                   | -  ``type`` - The entity types to |
|                                   |    include                        |
|                                   | -  ``filters`` - Key=value pairs  |
|                                   |    of conditions by which to      |
|                                   |    filter the output, comma       |
|                                   |    separated — for example,       |
|                                   |    ``title=New*, status=1``       |
+-----------------------------------+-----------------------------------+

``content-hub-local``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prints an entity (in CDF format) from a local source (a Drupal website)

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Alias
     - Arguments
   * - ``ach-lo``
     - 
       * ``entity-type``
       * ``entity-id`` - The UUID of the entity


``content-hub-mapping``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shows Elastic Search field mappings for |acquia-product:ch|.

+----------------+-----------+
| Alias          | Arguments |
+================+===========+
| ``ch-mapping`` | *none*    |
+----------------+-----------+

``content-hub-purge``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(*Developer only*) - Deletes all entities from the
|acquia-product:ch|. This is disabled in |acquia-product:ch| 1.18.0
to 8.x-1.12.

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ch-purge``                      | -  ``api`` - The                  |
|                                   |    |acquia-product:ch| API key    |
|                                   | -  ``secret`` - Your secret key   |
+-----------------------------------+-----------------------------------+

``content-hub-regenerate-secret``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Regenerates the shared secret used for webhook verification.

+---------------+-----------+
| Alias         | Arguments |
+===============+===========+
| ``ch-regsec`` | *none*    |
+---------------+-----------+

``content-hub-remote``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prints an entity (in CDF format) from a remote source (the
|acquia-product:ch|).

+-----------+----------------------------------------+
| Alias     | Arguments                              |
+===========+========================================+
| ``ch-re`` | ``entity-id`` - The UUID of the entity |
+-----------+----------------------------------------+

``content-hub-reindex``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(*Developer only*) - Reindexes all entities in |acquia-product:ch|

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ch-reindex``                    | -  ``api`` - The                  |
|                                   |    |acquia-product:ch| API key    |
|                                   | -  ``secret`` - Your secret key   |
+-----------------------------------+-----------------------------------+

``content-hub-restore``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(*Developer only*) - Restores the backup taken by a previous
execution of the ``purge`` command.

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| ``ch-restore``                    | -  ``api`` - The                  |
|                                   |    |acquia-product:ch| API key    |
|                                   | -  ``secret`` - Your secret key   |
+-----------------------------------+-----------------------------------+

``content-hub-update-secret``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Updates the shared secret used for webhook verification.

+--------------+-----------+
| Alias        | Arguments |
+==============+===========+
| ``ch-upsec`` | *none*    |
+--------------+-----------+

``content-hub-webhook``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perform a webhook management operation.

+-----------------------------------+-----------------------------------+
| Alias                             | Arguments                         |
+===================================+===================================+
| -  ``ch-webhook``                 | ``op`` - The operation to use:    |
| -  ``ch-w``                       | ``register``, ``unregister``, or  |
|                                   | ``list`` — requires the           |
|                                   | ``webhook_url`` as an option      |
+-----------------------------------+-----------------------------------+

``queue-list``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This command is not specific to |acquia-product:ch|, but will return
additional results with it. See `drush
queue-list <https://drushcommands.com/drush-8x/core/queue-list/>`__.

+-----------------------------------+-----------------------------------+
| Result                            | Description                       |
+===================================+===================================+
| ``content_hub_webhook_queue``     | The number of items in the        |
|                                   | |acquia-product:ch| webhook queue |
+-----------------------------------+-----------------------------------+

``queue-run``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This command is not specific to |acquia-product:ch|. See `drush
queue-run <https://drushcommands.com/drush-8x/core/queue-run/>`__.

+-----------------------------------+-----------------------------------+
| Argument                          | Description                       |
+===================================+===================================+
| ``content_hub_webhook_queue``     | Processes the remaining           |
|                                   | |acquia-product:ch| webhook queue |
+-----------------------------------+-----------------------------------+
