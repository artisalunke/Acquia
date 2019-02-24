.. include:: /common/global.rst

Personalization methods
=======================

+-----------------------------------+-----------------------------------+
| Method                            | Description                       |
+===================================+===================================+
| ``customize``                     | Triggers a Decision API call to   |
|                                   | retrieve decisions, and then      |
|                                   | broadcast the customized portion  |
|                                   | of the response data to the       |
|                                   | webpage.                          |
|                                   | The function can take a           |
|                                   | configuration object as an        |
|                                   | optional argument. All result     |
|                                   | decisions of customized slots are |
|                                   | broadcasted by the JavaScript     |
|                                   | event                             |
|                                   | ``acquiaLiftContentCustomizable`` |
|                                   | .                                 |
|                                   | See |JavaScript API events|_      |
+-----------------------------------+-----------------------------------+
| ``personalize``                   | Triggers a Decision API call to   |
|                                   | run personalization for the       |
|                                   | webpage or for a list of slots on |
|                                   | the webpage. *Contained in the    |
|                                   | ``window.AcquiaLiftPublicApi``    |
|                                   | namespace.*                       |
|                                   | The function can take a           |
|                                   | configuration object as an        |
|                                   | optional argument. When not       |
|                                   | specified, the decisions are      |
|                                   | returned for all slots on the     |
|                                   | current URL.                      |
+-----------------------------------+-----------------------------------+


.. |JavaScript API events| replace:: JavaScript API events
.. _JavaScript API events: /lift/javascript/events

Examples
--------

Use the following code to personalize an entire page:

``window.AcquiaLiftPublicApi.personalize();``

To personalize a specific slot or an array of slots, use the following:

``window.AcquiaLiftPublicApi.personalize({slots: ['744bffce-66b3-4f4a-8ea9-b481a556c3f8']});``

In the previous example, ``744bffce-66b3-4f4a-8ea9-b481a556c3f8`` is an
example slot ID that you want to use. The slot ID is an auto-generated
`UUID (Universally Unique Identifier) <https://tools.ietf.org/html/rfc4122.html>`__.

To obtain the decisions of the slots from another URL, and then apply
the personalization on the current webpage, use code similar to the
following:

``window.AcquiaLiftPublicApi.personalize({url: 'http://mysite.com/another-page'});``
