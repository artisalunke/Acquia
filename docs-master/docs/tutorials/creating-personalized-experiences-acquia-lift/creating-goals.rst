.. include:: /common/global.rst

Creating Goals
===================

.. container:: message-status

   Creating Personalized Experiences with |acquia-product:cha| – |Back to intro|_ |br| 
   Previous lesson – |Previous lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/creating-personalized-experiences-acquia-lift

.. |Previous lesson| replace:: Creating Rules
.. _Previous lesson: /tutorials/creating-personalized-experiences-acquia-lift/creating-rules


Lesson Goal
-----------

.. container:: message-status
   
   Create a smart success measure to guide future changes.

A Goal is a discrete action we want our visitors to take after they view
a personalization or A/B test. This measures the effectiveness of your
Rule.

.. note::  

   In order to track an action as outlined in this lesson, a developer must
   first create an `Event </lift/offers/event/category>`__ using 
   `Google Tag Manager </lift/profile-mgr/gtm>`__.

Think of a Goal as a conversion like a visitor clicking the “Add to
Cart” button. Following our example, we want to know if the personalized
banner results in the customer clicking through for more information on
a future sale.

#. `Sign in </lift/drupal/web#signing>`__ to the |acquia-product:lpm| 
   interface, and then click the **Goals** tab. 
   
   |Part 2 of Directions|

#. Click the **Add new goal** link.
#. Enter values for the following fields to provide details about the
   goal you wish to create:

   -  **Goal Name** - Enter a name for the goal, such as "Clicked
      Banner"
   -  **Description** - Enter a brief explanation of the goal, such as
      "Clicked Banner as Boston Returning Visitor"
   -  **Value** - A goal should associate a number for key comparisons.
      In this example, we care about engagement and will follow clicks

#. In the **Customer Sites** list, select one or more customer sites to
   add the goal. By default, the **Apply Goal to all customer sites**
   check box is selected. Clear this check box to apply the goal to only
   this customer site selected.
#. In order to ensure the discrete action a user takes is tracked as a
   Goal, we must add an event to the goal. Ensuring your developer has
   created an event, complete the following steps:

   -  In the **Events** section, in the **Select customer site** list,
      click the site that you want to use.
   -  In the **Select an event** list, click an available event from the
      list. This list contains one or more events that can be associated
      with a goal.
   -  Click **Add**.

#. Click **Save** to save your new goal.

Congratulations, you have created a Goal and applied it to a Rule to
measure your success and future changes.

Now let's add the goal to a report.

|Part 3 of Directions|

#. Log into |acquia-product:leb| on your website
#. Click **Rules**.
#. Click on the **3 dots** next to any displayed Rule.

   -  Then select **Configure**

#. Click on the **Goals** section.
#. Click **Add Goal to Rule**.
#. Under the drop down, you should now see the "Clicked Banner" goal you
   created in |acquia-product:lpm|.
#. Select the goal.
#. Click **Save**.

Congratulations! You have successfully created a personalization to push the right content, to the right audience, at the right time, and ensured your effectiveness with |acquia-product:cha|.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. |Part 2 of Directions| image:: /sites/docs.acquia.com/files/inline-images/CreatingGoals2-optimize.gif
.. |Part 3 of Directions| image:: /sites/docs.acquia.com/files/inline-images/CreatingGoals3-optimize-resize.gif

