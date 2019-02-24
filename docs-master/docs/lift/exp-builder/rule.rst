.. include:: /common/global.rst

Creating rules in |acquia-product:cha|
======================================

.. toctree::
   :hidden:
   :glob:

   /lift/exp-builder/rule/*

When you add one or more content variations to a
`slot </lift/exp-builder/slots>`__, you create a *rule*. You then choose
the segment to which the content in this rule applies, so that
|acquia-product:cha| can test this content on a specific group of
visitors to your website.


About rules
-----------

Each slot on your webpage can have one or more rules that apply to that
slot. You can see rules using either of the following two methods:

-  Click **Expand Slot** in a highlighted slot, which expands the slot
   to the full window, allowing you to access all of the rules.
-  Click the **Rules** tab, which displays a list of all rules on the
   webpage, for all slots.

Rules can be one of two types: *draft* or *published*.

-  *Draft*

   -  Have a grey sidebar
   -  Displayed only to users with admin permissions who are signed in
      to |acquia-product:cha|

-  *Published*

   -  Have a green sidebar
   -  Displayed to all users

.. container:: message-status

   |Learning Services logo|\ For a step-by-step video tutorial introducing you 
   to personalization with |acquia-product:cha|, including creating rules, see 
   |tutorial|_.

.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px

.. |tutorial| replace:: Creating Personalized Experiences with \ |acquia-product:cha|\ 
.. _tutorial: /tutorials/creating-personalized-experiences-acquia-lift


Creating rules
--------------

To add content to a slot and create a rule, complete the following
steps:

#. Sign in to an |acquia-product:cha|-enabled website as an
   administrative user.
#. Activate the |acquia-product:lpm|
   `bookmarklet </lift/exp-builder/access>`__.
   The |acquia-product:cha| sidebar will appear.
#. In the sidebar, click the **Create** tab.

   |Create tab|

#. | Click the **Content** tab, and then enter your search criteria in
     the **Search for Content** field.

   |Content tab|

#. Click the magnifying glass |Search| in the field to search.
   |acquia-product:cha| displays a list of search results as thumbnail
   images with titles. These images represent pieces of content,
   including content imported from |acquia-product:ch|.
#. Click **Filter** to display the Filter & Search Content dialog box,
   and use the following fields to refine your search results:

   -  **Keywords**
   -  **Sources** list
   -  **Tags** list
   -  **Content Type (comma separated)**
   -  **Date(s)**

#. | Click **Filter Content**.

   .. note::  

      To learn more about saving and reusing filters, see `Managing filters
      in |acquia-product:cha| </lift/exp-builder/rule/filters>`__.

#. To display any available slots with a blue border to help you find
   them more easily on your website, enable the **Highlight Slots**
   feature.

   |Slider to highlight slots|

#. Set your active `segment </lift/profile-mgr/segment>`__. You can
   choose to apply a rule to a particular segment by selecting a segment
   from the **Set Active Segment** list at the top of the
   |acquia-product:cha| sidebar. By default, this segment is set to
   **Everyone**, which means that all the visitors to your website fall
   into this segment. The segment that you select from this list will
   allow you to preview the current webpage as a visitor from that given
   segment. You can also modify the segment of a rule after creating it.
   For information about creating additional segments, see `Managing
   your site's segments </lift/profile-mgr/segment#adding>`__.
#. In the **Algorithm** list, click the method that you want to use for
   recommending content:

   -  **Most recent content** – Displays the newest content
   -  **Most viewed content** – Displays the most popular content
   -  **Similar to current content** *(private beta)* – Displays the
      content most similar to the currently displayed content
   -  **Similar to previously viewed** *(private beta)* – Displays the
      content most similar to pages previously viewed by the visitor

   .. admonition::  Private beta access

      For access to the algorithms available through private beta, contact
      your Account Manager.

#. | Click the piece of content that you want to add to your rule, and
     then drag it to the slot where you want to place it.
   | |acquia-product:cha| displays the slot with a yellow border and the
     message **New Rule**. If there are rules already present in the
     slot, |acquia-product:cha| displays these rules in a dialog box
     after you drag the piece of content into the slot. When you add the
     content to the slot, |acquia-product:cha| displays the following
     options in a dialog box:

   -  **Create a new Rule** – Add a new rule with the added content
   -  **Replace content** – Replace the content in an existing rule
   -  **Create A/B Test** – Create an A/B test rule from an existing
      targeting rule
   -  **Add to test** – Add the content to an existing testing rule

   Only the rules for the segment currently selected will be displayed
   while you drag the piece of content over to it, and only unpublished
   rules can be modified.

   .. note::  

      By default, if there is existing (static) content in the slot, the
      content will display even when slot highlighting is enabled, and will
      include only the slot controls. After adding a rule, the rule details
      are added to the controls.

After you have selected an option from the dialog box, your content
displays in the slot. A default click-through
`goal </lift/profile-mgr/goals>`__ is created when the content is added
to the slot.

|acquia-product:cha| displays the following elements for the slot:

|Slot display|

-  **Slot name (X/Y)** – |acquia-product:cha| displays the name of the
   slot and **(X/Y)**, where X is the number of rules for the particular
   segment selected in the **Set Active Segment** and Y is the total
   number of rules in the slot. These numbers change to indicate that a
   rule has been added to this slot. For example, if there is one rule
   for this particular segment, and the total number of rules in this
   slot is one, the name **slot name 1/1** displays. Point to the slot
   name to display a dialog box containing the number of rules for this
   particular segment and the total number of rules in the slot.
-  **Expand slot** – This expands the slot to display all the rules that
   exist in the slot, allowing you to manage and prioritize the order in
   which they are shown.
-  **Layout** – This changes the display of content based on the view
   mode associated with the content. |acquia-product:ch| imports view
   modes, such as teasers, which can be used in slots. The preview will
   automatically update when a new view mode is chosen. Numbers will be
   displayed if there are three or fewer view modes. Point to **Layout**
   to display a small preview of the content in that view mode. If there
   are more than three view modes, this switches to a list.
-  **Dialog box** – |acquia-product:cha| displays a dialog box with the
   message **Rule Created!**
   This dialog box lists the following information for this rule:

   -  **Type of rule** – This indicates whether this rule is a `testing
      or targeting rule </lift/drupal/personalization-types>`__. If this
      is a targeting rule, |acquia-product:cha| displays a target icon.
      If this is a testing rule, |acquia-product:cha| displays a pie
      chart icon.
   -  **Rule name** – This is based on the title of the content used. If
      content is used in the same slot multiple times, the rule name is
      enumerated. For example, if you use content entitled **My dog**,
      which creates a rule, and then add it a second time, the new
      rule's default name will be similar to **My_dog_1**.
   -  **Segment to which the rule applies** – This indicates the group
      of website visitors to which the content in this rule will be
      shown.
   -  **Slot this rule is in** – The name of the slot to which the rule
      applies.

Modifying rule names
--------------------

By default, targeting rules will assume the name of the content that
they contain.

A testing rule, also known as an A/B test, will assume a name in the
format **{segment} A/B Test {number}**, where **{segment}** is the name
of the segment to which the content in the rule will be shown, and
**{number}** is the number of tests that have been created.

For example, the default name for the second A/B test for first-time
visitors could be **First-time visitors A/B Test 2**.

You can modify these names by completing the following steps:

#. Click the **Rules** tab.
#. Click the 3 vertical dots in the rule that you want to modify.
#. Click **Configure**.
#. In the **Rule name** field, enter the new name for this rule.
#. Click **Save**.

.. |Create tab| image:: https://cdn4.webdamdb.com/1280_s4eaMwVIn576.png?1526475537
   :width: 414px
   :height: 158px
.. |Content tab| image:: https://cdn3.webdamdb.com/1280_3qAeFQi02.png?1526476123
   :width: 407px
   :height: 153px
.. |Search| image:: https://cdn3.webdamdb.com/1280_gkj6T9cHJgu3.png?1526475606
   :width: 28px
   :height: 29px
.. |Slider to highlight slots| image:: https://cdn4.webdamdb.com/1280_6BaxHnbNNa74.png?1526475799
   :width: 111px
   :height: 28px
.. |Slot display| image:: https://cdn3.webdamdb.com/1280_QYGhe8uXpu54.png?1526475822
   :width: 335px
   :height: 102px
