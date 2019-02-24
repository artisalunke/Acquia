.. include:: /common/global.rst

|acquia-product:cha| Push API reference
=======================================

.. container:: message-status

   This feature is available only to |acquia-product:cha| |acquia-product:ldb| subscribers.

The |acquia-product:cha| Push API allows you to receive information in
real time when a visitor to your website enters a segment in which
you're particularly interested. In the |acquia-product:lpm| interface,
you can enter an URL and associate specific segments to this location,
so that whenever a person enters those segments, a notification
containing information about the person, touch, event and matched
segments is sent to the URL that you have chosen.

.. note::  

   In addition to configuring the Push API in |acquia-product:lpm|, you
   will also need to set up a HTTP server to listen for notification
   messages (also called an *endpoint*). This setup will be different for
   different servers, but generally, you will open a port on a public
   domain and write a program to listen on that port. This program can be
   written in any language. Contact your service provider for more
   instructions on how to set up your server.


Using the Push API
------------------

The notification messages that the |acquia-product:cha| service sends to
an HTTP server will contain the following parameters:

.. list-table::
   :widths: 33 33 34
   :header-rows: 1 

   * - Parameter
     - Description
     - Example
   * - ``person``
     - Contains values for the fields in the `Omnichannel person table </lift/omni/person#person-table>`__
     - ``anonymous_visitor``, ``do_not_track``
   * - ``identifiers``
     - Contains values for the fields in the `Omnichannel person_identifier </lift/omni/person#person-identifier-table>`__ table
     - ``person_identifier_type_id``, ``person_id``
   * - ``touch``
     - Contains values for the fields in the `Omnichannel touch table </lift/omni/touch>`__
     - ``engagement_score``, ``number_of_page_views``
   * - ``event``
     - Contains values for the fields in the `Omnichannel event table </lift/omni/event>`__
     - ``keywords``, ``page_url``
   * - ``newMatchedSegments``
     - Contains values for the fields in the `Omnichannel matched_segment table </lift/omni/segments#matched-segment-table>`__
     - ``segment_id``, and all of the new segments the visitor has entered during this touch
   * - ``currentMatchedSegments``
     - Contains values for the fields in the `Omnichannel matched_segment table </lift/omni/segments#matched-segment-table>`__
     - ``segment_id``, and all of the segments the visitor was in before this touch, including segments the visitor reentered during this touch


Configuring the Push API
------------------------

To configure the |acquia-product:cha| Push API, complete the following
steps:

#. Sign in to the |acquia-product:lpm| interface, and then click the
   **Admin** tab.
#. Click the **Manage Configuration Data** link.
#. Click the **Push API** link.
#. Click the **Add new rule** link.
#. Configure the following settings:

   -  **Name** - Enter the name of the new rule you are creating.
   -  **Endpoint URL** - Enter the URL where you want the
      |acquia-product:cha| service to send notifications.
   -  **Description** - Enter a description of this particular push
      configuration for your own use.
   -  **Interval** - Enter a number that corresponds with your selection
      in the **Frequency criteria** field: for example, if you want to
      push notifications triggered by the same website visitor every
      four hours, enter ``4`` in this field.

      .. note::  

         If you select **event** or **touch** in the **Frequency criteria**
         list, you do not need to enter a number in the **Interval** field.

   -  **Frequency criteria** list - Select how frequently you want to
      push notifications to be triggered by the same website visitor:

      -  **event** - Receive notifications to your specified endpoint
         URL every time a visitor enters this segment.
      -  **touch** - Receive notifications to your specified endpoint
         URL only for the first a visitor enters this segment during a
         particular touch.
         A touch is a series of contiguous events (such as content
         views) with a duration between events of no more than 30
         minutes, and can can contain several events that are matched
         into the same segment. Choosing this option means that you will
         only receive a notification the first time an event in a touch
         matches a segment, and not when subsequent events in the touch
         match the segment.
      -  **minute** - Set how many minutes you want to elapse between
         each push notification triggered by the same visitor.
      -  **hour** - Set how many hours you want to elapse between each
         push notification triggered by the same visitor.
      -  **day** - Set how many days you want to elapse between each
         push notification triggered by the same visitor.
         If you select **minute**, **hour** or **day**, you will receive
         a push notification only if the visitor re-enters the segment
         after this timeframe; no push will be sent if the visitor
         re-enters the segment before the set time has elapsed. For
         example, if you set the frequency criteria to 10 minutes, you
         would not receive a push notification if the visitor re-enters
         the segment after eight minutes, but would receive a
         notification if it occurred after 12 minutes.

#. In the **Segment Triggers** section, in the **Select a segment**
   list, click the segment that you want to add to the **Segment
   Triggers** table.
#. Click **Add**.
   The segment name, ID, and description will appear in the **Segment
   Triggers** table.
   A segment trigger means that if a website visitor enters the segment
   you have defined as a trigger, the Push API sends a notification to
   the endpoint URL. For example, you can define as a trigger a segment
   in which a visitor views two pages on your website. In this case,
   whenever a visitor views two pages on your website, the
   |acquia-product:cha| service triggers a push notification to the
   endpoint URL.
#. Click **Save** to save this configuration.

The |acquia-product:cha| Push API will now begin sending notifications
to your endpoint URL.


Deleting a segment
------------------

To delete a segment from the **Segment Triggers** table, complete the
following steps:

#. Sign in to the |acquia-product:lpm| interface, and then click the
   **Admin** tab.
#. Click the **Manage Configuration Data** link.
#. Click the **Push API** link.
#. In the **Segment Triggers** table, in **Actions**, click **Delete**
   to the right of the name of your segment.
