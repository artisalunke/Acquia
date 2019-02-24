.. include:: /common/global.rst

Embeddable: Carousel
====================

.. container:: message-status

  This feature is available only to |acquia-product:dam| Professional
  subscribers.

Embeddables allow admins and contributors to create code that embeds
assets on third-party platforms, including Wordpress, Drupal, and Brand
Connect — essentially anywhere you can embed code.

The **carousel** embeddable allows you to schedule when and how long an
asset displays, and what asset comes next.

For example, you want to display a holiday-themed promotional asset on
your Wordpress-powered website during the holidays, and when the
holidays are over you want to replace the asset with a different
campaign asset for an upcoming product launch. To do this, you can
create a carousel that displays the holiday asset from December 15 to
January 1, which then gets replaced by the campaign asset.

Using the carousel, you can schedule as many assets as you want, as far
into the future as you need.

There are two kinds of carousels available for your use:

-  `Basic carousel <#basic>`__ - Embed an asset or group of assets that
   rotate and repeat during specific intervals of time (hours, days,
   weeks, months).
-  `Advanced carousel <#advanced>`__ - Instead of a group of assets that
   rotate for the same period of time, schedule individual assets to
   rotate in and out at specific times.

.. _basic:

Creating a basic carousel
-------------------------

A basic carousel allows you to embed an asset or group of assets that
rotate and repeat during specific intervals of time (hours, days, weeks,
months). To create a basic carousel, complete the following steps:

#. Sign in to |acquia-product:dam|.
#. Select one or more assets that you want to embed, click the pencil
   icon |Pencil icon| in the actions toolbar, and then click **Embed
   assets**.
#. In the Carousel dialog box, configure your carousel with the
   following fields:

   -  **Carousel name** - Enter a descriptive name for the carousel.
   -  **Add a description** - Optionally, enter additional information
      to identify the carousel.
   -  **Carousel behavior** - Click **Basic**.
   -  **Start** - Skip this field to have the carousel start immediately
      after being created, or click **Change** to customize the start
      time.

#. Click the **Interval** dropdown menu to select Hours, Days, Weeks or
   Months and enter the interval duration.
#. Click the box next to **Repeat** if you want these assets to repeat
   their rotation.
#. Click **Continue**.

   |Carousel setup|

#. Click **ADD ASSETS** to add additional assets to your carousel.
#. The top asset is your default asset, meaning it will display any time
   there is a gap in scheduling. To change the default, point to the
   current default image, and then click the pencil icon |Pencil icon|.
   Select a new default, and then click **Insert**.
#. If you want to change an individual asset’s interval time, click the
   duration under the asset file name, update the interval and click
   **Set**.
#. Click the **Continue** button.

   |Carousel assets|

#. Select the preferred resolution **Size**, and then copy the **Embed**
   code.

You can now paste the embed code wherever you want to post the carousel.

|Carousel embed|

.. _advanced:

Creating an advanced carousel
-----------------------------

An advanced carousel allows you to schedule start and stop times and
dates for individual assets, with no looped repeating.

#. Sign in to the core application.
#. Select the assets you want to embed (hold down ``Command`` key on a
   Mac or the ``CTRL`` key on a PC to select multiple assets) and click
   the |Pencil icon| **Pencil** icon on the actions toolbar. Select
   **Embed assets**.
#. *SETUP*:

   #. Enter a carousel name and an optional description, then select
      **Advanced**.
   #. Click **Change** to customize the start time, or move on if you
      want it to start immediately.
   #. Click the **Continue** button.

#. *ASSETS*:

   #. Click **ADD ASSETS** to add additional assets to your carousel.
   #. The top asset is your default asset, meaning it will display any
      time there is a gap in scheduling. To change the default, hover
      over the current default image and click the |Pencil icon|
      **Pencil** icon. Choose a new default and click **Insert**.
   #. Click **Schedule** next to each asset to set start and stop
      display dates and times. By default, the interval date will be one
      week.
   #. Click the **Continue** button.
      |Carousel schedule|

#. *EMBED*:

   #. Select the preferred resolution size, then copy the embed code.
   #. Paste the embed code wherever you want to post the asset.

.. _manage:

Managing a carousel
-------------------

Contributors may manage their own carousels, while admins may manage
carousels created by all users.

#. Sign in to the core application.
#. At the bottom of the the left menu, click **Embeddables**.
#. Hover over the embeddable you want to edit and click the |Pencil
   icon| **Pencil** icon. Select **Edit** to make changes or check
   settings.
#. Edit the settings. Click the **Close** button when you’re finished.

.. |Pencil icon| image:: https://cdn2.webdamdb.com/100th_sm_2xhR0XmxWk21.png?1526475528
   :width: 21px
   :height: 21px
.. |Carousel setup| image:: https://cdn4.webdamdb.com/1280_M0oRN32qm251.png?1526475979
   :width: 500px
   :height: 491px
.. |Carousel assets| image:: https://cdn4.webdamdb.com/1280_o8GRgenwNrR9.png?1526475450
   :width: 500px
   :height: 563px
.. |Carousel embed| image:: https://cdn4.webdamdb.com/1280_sJg2ZsDm18k9.png?1526476104
   :width: 550px
   :height: 542px
.. |Carousel schedule| image:: https://cdn4.webdamdb.com/1280_sjCfXFHMuPR2.png?1526475636
   :width: 500px
   :height: 563px
