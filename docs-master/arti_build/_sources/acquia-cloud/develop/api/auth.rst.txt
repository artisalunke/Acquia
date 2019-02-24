.. include:: /common/global.rst

Cloud API authentication
========================

All Cloud API calls (whether in a RESTful API call or in a Drush Cloud
command) need to be authenticated in order to work. You authenticate a
call using your user name (the email address with which you sign in to
Acquia) and a private key that you can find on your Acquia Profile page.

Cloud API private keys and API tokens

|acquia-product:ac| also uses a method of API authentication using API
tokens. In this release, API tokens are used *only* to `authenticate
with the pipelines
feature </acquia-cloud/develop/pipelines/cli/install#authenticate>`__.
For all other Cloud API purposes, authenticate with the Cloud API using
the Cloud API private key described on this page.

To find your private key:

#. Sign in to the `|acquia-product:ui| <https://cloud.acquia.com>`__
   using your email address and Acquia password.
#. Click your user avatar in the upper right corner, and then click
   **Edit profile**.

   |Edit your profile|

#. On the Profile page, click **Credentials**, and then enter your
   Acquia password.

   |Profile Credentials page|

#. Under **Cloud API**, click **Show**, and then copy your private key.

You can change your Cloud API private key at any time by clicking
**Regenerate private key**.

.. _command-line:

Authenticating in Cloud API RESTful interface calls
---------------------------------------------------

Each Cloud API call has a required username and password argument, in
the format ``user:password``. Use the email address in your Acquia
profile for the username, and the Cloud API private key in your Acquia
profile for the password.

.. _drush:

Authenticating in Drush Cloud commands
--------------------------------------

To use Drush Cloud commands, download the |acquia-product:ac| Drush
integration, as described in `Using Drush
aliases </acquia-cloud/drush/aliases>`__. Your Cloud API credentials are
included in the download, in the ``.acquia/cloudapi.conf`` file.

.. _browser:

Authenticating from a browser
-----------------------------

|acquia-product:api| also implements `Cross-origin resource sharing
(CORS) <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS>`__,
enabling you to implement authentication in browser-based clients when
using Acquia's supported API tokens. Requests should use the
``Access-Control-Allow-Origin`` header for identification.

.. |Edit your profile| image:: https://cdn4.webdamdb.com/1280_ANJ4181Z1uE8.png?1526476118
   :width: 321px
   :height: 483px
.. |Profile Credentials page| image:: https://cdn2.webdamdb.com/1280_M5MWwTjfhUA1.png?1526475789
   :width: 509px
   :height: 416px
