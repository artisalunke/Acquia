.. include:: /common/global.rst

Viewing a visitor's profile summary
===================================

.. container:: internal-navigation

   **Profile Manager Person detail**

   * :doc:`Intro </lift/profile-mgr/person>`
   * Summary
   * :doc:`Insights </lift/profile-mgr/person/insights>`
   * :doc:`Activity </lift/profile-mgr/person/activity>`
   * :doc:`Details </lift/profile-mgr/person/profile-details>`


On a visitor's **People > Person detail** page, the panel on the left
displays profile summary information for the visitor.

|lift-web-people-summary .png|

The profile summary includes the following information:

-  **Status** - Whether the visitor is an **Anonymous User** or
   **Identified User** of the website. Identified users have provided
   identifiers (such as an email address or Facebook ID) to your
   website. Anonymous users have not provided any identifiers to your
   website.
-  **Tracking ID** - Each visitor is assigned a unique tracking ID which
   is stored in a cookie when they visit your website, so that their
   activity can be recorded
-  **Identifiers** - If the visitor is an identified user, this field
   displays their identifiers, which are used to identify and track
   visitors to your website (such as account IDs, tracking IDs, or other
   pieces of trackable identity information). If the visitor is an
   anonymous user, |acquia-product:lpm| does not display this field,
   because anonymous users do not have any identifiers.
   For both a list of the default identifiers and how to create
   additional custom identifiers, see `Updating your customer
   details </lift/profile-mgr/admin/customer>`__.
-  **Persona** - You can assign one or more personas to each item of
   content on your website. This field displays the persona that the
   visitor viewed most frequently — for example, if the visitor viewed
   one piece of content tagged with the persona **Foodie** and three
   pieces of content tagged with the persona of **Hiker**, this field
   will display the **Hiker** persona.

   .. note::  

      If |acquia-product:cha| does not yet have enough information about the 
      visitor to assign them a persona, |acquia-product:lpm| will not display 
      the **Persona** field.

-  **Engagement Score** - Indicates the visitor's depth of interaction
   with your website. which can be based on the following attributes:

   -  The number of pages visited
   -  The visitor has accessed specific pages that you have assigned
      more engagement value
   -  The visitor may have performed an action, such as subscribing to a
      newsletter

   This field displays the sum of all the engagement scores for this
   visitor's events across all of your customer sites in the past 90
   days.

   .. note::  

      When an `identity merge <#capture>`__ occurs and a pre-existing
      visitor’s identifier is added to an already existing visitor profile
      (the visitor who has the identifiers added to their profile is
      referred to as the *person of record*), |acquia-product:cha| adds the
      engagement score for that pre-existing visitor to the person of
      record’s engagement score, and then displays the calculated total as
      the new engagement score for the person of record.

-  **Last Seen** - The time of the visitor's last action on your
   website, measured in hours.
-  **First Seen** - The time of the visitor's first action on your
   website, measured in hours.


Interpreting capture-related error messages
-------------------------------------------

Sometimes |acquia-product:lpm| displays error messages in the **Person
Details** section when you view a particular visitor's details. These
messages are due to a merge failure, which is a processing problem that
can occur during a visitor capture. Merge failures happen when one
website visitor has more than 25 identifiers. Visitors often have
several identifiers — if a visitor logs into your website from a
different browser or signs in with a different email address, this
action will generate a new identifier. If a visitor has more than 25,
instead of the 26th identifier being merged to the same website visitor,
the |acquia-product:lpm| service will generate a new tracking ID and
merge the 26th identifier to that tracking ID. This helps prevent the
|acquia-product:lpm| service from experiencing performance issues
related to too-large visitor profiles.

These errors do not affect how |acquia-product:lpm| works, other than
improving its performance. You do not need to take any action related to
these messages, other than investigating why |acquia-product:lpm| might
be creating overly large visitor profiles.

More information
----------------

For more information about this visitor's behavior and activities on
your website, see `Examining visitor
information </lift/profile-mgr/person>`__.

.. |lift-web-people-summary .png| image:: https://cdn2.webdamdb.com/1280_od2H8tSlAOK4.png?1526475798
   :width: 590px
   :height: 316px
