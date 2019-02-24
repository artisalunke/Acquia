.. include:: /common/global.rst

Creating and managing goals
===========================

A *goal* is an event in |acquia-product:cha| that is used to measure the
effectiveness of a `rule </lift/exp-builder/rule>`__. A goal is
triggered when a decision from a rule, which shows a particular piece of
content, results in an event. Events can include actions such as a user
completing a form, landing on a page, clicking on a page element, or
purchasing an item.

To create a goal, |acquia-product:cha| determines each new inbound
event's eligibility to be a goal. A goal is created when the following
set of conditions is met:

-  The event is associated with a goal
-  That goal is tied to a rule
-  That rule triggered a decision within 72 hours for a given visitor
-  A goal has not been previously awarded for the rule to that visitor

For example, you can create an event *Purchase*, which is associated
with a goal **Purchased annual subscription**, which is tied to a rule
where a user is shown content intended to convince them to make a
purchase. The goal is met if the user makes the purchase within 72
hours.

The goals are then used in reporting to help you understand which
content variations perform better than others.

.. container:: message-status

   |Learning Services logo|\ For a step-by-step video tutorial introducing you 
   to personalization with |acquia-product:cha|, including creating goals, 
   see |tutorial|_

.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px

.. |tutorial| replace:: Creating Personalized Experiences with \ |acquia-product:cha|\ 
.. _tutorial: /tutorials/creating-personalized-experiences-acquia-lift


Managing your goals
-------------------

To manage your goals, or to make changes to your current goals, 
`sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm| interface,
and then click the **Goals** tab.

The Goals page displays options for actions you can take with your
available goals.

-  **Find** - Enter your search criteria in the **Find Goals** text
   field. This can be filtered by selecting a **Customer Site**. Click
   **Find** to search.
-  **Add** - `Add <#add>`__ a new goal.
-  **Edit** - Select **Edit** to change a current goal.
-  **Delete** - To delete a goal, click **Delete** next to the goal you
   want to remove.

By default, the first rule created for a slot automatically creates a
click-through goal, so there will always be at least one goal for every
slot with rules. This click-through goal has a value of ``1``.

Adding new goals
----------------

To add a goal, complete the following steps:

#. `Sign in </lift/drupal/web#signing>`__ to the |acquia-product:lpm| interface, 
   and then click the **Goals** tab.
#. Click the **Add new goal** link.
#. Enter values for the following fields to provide details about the
   goal that you want to create:

   -  **Goal Name** - Enter a name for the goal, such as ``Purchased 1-year subscription``.
   -  **Goal ID** (hidden by default) - This field contains the machine name of 
      the goal, which is based on the **Goal Name** that you enter. To view this 
      field and make changes to the default **Goal ID**, click the 
      **Edit Goal ID** link.
   -  **Description** - Enter a brief explanation of the goal, such as ``Purchased 1-year subscription for service``.
   -  **Value** - Enter the value attributed to the goal, which can be used to designate the relative weight of one goal to another.
      Alternatively, this can be used to directly track the dollar ($)
      value of the goal. This dollar value can be passed dynamically,
      using the goal’s associated event. For example, you could have the
      ``Purchased 1-year subscription`` goal value set to ``$50``, and a
      different goal like ``Purchased monthly subscription`` set to
      ``$5``.

#. In the **Customer Sites** list, select one or more customer sites to
   which to add the goal. By default, the **Apply Goal to all customer
   sites** check box is selected. Clear this check box to apply the goal
   to only the customer sites that you have selected.
#. To add an `event </lift/offers/event/category>`__ to the goal,
   complete the following steps:

   a. In the **Events** section, in the **Select customer site** list,
      click the site that you want to use.
   b. In the **Select an event** list, click an available event from the
      list. This list contains one or more events that can be associated
      with a goal. If an event is triggered, the |acquia-product:cha|
      service will examine all of the matching goals and then determine
      if a corresponding rule was triggered to show a piece of content
      to a user.
   c. Click **Add**.

#. Click **Save** to save your new goal.

`Rules are associated with goals </lift/exp-builder/rule>`__ in
|acquia-product:lpm|. After you have added goals to the rules that you
created, you have all of the necessary elements to provide customized
experiences for your users and track their responses.
