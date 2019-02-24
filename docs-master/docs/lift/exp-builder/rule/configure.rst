.. include:: /common/global.rst

Configuring and prioritizing rules
==================================

Rules can be configured and managed from both the Rules tab and by
expanding individual slots. On any rule card, clicking the three dots
opens the Rules menu. In the Rules menu, you can take the following
actions:

|Rule card options|

-  **Preview** - Allows you to preview the rule as it would appear on
   the page. If the rule is an A/B test, you can select which piece of
   content in the A/B test you wish to preview
-  |configure|_ - Expands the rule card to configure
   different settings of the rule
-  **Report** - Expands the rule card to show its report. Learn how to
   `read rule reports </lift/exp-builder/rule/reports>`__
-  **Publish/Unpublish** - Changes the status of your rule to published
   or unpublished depending on the rule’s current state
-  **Delete** - Deletes the rule from |acquia-product:cha|

.. |configure| replace:: **Configure**
.. _configure: /configure

Configure
---------

Clicking **Configure** in the rule menu expands the card to display the
following three tabs which enable users to modify the rule.

Content
~~~~~~~

This tab contains a list of the content to be shown for this rule. A
targeting rule will display a single piece of content, while a testing
rule will show two or more pieces of content.

|Configuring the rule content|

Each rule displays a thumbnail of the content, the rule name, and the
**Layout** used by this rule. Users can preview individual content items
on the page by clicking the **Preview** link next to each content item.

Goals
~~~~~

A `goal </lift/profile-mgr/goals>`__ is a specific objective created for
visitors to your website. `Adding goals to a
rule </lift/profile-mgr/goals>`__ allows |acquia-product:cha| to track
whether these goals are met when the rule is shown to visitors. To
create a new goal in |acquia-product:lpm|, click the **Goals** tab. By
default, a click-through goal is created for every rule.

|Adding a goal to a rule|

To add additional goals to a rule:

#. On the appropriate rule card, click the **+Add goal to rule** link.
   |acquia-product:cha| displays an additional goal list.
#. In the goal list, click a new goal.
#. Remove any obsolete goals by clicking the **Remove goal** link next
   to each goal.
#. Click **Save** to save your changes.

Settings
~~~~~~~~

The **Settings** tab enables users to modify the name of the rule and
the segment to which it applies. Additionally, if the rule is a testing
rule, users can modify the testing distribution for each content item.

|Changing rule settings|

Rule names
^^^^^^^^^^

When a rule is created, it inherits the name of its content item. Rules
can be renamed at any time, but a rule name must be unique to the
individual slot it exists within. For example, you can have two rules in
two different slots with the name **Test rule** but you cannot have two
rules named **Test rule** in the same *slot*. To change a rule name,
enter the new name in the **Rule name** text box, and then click
**Save**.

Rule segments
^^^^^^^^^^^^^

The rule's target segment can be changed using the segment selection
list. Segments can be `created and
managed </lift/profile-mgr/segment>`__ in |acquia-product:lpm|. To
change the segment, select the segment you wish to target in the
**Segment** list and then click **Save**.

A/B testing
^^^^^^^^^^^

If the rule is a testing rule, there will be a section at the bottom of
the Settings tab listing the different content items and their testing
distribution. By default, all testing rules inherit an even testing
distribution between their content items. To change this testing
distribution, complete the following steps:

#. Click **Custom** next to the **Testing Distribution** label. This
   activates the text boxes next to each content item.
#. After the text boxes are active, enter a
   ``percentage (%) distribution`` of your choice for each content item.
   The sum of each content items percentage must equal 100%.
   |acquia-product:cha| displays an error if this is not the case.
#. You can switch the distribution back to an even split by clicking the
   **Even** heading next to **Testing Distribution**.

Once your percentages are set, click **Save**.

Prioritizing rules
~~~~~~~~~~~~~~~~~~

Rules are prioritized on a per-slot basis. Prioritizing rules determines
which rules should show ahead of others when more than one rule exists
within a slot.

To prioritize the rules in a slot, click the slot to activate its slot
controls, and then click **Expand Slot**.

|Expand the slot|

The slot expands to a full-screen window and lists all the rules that
exist within the slot, regardless of the rule's targeted segment.

The rules in the slot are prioritized in the list from top to bottom.
|acquia-product:cha| will compare the user's profile to the available
rules, and offer the user content for the first rule that matches their
profile. For example, if a user does not fall into the segment of the
first published rule in the list, their profile is compared to each
successive rule, and matched with the next published rule in the list
that matches their assigned segment.

|Prioritizing rules|

To change the priority of a rule, click the dots on the left side of the
rule card and drag the rule card to the location in the list where you
want the rule.

.. note::  

   Rules targeted toward the ``Everyone`` segment are shown to all website
   visitors. If a published rule using the ``Everyone`` segment is
   prioritized above other published rules in the slot, it always displays
   to all visitors.

.. |Rule card options| image:: https://cdn4.webdamdb.com/1280_sdpGhTmGacV5.png?1526475532
   :width: 390px
   :height: 165px
.. |Configuring the rule content| image:: https://cdn3.webdamdb.com/1280_kNGrv0HFFQ94.png?1526475968
   :width: 392px
   :height: 441px
.. |Adding a goal to a rule| image:: https://cdn2.webdamdb.com/1280_2u2sPipqOHi6.png?1526475691
   :width: 390px
   :height: 466px
.. |Changing rule settings| image:: https://cdn4.webdamdb.com/1280_QVdiQer0Yd11.png?1526475464
   :width: 393px
   :height: 567px
.. |Expand the slot| image:: https://cdn4.webdamdb.com/1280_kBtrsHuNinv5.png?1526475894
   :width: 547px
   :height: 279px
.. |Prioritizing rules| image:: https://cdn2.webdamdb.com/1280_US3CitgXWq76.png?1526476130
   :width: 590px
