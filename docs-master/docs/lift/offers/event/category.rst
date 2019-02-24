.. include:: /common/global.rst

Creating and managing events
============================

To help you understand how your website visitors interact with your
website and receive a personalized experience, your website sends your
website visitors' interactions (also known as captures) to
|acquia-product:cha|. Depending on your website's size and
implementation, you may have to attempt to evaluate many thousands of
these types of interactions.

|acquia-product:cha| includes descriptive containers called *events*
that you can use to compartmentalize your captures by a common theme
(such as Shares or Registrations) or conversion events (including
clicks).


Creating new events
-------------------

To create new descriptive events for the website visitor captures that
|acquia-product:cha| receives from your website, complete the following
steps:

#. `Sign in </lift/profile-mgr>`__ to the |acquia-product:lpm|
   interface, and then click the
   **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Events** link.
#. Click the **Add new event** link.
#. In the **Event Name** field, enter a descriptive name for the event
   that you want to monitor.
#. In the **Event ID** field, enter the machine name for the event.
#. In the **Customer Site** list, click the customer site to which you
   want this event to apply. Click **Global** to use this event across
   all your websites.
#. The **Event Type** list describes how visitors are interacting with
   your website.
#. Click **Save** to create the new event.


Managing your events
--------------------

To list and manage the events available for your use (including removing
those that you no longer want to use), complete the following steps:

#. `Sign in </lift/profile-mgr>`__ to the |acquia-product:lpm|
   interface, and then click the
   **Admin** tab.
#. Click **Manage configuration data**, and then click **Events**.
#. To view a filtered list of events, complete the following steps:

   a. Enter your search criteria in the **Find events** field. Leave
      this field empty to display all events.
   b. In the **Customer Site** list, click the customer site whose
      events you want to display. Click **Global** to list all your
      websites' events matching the search criteria in the **Find
      events** field.

#. Click **Find**.

To edit an existing event, click its **Event Name**, and then modify its
values as required. Be sure to click **Save** to save your changes.

To delete an event, find the event that you want to remove, and then
click its **Delete** link.

.. note::  

   Removing an event does not delete the captures associated with that
   event from |acquia-product:cha|.


Viewing reports based on events
-------------------------------

After you create a campaign and |acquia-product:cha| begins to receive
captures from visitors, you can use the **Person details** page to
display how many of those types of events |acquia-product:cha| is
receiving for a particular visitor.

To view information about all events that have been captured by
|acquia-product:cha|, go to the **Analytics** tab, and in the **Events**
report list, click the **Events by Events name** report.

Displaying filter settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

To display the report's filter settings, click the down arrow to the
right of **Filters**.

Limiting report results
~~~~~~~~~~~~~~~~~~~~~~~

To limit the report's results to those visitors who have one or more of
a particular event in their history, complete the following steps for
the **Event Name** field:

#. In the list of filtering options for the field, click the filter that
   you want to use — for example, click **Contains** to limit search
   results to visitors with events in their history that contain your
   search term.
#. In the empty field, enter the event name for which you want to
   search. Depending on what you enter, |acquia-product:lpm| will
   suggest website events that you can click.
#. If required, click the plus sign ( **+** ) to create additional event
   name filters.
#. After you have made all of your filter changes, click **Run**.

The report displays information about the event or events that you have
specified.
