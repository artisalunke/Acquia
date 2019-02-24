.. include:: /common/global.rst

Using taxonomy with discovery
=============================

When you import content, |acquia-product:ch| uses tags, both as filters
for import, and like other taxonomy terms native to your website (after
the content is imported).

Adding terms
------------

For information about taxonomy and how to create and use it with your
website, see the `Concept:
Taxonomy <https://www.drupal.org/docs/user_guide/en/structure-taxonomy.html>`__
user guide page on Drupal.org.

Configuring terms for import
----------------------------

You must configure |acquia-product:ch| to export tags before they can be
made available. Complete the following steps to configure tags for use
with |acquia-product:ch|:

#. Ensure that you have created a taxonomy and added tags to some of
   your content.
#. As an administrator on your website, navigate to **Configuration >
   Web services > Acquia Content Hub > Entity Configuration**.
#. In the **Taxonomy_Term** fieldset, select the check box next to the
   vocabulary that you want to make available for export.
#. Click **Save configuration**.

Using tags
----------

After a vocabulary is available for export, the **Tags** menu on the
`discovery </content-hub/discover>`__ page should have the terms from
your vocabulary that are available for import.

If no tags are available, |acquia-product:ch| will display a message
similar to the following:

``Your content does not have any tags associated with it.``
