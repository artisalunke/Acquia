.. include:: /common/global.rst

Site performance with |acquia-product:cha|
==========================================

Because variations are rendered and decisions are made in your website
visitors' browsers using JavaScript, there are no additional server
requirements to use |acquia-product:cha| (beyond the normal memory
requirements of installing three additional modules).

Also, your website's initial page load time is usually unaffected, and
the service works well both with Varnish caching and CDNs.

|acquia-product:cha| adds a single HTTP request per decision (usually a
variation set) on each page of your website that includes a personalized
element. Each HTTP request is approximately equivalent to loading an
image on the page, which in our testing takes between 40ms - 70ms for
the entire request. These requests are non-blocking, so although the
tested element won't load until that request has been made, everything
else on the page will display normally. Also, because variation
decisions are cached, when the same visitor redisplays the page, the
browser will quickly display the variation selected for them by
|acquia-product:cha|.

Contexts
--------

Adding additional contexts to your personalizations effectively adds no
additional time to the browser's decision-making process. However,
having a large number of contexts can cause personalization scenarios to
have to run for more time to ensure that meaningful results are
displayed for each of your contexts.

.. _actions:

Actions that can affect website performance
-------------------------------------------

The following actions can either improve or decrease website performance
with |acquia-product:alt|:

-  *Increase performance* - |acquia-product:alt| supports minified
   JavaScript, which can help your website load faster for website
   visitors. For more information, see `Enabling Acquia Lift Drupal on
   your website </lift/drupal/install7/enable>`__.
-  *Decrease performance* - Your website's page load times can increase
   if you add personalized blocks that contain many variations, make
   many calls to your website's database, or both.
