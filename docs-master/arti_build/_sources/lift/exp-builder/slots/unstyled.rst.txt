.. include:: /common/global.rst

Flash of unstyled content in slots
==================================

Flashes of unstyled content (FOUC) can occur in |acquia-product:cha|
when a `slot </lift/exp-builder/slots>`__ is created around content that
is initially rendered server-side before it can be personalized through
JavaScript. This slight delay can cause unstyled content to appear
momentarily on-screen, immediately followed by the personalized content
rendering and displaying in its place.

Flashes of unstyled content cannot be entirely prevented, but they can
be mitigated with one of the following methods:


Using CSS to hide the initial display of the slot
-------------------------------------------------

You can alter the initial display of the ``block-content__hero`` slot by
settings its opacity to ``0`` as described in the following example:

.. code-block:: css

   // CSS, needs to be replaced with the appropriate selectors
   // Source: https://docs.acquia.com/lift/exp-builder/slots/unstyled
   .block-content__hero {
      opacity: 0;
      -webkit-transition: opacity 300ms;
   }


Using JavaScript to change the display of the slot
--------------------------------------------------

To alter the initial display of a `slot </lift/exp-builder/slots>`__
with JavaScript, create a script that listens for the
``acquiaLiftContentAvailable`` or ``acquiaLiftStageCollection`` event
and then alters the slot's opacity back to ``1``, as described in the
following example code:

.. code-block:: JavaScript

   // JavaScript for altering the opacity of a slot
   // Source: https://docs.acquia.com/lift/exp-builder/slots/unstyled
   (function() {
      window.addEventListener('acquiaLiftContentAvailable', function(e) {
         console.log('acquiaLiftContentAvailable event occurred. This indicates a rule is published and is the last event in the personalization rendering.');
         console.log(e);
         jQuery('*[data-lift-slot="' + e.detail.decision_slot_id + '"]').css('opacity','1');
      });
      window.addEventListener('acquiaLiftStageCollection', function(e) {
         console.log('acquiaLiftStageCollection event occurred. This is the end of the Acquia Lift lifecycle and should occur whether rules are published or not.');
         console.log(e);
         jQuery('*[data-lift-slot]').css('opacity','1');
      });
   })();
