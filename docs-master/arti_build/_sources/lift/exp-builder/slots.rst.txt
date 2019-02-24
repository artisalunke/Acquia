.. include:: /common/global.rst

Creating slots in |acquia-product:leb|
======================================

.. toctree::
   :hidden:
   :glob:

   /lift/exp-builder/slots/*

|acquia-product:leb| allows you to both track the behavior of your
website's visitors and customize your content to match their interests.
You can then test your visitors' reactions to this customized content to
ensure that your marketing strategy is working. For more information,
see `Planning your A/B testing </lift/exp-builder/rule/ab>`__ or 
|types|_.

.. |types| replace:: Types of personalizations in \ |acquia-product:cha|\ 
.. _types: /lift/drupal/personalization-types

In |acquia-product:cha|, a *rule* is a set of customized content
targeted toward a particular audience, designed to prompt the defined
audience to take specific actions on your website.

The first step in creating rules in |acquia-product:leb| is defining a
*slot*. A slot is an area on your website that you configure to be able
to display A/B tests or targeted content. After you create a slot, you
can drag and drop content variations into it to create rules.


.. container:: message-status

   |Learning Services logo|\ For a step-by-step video tutorial introducing you 
   to personalization with |acquia-product:cha|, including creating slots, see |Creating|_.

.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px

.. |Creating| replace:: Creating Personalized Experiences with \ |acquia-product:cha|\ 
.. _Creating: /tutorials/creating-personalized-experiences-acquia-lift


Creating a slot
---------------

To create a slot, complete the following steps:

#. Sign in to your website as an administrative user with content
   personalization management rights.
#. Activate the |acquia-product:leb|
   `sidebar </lift/exp-builder/access>`__.
#. On the **Create** tab, click the **Slots** tab. |acquia-product:leb|
   displays a list of available slots on this webpage. If there are no
   available slots, |acquia-product:leb| displays the message
   ``There are no slots on this page. Add a slot to begin customizing your website's experience``.
#. To add a new slot, click **Create new slot**. |acquia-product:leb|
   displays a dialog box.
#. In the **Slot Name** field, enter a name that describes this slot's
   purpose (for example, **Frontpage Banner**).
#. In the **Slot Pages** field, enter the paths for the webpages where
   you want this slot to display, one webpage per line.
   |acquia-product:leb| displays the domain on which you are running
   |acquia-product:lpm| above the **Slot Pages** field. By default, this
   field displays the path of the webpage that you are currently
   visiting.

   .. note::  
   
      If you attempt to enter a name for a slot that matches an existing
      slot name anywhere on the website (not just on the webpage), the
      system will display an error message.

#. Click **Create Slot**.
   |acquia-product:leb| displays an **Embed Code** dialog box that
   contains the code that you can use to place this slot on your
   webpage. You can use the **Copy to clipboard** link to copy the embed
   code, which you can then paste and save in your
   website's code. This code can be applied to elements such as ``div``
   and ``p``.
#. Click **Save**.

|acquia-product:leb| displays the new slot in the following locations:

-  In the **Slots** tab
-  On the webpage where you have created it

**Highlight Slot On/Off** - This setting allows you to move between
previewing your website and manipulating content in a selected slot.
When slot highlighting is on, |acquia-product:leb| displays your slot
with a border. In this state, it is not possible to navigate around your
webpage and click links. When slot highlighting is off, you can click
links, navigate around your webpage and see the slot as it appears to
your website visitors. Highlighting remains on until it is turned off by
clicking **Off** or by collapsing the sidebar. Navigating to the
**Slots** tab automatically turns highlighting **On**.

After you have added all your desired slots, you can use
`rules </lift/exp-builder/rule>`__ to determine the content variations
that you want to appear in your slots.

Managing your slots
-------------------

Depending on your needs, you can edit existing slots, or remove them
from your website if they are no longer needed. Each slot lists all the
different webpages of your website the slot will be embedded on. By
default, the current webpage you are viewing is always entered in the
field. Additional webpages are included in a new line break using the
relative path to the current webpage.

If you have not embedded the slot code in a webpage — for example, if
you have created a slot with multiple webpages added, but have not added
the code to the webpages yet — the slot displays the following warning
message: ``Slot code not found on page``. Click **Configure** to obtain
the embed code, or click **Delete** to remove the slot from the webpage.

If a slot is defined in a single node on a single webpage, and that node
is deleted, the slot will no longer appear in the user interface. It may
appear as if though the slot has also been deleted — however, the slot
information still exists in the database and is accessible using the
API. If you recreate a node with the same path, the slot information
will again be displayed in the user interface.

If a slot displays a flash of unstyled content, you can alter the
initial display of the slot to `prevent unstyled content from
displaying </lift/exp-builder/slots/unstyled>`__.



Editing your slots
~~~~~~~~~~~~~~~~~~

To edit a slot, complete the following steps:

#. Click the **Create > Slots** tab.
#. Click **Configure** to make changes.
#. Click **Save** to save your changes or **Cancel** to discard changes.


Deleting your slots
~~~~~~~~~~~~~~~~~~~

To delete a slot, complete the following steps:

#. Navigate to the webpage where the slot exists.
#. Click the **Slots** tab.
#. Find the slot you want to remove, and click **Delete**.
#. If there are rules associated with the slot, they will be deleted as
   well. |acquia-product:leb| displays a confirmation box displaying the
   number of associated rules. Click **Delete** to confirm deletion.

If you have embedded HTML paragraph tags in your embed code and you
delete a slot, the embedded HTML will no longer display on the webpage,
with or without slot highlighting enabled. This causes the embedded HTML
to be hidden from view.

Next, you will need to `create rules </lift/exp-builder/rule>`__ to
place content in these slots.


Adding CSS to a slot
~~~~~~~~~~~~~~~~~~~~

It is possible to add additional styling to a slot's content. You can specify an external 
stylesheet to be loaded into a slot by adding a data 
attribute on the slot's <div>. Adding external CSS is primarily useful for untrusted slots that
render inside of an iframe, and therefore need the external CSS. To
learn more about trusted and untrusted modes, see 
`Content replacement modes </lift/exp-builder/config/modes>`__.

.. code-block:: none

   <div data-lift-slot="my-slot-id" data-lift-css="http://mysite.com/custom_slot.css"></div>

Creating a customizable slot
----------------------------

It is possible to serve decisions and content to a webpage, but not
inject the content into that webpage. Using the `content replacement
mode </lift/exp-builder/config/modes>`__, returned content is broadcast
with JavaScript events, allowing your website's JavaScript to customize
the output to meet your website's needs.

Retrieving a list of defined slots
----------------------------------


.. |decision API| replace:: \ |acquia-product:cha|\ Decision API 
.. _decision API: http://docs.lift.acquia.com/decision/#slots_get

Using the 
`Postman HTTP-HMAC package <https://github.com/acquia/http-hmac-postman>`__, you 
can retrieve a full list of the locations on your website with previously
created slots. To retrieve this slot list, construct an API call based
on the parameters in the ``/slots`` endpoint in the
|decision API|_, replacing
``[domain]`` with your Lift API URL, ``[site_id]`` with your
|acquia-product:cha| website ID, and ``[account_id]`` with your
|acquia-product:lpm| account ID:

.. code-block:: none

   https://[domain]/slots?site_id=[site_id]&account_id=[account_id]

To obtain your API URL, ``site_id``, and ``account_id``, see the
|acquia-product:liftapi| `reference </lift/omni/rest_api>`__. For more
information about the Postman HTTP-HMAC package, see `Using the
Acquia Lift APIs </lift/omni/api>`__.
