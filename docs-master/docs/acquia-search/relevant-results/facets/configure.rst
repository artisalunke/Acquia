.. include:: /common/global.rst

Configuring search facets
=========================

Search facets enable users to refine or sort their search result set.
Users can begin with a general search and narrow down the result set as
they understand better what content is available on your site. To learn
more about search facets, see the following:

-  `Filtering search results with facets </acquia-search/facets>`__
-  `How search facets work </acquia-search/facets/examples>`__

To enable search facets, install and enable the appropriate Drupal
module.

-  Drupal 7: `Facet API <https://www.drupal.org/project/facetapi>`__
-  Drupal 8: `Facets <https://www.drupal.org/project/facets>`__

If you are an administrators with search settings permissions, you can
go to the **Apache Solr Search > Settings > Facets** tab and enable the
facets you want to use in your search pages. The facets displayed on the
**Facets** tab depend on which bundles and entities you have enabled on
your site, as well as the other search-related modules you have
installed. For more information, read `Modules for
|acquia-product:as| </acquia-search/modules>`__.

|Enable search facets|

Facet configuration operations
------------------------------

For each enabled facet, you can select the following operations:

-  `Configure display <#display>`__
-  `Configure dependencies <#dependencies>`__
-  `Configure filters <#filters>`__
-  `Export configuration <#export>`__

Configure display
-----------------

The Configure display page enables you to configure how each facet is
displayed in the search results. On it, you can configure the following:

-  `Display widget <#widget>`__
-  `Soft limit <#soft>`__
-  `Empty facet behavior <#empty>`__
-  `Sort rules <#sort>`__
-  `Global settings <#global>`__

|Configure facet display settings|

Display widget
~~~~~~~~~~~~~~

The Facet API includes two basic display widgets: links and links with
checkboxes. Other modules (such as `Facetapi
Slider <https://www.drupal.org/project/facetapi_slider>`__) can provide
other display widgets.

Soft limit
~~~~~~~~~~

The soft limit limits the number of facets that are displayed initially.
Additional facets are displayed after the **Show more** link is clicked.

Empty facet behavior
~~~~~~~~~~~~~~~~~~~~

This controls the action to take when a facet has no items. The default
is to not display the facet if the search returned no items for that
facet. You can select **Display text**, and then enter and format the
text to display for an empty facet.

Sort rules
~~~~~~~~~~

You can configure how to sort the facets. Each sort rule can be in
ascending or descending order, and can have a weight assigned that
determines in which order to apply the sort rules.

Global settings
~~~~~~~~~~~~~~~

The global settings for facet configuration apply to this facet across
all realms.

Hard limit
^^^^^^^^^^

Display no more than this number of items per facet.

Minimum facet count
^^^^^^^^^^^^^^^^^^^

Only display facets that are matched in at least this many documents.
The default value is ``1``; you can increase this to eliminate some
facets, even if they contain search result items.

Configure dependencies
----------------------

Dependencies are conditions that must be met in order for the facet to
be processed by the server and displayed to the user. Dependencies can
be based on either bundles or roles.

Bundle-based dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~

Using bundle-based dependencies, you can control whether or not a given
facet should be displayed based on the bundle (such as content type).

Role-based dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Using role-based dependencies, you can control whether or not a given
facet should be displayed to a user based on the user's role.

Configure filters
-----------------

The Configure filters operation lets you enable, disable, and weight
facet filters that are created using search-related contributed and
custom modules.

Export configuration
--------------------

Using the export configuration operation, you can view, copy, and paste
a PHP version of the facet’s configuration. By exporting a facet’s
configuration to code, you can use version control for the
configuration, as well as export it to other sites.

Block cache settings
--------------------

The **Apache Solr Search > Settings > Facets** tab also displays your
Block cache settings. For best performance, enable block caching, which
you can do on the **Administration > Configuration > Development >
Performance** page. For more information, see `Page and block
caching </acquia-search/recommendation#cache>`__ in `Creating content
recommendation blocks </acquia-search/recommendation>`__.

.. |Enable search facets| image:: https://cdn2.webdamdb.com/md_Qyh2t2DeClw6.png?1527793648
   :alt: Enable search facets
.. |Configure facet display settings| image:: https://cdn3.webdamdb.com/md_Y4jZN39AZJF2.png?1527793652
   :alt: Configure facet display settings
