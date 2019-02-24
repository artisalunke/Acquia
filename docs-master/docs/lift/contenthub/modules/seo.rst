.. include:: /common/global.rst

SEO and social publishing metadata with |acquia-product:ch|
===========================================================

.. container:: message-status

   `The Metatag module is incompatible with Content Hub in Drupal 8 </content-hub/modules>`__.

If your purpose for using |acquia-product:ch| is syndicating blog or
editorial content, you’ll want to use the
`Metatag <https://www.drupal.org/project/metatag>`__ module in order to
maintain the Search Engine Optimization (SEO) of both original and
syndicated content. Metatag can help preserve canonical URL data across
the platforms.


The Metatag module
------------------

If you use |acquia-product:ch| to syndicate blog content, you’ll want
the metadata on your syndicated content to indicate the original source
(canonical URL) to preserve SEO. Installing the Metatag module on both
the publishing and subscribing websites allows metadata from the
publishing website to be transferred to the hub, and then to the
subscribing websites.

It is essential to set canonical URL in the Metatag module. This will
enable your syndicated content to maintain its original source
information.

There are options to vary deployment and Metatag module settings on
subscribing websites for more complex architectures.


Preventing evaluation of tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ch| provides the ability to blacklist tokens_ when there are
properties that you do not want submitted to the publishing hub.

.. _tokens: https://www.drupal.org/node/390482

As an administrator, complete the following steps:

#. Navigate to **Configuration > Acquia Content Hub Connector > Settings**.
#. In the **Properties List** field, enter the tokens you want to
   exclude. Each token must be on a separate line.
#. Click **Save configuration** when finished.


Social metadata with |acquia-product:ch| and the Metatag module
---------------------------------------------------------------

Users interested in good social metadata can use the Metatag module to
create more efficient workflows. Using the module allows the publishing
website to invest additional effort in social media display by editing
`Open Graph <https://developers.facebook.com/docs/sharing/opengraph>`__
and `Twitter Cards <https://dev.twitter.com/cards/overview>`__ metadata
in the publishing website, which adds value to syndicating websites.


Subscribing websites and the Metatag module
-------------------------------------------

There are options to vary deployment and Metatag module settings on
subscribing websites for more complex architectures through token
overrides.
