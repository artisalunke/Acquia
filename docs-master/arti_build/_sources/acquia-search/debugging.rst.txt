.. include:: /common/global.rst

Debugging |acquia-product:as|
=============================

Use the following steps when you troubleshoot issues with
|acquia-product:as|:

#. Try connecting from your local install using the subscription's keys.
   You'll probably have to disable and reenable all of the search
   modules to regenerate the salt variables. This step can determine if
   the issue is with the website or the search subscription.
#. Examine the version of the `Apache Solr Search
   Integration <https://www.drupal.org/project/apachesolr>`__ module.
#. If indexing appears to run fine but the results are sparse, examine
   ``/admin/settings/apachesolr/query-fields`` to ensure that no major
   fields are set to **Omit**. Also, scroll to the bottom of
   ``/admin/settings/apachesolr/content-bias`` and verify which content
   types are excluded from indexing.
#. Find the last node that was successfully indexed. To do this,
   complete the following steps:

   a. Run the following command:

      ``drush -vd search-index``

   b. At some point, you'll start seeing notices about what nids failed
      to index. Run the following command and note the limit:

      ``drush vget apachesolr_cron_limit``

   c. Divide the value returned by the previous command by 2, and then
      use the value with the following command:

      ``drush vset apachesolr_cron_limit [value]``

      For example, if you have 100 results, run the following command:

      ``drush vset apachesolr_cron_limit 50``

   d. Repeat the process, halving the limit each time until you get to 1
      returned value.

   At this point, you'll know which node is causing problems.

   Another technique to find the last successfully indexed node is to
   use the following command:

   ``drush vget apachesolr_index_last``

   Use the following command for Drupal 7:

   ``drush php-eval 'module_load_include("inc", "apachesolr", "apachesolr.index"); $rows = apachesolr_index_get_entities_to_index(apachesolr_default_environment(), "node", 1); foreach ($rows as $row) { print_r($row); }'``

   That reported node is probably where the indexing problem is located.

.. _drush:

Drush commands with Apache Solr Search Integration
--------------------------------------------------

The `Apache Solr Search
Integration <https://www.drupal.org/project/apachesolr>`__ module
includes a set of Drush commands that you can use to work with your
search environments. The following list includes several useful
commands:

+-----------------------------------+-----------------------------------+
| Command                           | Description                       |
+===================================+===================================+
| ``solr-delete-index``             | Deletes the content from the      |
|                                   | index (can accept content types   |
|                                   | as parameters)                    |
+-----------------------------------+-----------------------------------+
| ``solr-get-env-id``               | Get the default Apache Solr       |
|                                   | environment ID, or all            |
|                                   | environment IDs and names         |
+-----------------------------------+-----------------------------------+
| ``solr-get-env-name``             | Get the Apache Solr environment   |
|                                   | name                              |
+-----------------------------------+-----------------------------------+
| ``solr-get-env-url``              | Get the Apache Solr environment   |
|                                   | URL                               |
+-----------------------------------+-----------------------------------+
| ``solr-index``                    | Re-indexes the content marked for |
|                                   | re-indexing                       |
+-----------------------------------+-----------------------------------+
| ``solr-mark-all``                 | Marks content for re-indexing     |
|                                   | (can accept content types as      |
|                                   | parameters)                       |
+-----------------------------------+-----------------------------------+
| ``solr-search``                   | Search the website for keywords   |
|                                   | using Apache Solr                 |
+-----------------------------------+-----------------------------------+
| ``solr-set-env-url``              | Set the URL for an Apache Solr    |
|                                   | environment                       |
+-----------------------------------+-----------------------------------+
| ``solr-variable-delete``          | Delete an Apache Solr environment |
| (``solr-vdel``)                   | variable                          |
+-----------------------------------+-----------------------------------+
| ``solr-variable-get``             | Get a list of Apache Solr         |
| (``solr-vget``)                   | environment variable names and    |
|                                   | values                            |
+-----------------------------------+-----------------------------------+
| ``solr-variable-set``             | Set an Apache Solr environment    |
| (``solr-vset``)                   | variable                          |
+-----------------------------------+-----------------------------------+
| ``solr-set-derived-key``          | Sets an environment to be active  |
|                                   | for |acquia-product:as| using a   |
|                                   | specific derived key — you should |
|                                   | use your Acquia Identifier and    |
|                                   | Network Key to set this value     |
|                                   | (you can find those values on the |
|                                   | Acquia Network Subscription page, |
|                                   | under **Acquia Network keys**)    |
+-----------------------------------+-----------------------------------+

For additional information about these commands, run ``drush help`` from
the command line of your
`docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__ where
|acquia-product:as| is installed.
