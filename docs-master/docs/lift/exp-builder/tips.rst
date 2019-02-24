.. include:: /common/global.rst

|acquia-product:leb| tips
=========================

This page contains other useful tips for interacting with
|acquia-product:leb|.

- How do my custom effects adjust when the |acquia-product:leb| sidebar appears and disappears?
   When you display the |acquia-product:leb| sidebar, the sidebar adjusts
   the ``<body>`` tag's right margin. |acquia-product:leb| dispatches the 
   standard window resize events whenever the ``<body>`` is adjusted to display 
   or hide the sidebar. Any custom code for the webpage should listen for both 
   window resize events to adjust for changes in the browser viewport and 
   changes based on |acquia-product:leb| inclusion. As with any window resize 
   events, handlers should expect this event to fire frequently and utilize a
   debounce method when appropriate.
