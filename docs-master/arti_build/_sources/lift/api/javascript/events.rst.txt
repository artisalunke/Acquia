.. include:: /common/global.rst

JavaScript API event notifications
==================================

|acquia-product:cha| provides event notifications for decision handling.
Whenever an event triggers, this notification can enable custom
JavaScript to use that trigger to provide additional functionality.

You can trigger the following events:

+-----------------------------------+-----------------------------------+
| Event                             | Description                       |
+===================================+===================================+
| ``acquiaLiftDecision``            | Triggers when a decision has been |
|                                   | received and processed — the      |
|                                   | content may still be in the       |
|                                   | rendering process, but data is    |
|                                   | available and processing is       |
|                                   | complete                          |
+-----------------------------------+-----------------------------------+
| ``acquiaLiftContentAvailable``    | Triggers when a decision's        |
|                                   | content has been rendered by the  |
|                                   | browser and is available for      |
|                                   | manipulations or query            |
+-----------------------------------+-----------------------------------+
| ``acquiaLiftContentCustomizable`` | Triggers when                     |
|                                   | ``AcquiaLiftPublicApi.customize() |
|                                   | ``                                |
|                                   | is called; contains all the       |
|                                   | decisions and their contents in   |
|                                   | customizable slots. See |modes|_. |
+-----------------------------------+-----------------------------------+
| ``acquiaLiftClickThrough``        | Triggers when decision content is |
|                                   | clicked                           |
+-----------------------------------+-----------------------------------+

.. |modes| replace:: Content Replacement modes
.. _modes: /lift/exp-builder/config/modes

.. _detail:

Details
-------

For ``acquiaLiftDecision``, ``acquiaLiftContentAvailable``, and
``acquiaLiftClickThrough``, each event has a ``detail`` property, which
can include the following available information about the decision:

+-----------------------------------+-----------------------------------+
| Detail                            | Description                       |
+===================================+===================================+
| ``decision_content_id``           | The ID of the content that was    |
|                                   | displayed                         |
+-----------------------------------+-----------------------------------+
| ``decision_content_name``         | The title of the content that was |
|                                   | displayed                         |
+-----------------------------------+-----------------------------------+
| ``decision_policy``               | The decision policy used to make  |
|                                   | the decision                      |
+-----------------------------------+-----------------------------------+
| ``decision_rule_id``              | The ID of the rule that was used  |
|                                   | to replace content                |
+-----------------------------------+-----------------------------------+
| ``decision_rule_name``            | The name of the rule that was     |
|                                   | used to replace content           |
+-----------------------------------+-----------------------------------+
| ``decision_rule_segment_id``      | The ID of the segment on which    |
|                                   | the rule triggers                 |
+-----------------------------------+-----------------------------------+
| ``decision_rule_segment_name``    | The name of the segment on which  |
|                                   | the rule triggers                 |
+-----------------------------------+-----------------------------------+
| ``decision_rule_type``            | The type of rule that was used —  |
|                                   | examples include ``ab`` (for `A/B |
|                                   | testing </lift/exp-builder/rule/a |
|                                   | b>`__)                            |
|                                   | and ``target`` (for targeting)    |
+-----------------------------------+-----------------------------------+
| ``decision_slot_id``              | The ID for the slot where content |
|                                   | was replaced                      |
+-----------------------------------+-----------------------------------+
| ``decision_slot_name``            | The name of the slot where        |
|                                   | content was replaced              |
+-----------------------------------+-----------------------------------+
| ``decision_view_mode``            | The ID of the layout of the       |
|                                   | content that was displayed        |
+-----------------------------------+-----------------------------------+

For ``acquiaLiftContentCustomizable``, each event has the following
properties.

+-----------------------------------+-----------------------------------+
| Detail                            | Description                       |
+===================================+===================================+
| ``contents``                      | An array of content pieces, with  |
|                                   | each content piece containing     |
|                                   | ``base_url``, ``html``, and       |
|                                   | ``id``. ``base_url`` is content's |
|                                   | publishing site's base URL;       |
|                                   | ``html`` is the content markup,   |
|                                   | and; ``id`` is the id of the      |
|                                   | content. See `Content Replacement |
|                                   | modes </lift/exp-builder/config/m |
|                                   | odes>`__.                         |
+-----------------------------------+-----------------------------------+
| ``slot_css_selector``             | As configured in the slot, the    |
|                                   | CSS selector to find the slot, if |
|                                   | it exists, on the page            |
+-----------------------------------+-----------------------------------+

Examples
--------

You can use the following code examples to provide further customization
on your website:

.. _decisionevent:

Example: ``decision`` event
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: JavaScript

   window.addEventListener('acquiaLiftDecision', function(e) {
   console.log('received decision event for ' + e.detail.decision_slot_id + ' slot');
   });

In the previous example, ``acquiaLiftDecision`` is the
`event <#event>`__, and ``decision_slot_id`` is the `detail <#detail>`__
property. Both of these can be replaced by other values, as explained in
the following sections.

To customize your personalized content pieces, use code similar to the
following:

.. code-block:: JavaScript

   // Define a callback function for "acquiaLiftDecision" event.
   window.addEventListener('acquiaLiftDecision', function(e) {
      // e.detail has decision's information. If the decision isn't our target "My Carousel Slot", early exit.
      if (e.detail.decision_slot_name !== 'My Carousel Slot') {
         return;
      }
      // For example, you can select all content pieces within a slot, and wrap each one of them by a <div>.
      jQuery('[data-lift-slot="' + e.detail.decision_slot_id + '"] > *').wrap('<div style="border: 1px solid red;" class="my-carousel-item"></div>');
   });

If your website uses custom JavaScript (such as slideshows, modal
windows, or custom dropdown lists), you may need code to both listen for
the returned decision and reinitialize your JavaScript library. The
following example uses the
`Chosen <https://harvesthq.github.io/chosen/>`__ library:

.. code-block:: JavaScript

   window.addEventListener('acquiaLiftDecision', function(e) {
   console.log('received decision event for ' + e.detail.decision_slot_id + ' slot');
   console.log("Loaded");
   
   $selectItems = jQuery('.form-item select'); 
   $selectItems.delay(1000).chosen({
      disable_search_threshold: 5,
      no_results_text: "No Results Found.",
      width: "100%" 
   }).prop('disabled', false).trigger("chosen:updated");
   });


Example: ``acquiaLiftContentCustomizable`` event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: JavaScript

   window.addEventListener('acquiaLiftContentCustomizable', function(event) {
   // Console to show the customizable decision content.
   console.log('acquiaLiftContentCustomizable', event.detail);
   });

To customize your personalized content pieces using decision data, use
code similar to the following:

.. code-block:: JavaScript

   window.addEventListener('acquiaLiftContentCustomizable', function(event) {
   // Console to show the customizable decision content.
   console.info('acquiaLiftContentCustomizable', event.detail);
   // Process decisions.
   var decisions = event.detail;
   Object.keys(decisions).forEach(function(slotId) {
      // Process a decision.
      var decision = decisions[slotId];
      var html = decision.contents.reduce(function(html, content) { return html + content.html }, '');
      var slotElement = document.querySelector(decision.slot_css_selector);

      if (!slotElement) {
         console.warn('Decision on slot "' + slotId + '" has HTML "' + html + '", but slot is not on the page.');
         return;
      }

      // Empty out the element.
      while (slotElement.hasChildNodes()) {
         slotElement.removeChild(slotElement.lastChild);
      }

      // Set the customizable content to the target element's innerHTML.
      slotElement.innerHTML = html;
   });
   });