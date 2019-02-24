.. include:: /common/global.rst

Embedding slots on a page
=========================

There are several available methods for embedding a
`slot </lift/exp-builder/slots>`__ into your webpages for personalized
content, including `adding code to an element <#add>`__, `using CSS
selectors <#selector>`__, and `adding to the theme <#theme>`__.

Adding code to an element
-------------------------

If a page element has an HTML section that can be edited, you can add an
embed code to the element. For example, to add code to a block, complete
the following steps:

#. Copy the embed code.
#. Add the embed code to a block. The block must use the Full HTML
   format, and you must edit the HTML source code to add the ``div``
   correctly.
#. Save the block.
#. Add the block to the webpage in Full HTML or another trusted format.

This block can now be used as a slot for |acquia-product:leb|. The embed
code is HTML, and will render in the webpage, but is not visible to the
user.


Using CSS selectors
-------------------

You can manually enter a webpage element’s `CSS
selector(s) <https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors>`__
into the labeled field on a slot card. Any selector or group of
selectors that can be defined with CSS can be used by
|acquia-product:cha| to define your slot region.

Users can enter one or more selectors into the field to define the slot
region on the webpage.

|Adding a CSS selector|

The selector or group of selectors entered into the field:

-  must be unique across all the slots on your website.
-  must not belong to a page element whose parent or child element is
   also an |acquia-product:cha| slot.
-  must target an `HTML block-level
   element <https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements>`__
   on the page, such as:

   -  ``p``
   -  ``li``
   -  ``div``
   -  headers (``h1``, ``h2``, and others)

   .. note::  

      Acquia does not recommend using special-use tags (such as ``image``,
      ``canvas``, ``video``, ``br``, or ``hr``) as these are unlikely to
      work well for slots.

This ensures that multiple slots do not overlap with each other on your
webpage, and that two slots do not use the same region of your website.
If you have overlapping selectors, |acquia-product:leb| may display a
message similar to the following:

.. code-block:: none

   Please ensure the slot's chosen CSS selector targets a single element 
   on the page and does not conflict with any existing Lift slots. See 
   the "How to use CSS selectors" link above for more details.

If your selector matches multiple elements, only the first matched
element will render a slot. An example of a selector group that can be
used by |acquia-product:cha|:

.. code-block:: CSS

   #first-line div > p

Entering this code into the slot’s CSS Selector field enables
|acquia-product:cha| to use a paragraph in a ``div`` that uses the ID
``first-line`` as an |acquia-product:cha| slot. You can change the CSS
selector that was entered into the field on the slot card at any time,
which changes only where the slot is rendered on the webpage. Any rules
that you have created for the slot are not affected when you modify the
slot’s CSS selector.

.. _replace:

Content replacement mode
~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:leb| allows you to configure slots with different
`content replacement modes </lift/exp-builder/config/modes>`__, which
define how the content is provided:

-  *trusted mode* - Content is injected plainly
-  *untrusted mode* - Content is injected, but encapsulated
-  *customized mode* - Content is not injected, but is provided by
   JavaScript for further customization

Finding a selector
~~~~~~~~~~~~~~~~~~

You can use your `browser's tools </resource/browser-tool>`__ to inspect
a webpage and find the identity of a particular element.

For a potentially easier selector discovery method, we recommend that
you use a browser extension to find the CSS selectors on your webpage.
For specific solutions, visit your browser’s extension or add-on store.

.. _theme:

Adding to the theme
-------------------

You can also add slot information to your website theme, as part of your
committed code. However, embedding slot information this way can make it
more difficult for users to change it.

.. |Adding a CSS selector| image:: https://cdn4.webdamdb.com/1280_YypQsiBcNTU8.png?1526475752
   :width: 345px
   :height: 137px
