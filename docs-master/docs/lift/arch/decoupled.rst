.. include:: /common/global.rst

Decoupled architecture and |acquia-product:cha|
===============================================

.. toctree::
   :hidden:
   :glob:

   /lift/arch/decoupled/*

|acquia-product:cha| supports website personalization for customers
looking to build dynamic single-page applications in traditional,
progressively-decoupled, and fully-decoupled front-ends.

When using decoupled architecture with |acquia-product:cha|, the
front-end JavaScript application needs to control both the requests to
the |acquia-product:cha| service, and the entire rendering of content
after the data is returned from the `Decision
API </lift/omni/api/file/import>`__. Your architecture should take into
consideration the following items:

-  Because the decoupled architecture does not refresh the full webpage,
   |acquia-product:cha| will not bootstrap on page loads
-  The rendered content stored in |acquia-product:ch| is not useful, as
   Drupal does not have view modes for the content items
-  Due to the lack of styled content, |acquia-product:cha| should not
   return and render content directly to the website front-end

Traditional and progressively-decoupled applications
----------------------------------------------------

In a traditional and progressively-decoupled environment, Drupal
controls all or portions of the content rendering, as indicated in the
following diagram:

|Traditional architecture diagram|

#. Drupal controls either all or portions of the content rendering, and
   JSON and HTML versions of this content are stored in
   |acquia-product:ch|.
#. A standard page load bootstraps a JavaScript request to the
   |acquia-product:cha| `Decision API </lift/omni/api/file/import>`__
   for personalized content.
#. The Decision API retrieves the personalized content from
   |acquia-product:ch|.
#. The Decision API returns the JavaScript to the front-end client to be
   rendered as HTML in the specified |acquia-product:cha| slot.

This architecture style enables |acquia-product:cha| to make decisions
and render personalized content entirely from its own workflow. After
content is stored in |acquia-product:ch|, the |acquia-product:cha|
Decision API can fetch content during the personalization process,
instead of from the website's own content storage.

Fully decoupled front-end applications
--------------------------------------

Although there are several available methods to create a decoupled
front-end website architecture, Acquia generally recommends using Drupal
as a backend content management system (CMS). Raw structured JSON
content is fetched through either a Node.js server or the Drupal API,
and then returned as JSON to be rendered by the front-end JavaScript
application, as described by the following diagram:

|Basic decoupled architecture|

In this architecture style, the content being served from Drupal is raw
data instead of rendered content. After the JSON content is consumed by
your front-end application, it must be placed into the necessary
rendered templates and then styled appropriately.

Single-page applications (SPAs)
-------------------------------

When creating a single-page decoupled application with
|acquia-product:cha| using Drupal as your backend content management
system (CMS), your content will be authored in Drupal and published and
stored in |acquia-product:ch|.

Your front-end JavaScript application should directly call the
|acquia-product:cha| service through the `JavaScript
API </lift/javascript>`__ to track visitor behavior and request
personalized content.

The Decision API will request the personalized content from
|acquia-product:ch|, and will return the metadata for personalized
content, and HTML and JSON versions of the content, through JavaScript
events for your single-page application to consume, render, and display
on your webpage as indicated in the following diagram:

|Decoupled architectures|

For information about setting up this architecture, see |singlepage|_ for more information.


.. |singlepage| replace:: Using  \ |acquia-product:cha|\  with single-page applications
.. _singlepage: /lift/decoupled/singlepage

.. |Traditional architecture diagram| image:: https://cdn2.webdamdb.com/1280_QaM7nhZ9s3R1.png?-62169955200
   :class: align-center no-sb
   :width: 550px
.. |Basic decoupled architecture| image:: https://cdn3.webdamdb.com/1280_YiuNUpdEWbj6.png?-62169955200
   :class: align-center no-sb
   :width: 300px
.. |Decoupled architectures| image:: https://cdn2.webdamdb.com/1280_oBFkiWLkZjw3.png?-62169955200
   :class: align-center no-sb
   :width: 550px
