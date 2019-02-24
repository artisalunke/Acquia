.. include:: /common/global.rst

Creating Rules
===================

.. container:: message-status

   Creating Personalized Experiences with |acquia-product:cha| – |Back to intro|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/creating-personalized-experiences-acquia-lift

.. |Next lesson| replace:: Creating Goals
.. _Next lesson: /tutorials/creating-personalized-experiences-acquia-lift/creating-goals


Lesson Goal
-----------

.. note::  

   Create logic to display the right content, in the right area, to the right audience.

A rule is comprised of a slot_, a piece of content_, and a segment_.
Once content variations are added to a slot, a rule is created. You then
choose the segment to which the content in this rule applies, so that
|acquia-product:cha| can test this content on a specific group of
visitors to your website. An example of this is: for every visitor from
the geo-location of Boston, and is returning to the site, show them a
different homepage banner.

.. _slot: /tutorials/creating-personalized-experiences-acquia-lift/creating-slots
.. _content: /tutorials/creating-personalized-experiences-acquia-lift/publishing-content-experience-builder
.. _segment: /tutorials/creating-personalized-experiences-acquia-lift/creating-target-segment-personalization

About rules
-----------

Each slot on your page can have one or more rules that apply to that
slot. You can see rules using either of the following two methods:

-  Click **Expand Slot** in a highlighted slot, which expands the slot
   to the full window, allowing you to access all of the rules.
-  Click the **Rules** tab, which displays a list of all rules on the
   page, for all slots.

Rules can be one of two types: *draft* or *published*.

-  *Draft*

   -  Have a grey sidebar
   -  Displayed only to users with admin permissions who are signed in
      to |acquia-product:cha|

-  *Published*

   -  Have a green sidebar
   -  Displayed to all users

Creating rules
--------------

We are now going to add content to a slot and create a rule. The rule
will say that for everyone who is visiting our site from the Boston
area, show them a hero banner related to the city of Boston.

|Directions for Part 1|

#. Sign in to an |acquia-product:cha|-enabled website.
#. Activate the |acquia-product:lpm| `bookmarklet. </lift/drupal/3/bookmarklet>`__
#. The |acquia-product:cha| sidebar opens. |Part 2 of Directions|
#. In the sidebar, click the **Create** tab.
#. Click the **Content** tab, and enter your search criteria in the
   **Search for Content** field.
#. Click the **magnifying glass** button in the field to search.
#. |acquia-product:cha| displays a list of search results as thumbnail
   images with titles. These images represent pieces of content imported
   from your Drupal site for use as variations.
#. Click **Filter** to display the Filter & Search Content dialog box,
   and use the following fields to refine your search results:

   -  **Keywords**
   -  **Sources** list
   -  **Tags** list
   -  **Content Type (comma separated)**
   -  **Date(s)**

#. Click **Filter Content**. 
   
   |Part 3 of Directions|

#. To more easily find your available slots, flip the **Highlight
   Slots** toggle feature to **On** which will show all available slots
   in a blue outline.
#. Set your active `segment </lift/offers/segment>`__. Following our
   example, we will set our active Segment to Boston Visitors.
#. For information about creating additional segments, see `Managing
   your site's segments </lift/offers/segment#adding>`__.
#. Select the hero banner image and then drag it to the banner slot.
#. |acquia-product:cha| displays the slot with a yellow border and the
   message **New Rule**. |acquia-product:cha| displays the following
   options in a dialog box:

   -  **Create a new Rule** - Add a new rule with the added content \*To
      follow our example, select this option\*
   -  **Replace content** - Replace the content in an existing rule
   -  **Create A/B Test** - Create an A/B test rule from an existing
      targeting rule
   -  **Add to test** - Add the content to an existing testing rule

#. Your content is now displayed in the slot. A default click through
   goal is also created now that our content is added to the slot.

   -  Only the rules for the segment currently selected are displayed
      while dragging the content over, and only unpublished rules can be
      modified.

#. Once content is dragged to the slot, a message appears stating “Rule
   Created!” 
   
   |Part 3 of Directions|

#. Click the **Expand Slot** button to see the different rules in the
   slot.

   -  Here you can change the priority of rules to ensure visitors see
      the content you want them to see first.

#. The **Rule** is still in an unpublished state. Click the three dots
   next to the Rule name, click **Publish**, and then **Confirm**. 
   
   |Part 5 of Directions|

Congratulations, you have created and published a rule to display the
right content, in the right area, to the right audience.

Next Lesson > `Creating Goals </tutorials/creating-personalized-experiences-acquia-lift/creating-goals>`__
----------------------------------------------------------------------------------------------------------

.. |Directions for Part 1| image:: /sites/docs.acquia.com/files/inline-images/CreatingRules1-optimize.gif
.. |Part 2 of Directions| image:: /sites/docs.acquia.com/files/inline-images/CreatingRules2-optimize-resize.gif
.. |Part 3 of Directions| image:: /sites/docs.acquia.com/files/inline-images/CreatingRules3-optimize-resize.gif
.. |Part 3 of Directions| image:: /sites/docs.acquia.com/files/inline-images/CreatingRules4-optimize-resize.gif
.. |Part 5 of Directions| image:: /sites/docs.acquia.com/files/inline-images/CreatingRules5-optimize-resize.gif

