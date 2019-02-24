.. include:: /common/global.rst

Page Rules
==========

*Page Rules* provide powerful configuration options in |acquia-product:cf|, enabling subscribers to have granular control over how requests to their website behave for |acquia-product:cfc| and |acquia-product:cfp| solutions. You can create Page Rules that perform actions based on a requested webpage's URL, such as creating redirects, fine tuning caching behavior, or enabling and disabling certain |acquia-product:cf| services.

Acquia configures a base set of Page Rules, depending on whether the you have purchased |acquia-product:cf|, |acquia-product:cfp|, or both.

How do Page Rules work?
-----------------------

As a general rule, Page Rules should be ordered from most specific (at the beginning of the list), to least specific (at the end). You can pause Page Rules, in which case they will take no action, but are still displayed in the list and can be edited. The **Save as Draft** option will create a Page Rule that is initially paused.

When using multiple Page Rules, |acquia-product:cf| uses the following guidelines:

-  Only one Page Rule will take effect for any given visitor request.
-  Page Rules are evaluated in priority from top to bottom.

A Page Rule will take effect on a given URL pattern, matching the following format:

.. code-block:: none

   <scheme>://<hostname><:port>/<path>

The scheme and port components are both optional. If you omit the scheme, it will cover both ``http://`` and ``https://`` protocols. If the port is not specified, the Page Rule will match all ports.

URLs in Page Rules allow you to use wildcards to apply a Page Rule for multiple pages. For example, you could use ``*example.com`` to match both ``http://example.com`` and ``https://example.com``.

If you want to match every page on a domain, you will need to use ``example.com/*``, as ``example.com`` is not specific enough in this case.

Forwarding Page Rules
~~~~~~~~~~~~~~~~~~~~~

If you are using a *forwarding* Page Rule, you can map those wildcards to variables. In the forwarding URL, specify ``$1``, ``$2``, and so on to match the wildcards in the original URL (in order, from left to right).

For example, you could forward ``http://*.example.com/*`` to ``http://$2.example.com/$1.jpg``. This rule would match ``http://cloud.example.com/flare``, which would end up being forwarded to ``http://flare.example.com/cloud.jpg``.
