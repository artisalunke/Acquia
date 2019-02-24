.. include:: /common/global.rst

captureIdentity - Acquia Lift JavaScript API
============================================

When capturing events, sometimes you may want to directly send
additional identifying visitor information to |acquia-product:cha| — for
example, the website visitor's email address, social media username, or
an identifier from another system (such as a subscriber ID).

.. admonition::  Note for Drupal users

   You can 
   `install and use the Drupal modules </lift/exp-builder/install>`__ on your 
   website to send identifying information to |acquia-product:cha|, including 
   registration and login events and the corresponding email address of a 
   website visitor.

Although you can use functions in the JavaScript API to capture these
items, |acquia-product:cha| includes a special *identity* method that
collects this information into a single array of values.

To send a website visitor's identity information directly to
|acquia-product:cha|, use the following JavaScript code:

.. code-block:: none

   <script>
   _tcaq.push(['captureIdentity', '<value>', '<identity-type>']);
   </script>

Modify the example based on your website's needs by replacing the
following variables:

-  ``<value>`` - The value that you want to assign to a subparameter
-  ``<identity-type>`` - An information type that you can populate with a
   visitor-specific value

   Select from the following identity types for your use:

   +-----------------------------------+-----------------------------------+
   | Identity type                     | Description                       |
   +===================================+===================================+
   | ``email``                         | Email address                     |
   +-----------------------------------+-----------------------------------+
   | ``account``                       | Account ID, possibly an           |
   |                                   | identifier from another tracking  |
   |                                   | system                            |
   +-----------------------------------+-----------------------------------+
   | ``facebook``                      | Facebook username                 |
   +-----------------------------------+-----------------------------------+
   | ``twitter``                       | Twitter username                  |
   +-----------------------------------+-----------------------------------+
   | ``name``                          | Name, including first, middle,    |
   |                                   | last, or any combination of these |
   +-----------------------------------+-----------------------------------+
   | custom identifier                 | Customized visitor-specific       |
   |                                   | information that you want         |
   |                                   | |acquia-product:cha| to treat as  |
   |                                   | an identifier, such as            |
   |                                   | ``subscriber ID``                 |
   +-----------------------------------+-----------------------------------+

Sending additional parameters with captureIdentity
--------------------------------------------------

You can send additional information as parameters using the
``captureIdentity`` method, which is similar to other
|acquia-product:cha| Web capture methods. To do this, send your
parameters based on the following example:

.. code-block:: JavaScript

   _tcaq.push(['captureIdentity', '<value-identity>', '<identity-type>', {'<parameter>':'<value-param>'}]);


Because the ``captureIdentity`` method supports sending only a single
identity subparameter, you can also add ``identity`` as a special type
parameter to your ``captureIdentity`` method, allowing you to send
multiple identity values to |acquia-product:cha|.

.. code-block:: JavaScript

   _tcaq.push(['captureIdentity', '<value-identity>', '<identity-type>', {'<parameter>':'<value-param>'}, {'identity':{'<value-identity-2>':'<identity-type-2>'}}]);

.. note::  

   If you are not sending any parameters with a capture event, but are
   using ``identity`` as a parameter, be sure to include ``{}`` for the
   empty list of regular parameters.

The following example sends a website visitor's name and email address
using a single JavaScript capture instruction:

.. code-block:: javascript

   _tcaq.push(['captureIdentity', 'jdoe@example.com', 'email', {}, {'identity':{'John':'name'}}]);


Sending identity values with other capture methods
--------------------------------------------------

If you want to send website visitor identity information that's
associated with a website event (such as a registration event), you can
use the ``identity`` method as a parameter in the JavaScript event
capture code. The following example captures a page view with an event
category of Technology along with the website visitor's email address:

.. code-block:: JavaScript

   _tcaq.push(['capture', 'Technology', {}, {'identity':{'jdoe@example.com':'email'}}]);

.. _interpret:

Interpreting capture-related error messages
-------------------------------------------

Occasionally, merge failures can occur during visitor information
captures due to website visitors having more than 25 identifiers.
Visitors often have several identifiers — for example, a new identifier
is generated for both a visitor signing in to your website from a
different browser, and using a different email address. If the
|acquia-product:cha| service needs to merge a 26th identifier for a
visitor, it instead generates a new tracking ID and merges the new
identifier with that tracking ID. This helps to prevent the
|acquia-product:cha| service from experiencing performance issues
related to oversized visitor profiles.

If a merge failure occurs for a specific website visitor, the
|acquia-product:cha| service displays error messages in that visitor's
profile on the |People tab|_. You do not
need to take any action related to these messages, as these errors do
not affect how |acquia-product:cha| operates, other than by improving
its performance.


.. |People tab| replace:: **People** tab
.. _People tab: /lift/profile-mgr/person