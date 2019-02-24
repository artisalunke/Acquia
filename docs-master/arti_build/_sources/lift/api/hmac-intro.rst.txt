.. include:: /common/global.rst

|acquia-product:liftapi| and HMAC authorization
===============================================

Based on |acquia-product:cha| account configuration, API calls may
require HMAC authentication as a header within the request. HMAC is a
keyed-hash authentication code that calculates a message authentication
code (MAC) involving a cryptographic hash function in combination with a
secret cryptographic key.

This authentication scheme protects your data and ensures that your
secret keys stay secure, and utilizes the Access Key ID and secret
access key associated with your |acquia-product:cha| subscription.

Acquia has HMAC implementation scripts in `several
languages <https://github.com/acquia?&q=hmac>`__, including the
following:

-  `Ember <https://github.com/acquia/ember-http-hmac>`__
-  `Go <https://github.com/acquia/http-hmac-go>`__
-  `Javascript <https://github.com/acquia/http-hmac-javascript>`__
-  `PHP <https://github.com/acquia/http-hmac-php>`__
-  `Ruby <https://github.com/acquia/http-hmac-ruby>`__

|acquia-product:liftapi| calls support authentication with both HMAC v2
and HMAC v1.

.. note::  

   Although HMAC v1 is still supported, Acquia recommends that you use HMAC
   v2 with your |acquia-product:liftapi| calls.

-  `|acquia-product:cha| HMAC v2 authorization
   (recommended) </lift/omni/api/hmacv2>`__
-  `|acquia-product:cha| HMAC v1 authorization </lift/omni/api/hmac>`__
