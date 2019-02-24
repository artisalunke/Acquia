.. include:: /common/global.rst

Node.js and |acquia-product:ac|
===============================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/node-js/*

||acquia-product:ac| logo| + |logo-nodejs-sm.png|

|acquia-product:ac| is the leading cloud platform service for
developing, delivering, and managing Drupal, Node.js, and decoupled
Drupal applications. `Node.js <https://nodejs.org/>`__ is an open source
server-side environment (*runtime*) for JavaScript network applications.
|acquia-product:ace| customers can leverage both the Acquia platform and
Node.js to create unique digital experiences that better leverage the
best in JavaScript talent.

With Node.js in |acquia-product:ac|, you have a powerful set of tools to
enhance your decoupled Drupal applications, and you can also create
standalone Node.js applications that share data with Drupal.

What do Node.js applications in |acquia-product:ac| provide?

-  Server-Side rendering of front-end templates written in
   `AngularJS <https://angularjs.org/>`__,
   `React <https://reactjs.org/>`__, and
   `Ember <https://www.emberjs.com/>`__, or other front-end frameworks
-  Create powerful, flexible proxy layers between clients and Drupal,
   for enhanced security and performance
-  Enhance your *decoupled Drupal applications* with improved speed,
   SEO, and proxying capabilities
-  WebSockets support for performant, low-overhead, two-way data
   transfer to clients
-  Run stand-alone Node.js apps for real time communications like chat
   servers, for analyzing statistics or analytics, or anything else
-  Access to thousands of Node.js modules, through
   `NPM <https://www.npmjs.com/>`__

.. _decouple:

Decoupled Drupal support
------------------------

Using a Node.js application can bring beneficial enhancements to a
`decoupled Drupal
architecture <https://dri.es/the-future-of-decoupled-drupal>`__.

|acquia-product:ac| Node.js applications can use Node.js as a standalone
product, or can use Drupal as a CMS/business layer — making Drupal your
database, content creation, and update center, while connecting Node.js
with the presentation frameworks. This leverages Node.js frameworks with
decoupled Drupal architecture, exposing Drupal’s content and
business-logic backend through APIs and using a front-end framework to
build the user interface and presentation layer. Decoupled Drupal apps
combine modern user interface responsiveness and power with Drupal’s
unique content and logic features.

Traditionally, decoupled applications are hampered by a number of
significant drawbacks, including the following:

-  *Slow initial page load* - A page skeleton must load and then
   activate the front-end components to fetch content and render it,
   causing a perceived slow first-page load time.
-  *SEO unfriendly* - If page content is fetched and assembled in the
   browser, it is not available to search engines and other bots. Rich
   link previews like Facebook, LinkedIn, and so on, may not work.
-  *Security concerns* - Your Drupal API is exposed to the public
   internet, which means you may want to allow connections only from
   whitelisted addresses.

Node.js can help you address these issues by using server side rendering
to deliver an initial page straight to the browser, both decreasing
perceived load time and increasing readability by search engines.
Wrapping your Drupal APIs in Node.js means that they are exposed only to
Node.js, and not the world.

.. _start:

Getting started with Node.js applications
-----------------------------------------

Node.js application can be added to |acquia-product:ace| subscriptions
for an additional cost. Contact your account manager to learn about
adding Node.js to your subscription. For more information about Node.js
applications and environments in |acquia-product:ac|, see our `Getting
Started guide </acquia-cloud/node-js/start>`__.

.. ||acquia-product:ac| logo| image:: https://cdn4.webdamdb.com/1280_UxdMWKSngRN0.png?-62169955200
   :class: no-sb
.. |logo-nodejs-sm.png| image:: https://cdn3.webdamdb.com/1280_U6fI2wMc4E31.png?-62169955200
   :class: no-sb
   :width: 150px
   :height: 98px
