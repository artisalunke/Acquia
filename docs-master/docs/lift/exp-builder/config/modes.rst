.. include:: /common/global.rst

Content replacement modes
=========================

When you want |acquia-product:cha| to directly inject and display
personalized content on your website, you can set a
`slot's </lift/glossary#slot>`__ mode to *trusted* or *untrusted*. If
your website requires content to be injected and displayed in your own
customization (such as in a decoupled Drupal installation), you can set
the slot's mode to *customized*.

-  *Trusted mode* - If you control all imported content and are sure
   that any styles or JavaScript your content contains are safe for your
   website.
   When content is displayed in *trusted mode*, your website will render
   that content inline, as if it were native to your local website.
-  *Untrusted mode* - If you do not control the imported content, or you
   want to protect your website from potentially unsafe JavaScript or
   unsuitable CSS styling that the content may contain.
   When content is displayed in *untrusted mode*, the imported content
   will use the style of the original publishing website by wrapping the
   content in an ``<iframe>``.
-  *Customized mode* - If you want to further customize the display or
   content of the content with your own local JavaScript code while
   still utilizing |acquia-product:cha| decisions and content, such as
   in a single-page application or decouple Drupal installation.
   When content is displayed in *customized mode*, the decisions and
   their content are requested on-demand and broadcast using JavaScript
   events, causing your scripts will receive and react to them
   accordingly.

Changing content replacement mode
---------------------------------

To alter the content replacement mode used on your website, perform the
following steps to modify your |acquia-product:cha| configuration
settings:

#. Sign in to your website as an administrator.
#. Click **Configure > Acquia Lift Settings**.
#. Scroll down the webpage, and then click **Advanced configuration** to
   expand it.
#. In the **Content replacement mode** section, select one of the
   following values:

   -  **Trusted**
   -  **Untrusted** (default)
   -  **Customized**

#. Click **Save configuration**.

Overriding slot modes
---------------------

`One or more slots </lift/exp-builder/slots>`__ can have a different
setting than the website default. If you have a given slot that will
always hold untrusted content on an otherwise trusted website, or vice
versa, you can override the slot to have a non-default setting.

Within the `embed code </lift/exp-builder/slots#slots>`__ that you add
to your page, add the following line to set a particular slot to always
be trusted:

.. code-block:: none

   <div data-lift-slot="my-overridden-slot" data-lift-mode="[MODE]" />

where ``[MODE]`` is ``trusted``, ``untrusted``, or ``customized``.

Styling untrusted content
-------------------------

Trusted content automatically uses the style of your website by applying
appropriate CSS and targeting. When you are using imported content that
is not trusted, it does not use that CSS and its styling may not fit
with the style of your website. You can apply an attribute to the slot,
which applies a stylesheet:

.. code-block:: none

   <div data-lift-slot="my-slot-id" data-lift-css="http://mysite.com/custom_slot.css"></div>

Styles and scripts in trusted mode
----------------------------------

When rendering content in trusted mode, it is important to understand
when styles should or should not be imported with the content as
rendered by the view mode. In some cases, rendering the content in an
untrusted iframe will require additional styling and scripting that not
should be included in directly injected trusted content (or should be
the responsibility of the |acquia-product:cha| website displaying the
content).

In trusted content mode, |acquia-product:cha| renders *markup only* in 
``<body>`` tags, which removes all styles and scripts included in the 
``<head>`` tags that includes ``data-content-barrier-exclude="true"`` in 
its attributes. This attribute is applied by |acquia-product:ch| rendering 
templates for all footer JavaScript code. Content injected in untrusted mode 
will be injected as-is, with all markup included.

The intention with trusted mode is that the website receiving the
injected content should control the styling and scripting of content,
whether injected or rendered natively on the page. There are situations
when the content for replacement is architected in a more
component-based approach, and styles or scripts should be packaged with
the content for use in either trusted on untrusted mode. In these cases,
any styles and scripts necessary should be rendered in the ``<body>``
of the rendered view mode content in |acquia-product:ch|.


Example
~~~~~~~

For example, in untrusted mode, this markup is rendered:

.. code:: html

   <!DOCTYPE html>
   <html lang="en">
   <head>
      <style>
      .my-custom-style { color: #000000; }
      </style>
      <link rel="stylesheet" href="http://mysite.com/stylesheet.css" />
      <script type="text/javascript" src="http://mysite.com/myexternaljs.js"></script>
      <script>
      var foo = 'bar';
      </script>
   </head>
   <body>
      <style>
      .perfect { color: #39ff14; }
      </style>
      <script>
      var perfect = 'check out that style';
      </script>
      <p class="perfect">My perfect content
         <span data-content-barrier-exclude="true">Don't show this in trusted mode</span>
      </p>
      <div data-content-barrier-exclude="true">
      <script type="text/javascript" src="http://mysite.com/myfooterjs.js"></script>
      </div>
   </body>
   </html>

However, if the content is *trusted*, only this section will be
rendered:

.. code:: html

   <style>
   .perfect { color: #39ff14; }
   </style>
   <script>
   var perfect = 'check out that style';
   </script>
   <p class="perfect">My perfect content
   </p>

Working with customized content
-------------------------------

After setting a slot to ``customized`` mode, its content is now
broadcast to the webpage instead of being injected into the webpage. To
work with the content being broadcasted (but not displayed), you must
implement the following in your website's code:

#. Define a page-level JavaScript event listener on the
   ``acquiaLiftContentCustomizable`` event to process the data, and
   customize your website. For details about how to implement this
   function, see `JavaScript API events </lift/javascript/events>`__.
#. Call the public API function ``AcquiaLiftPublicApi.customize()``. For
   details about how to call ``customize()``, see 
   `Personalize methods </lift/javascript/personalize>`__.

With the slot included on a webpage, it will be monitored and tracked by
|acquia-product:cha|, even if the content is not injected.
