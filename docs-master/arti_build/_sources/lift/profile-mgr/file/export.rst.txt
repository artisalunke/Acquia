.. include:: /common/global.rst

Exporting visitor information
=============================

Although |acquia-product:lpm| allows you to view information about your
website visitors as you serve them personalized content, you can track
many other pieces of information about your visitors, across many
different applications. You may already have a business analytics
application that allows you to combine information about your visitors
and customers to draw better insights about their behaviors. You can
create export files of recent |acquia-product:lpm| visitor information
that you can later use in your applications.

Export files can contain up to 31 days of visitor data, consisting of
their person, event, and touch information. These files are saved to
your assigned Amazon S3 directory.


Creating an export file
-----------------------

To create a visitor information export file, complete the following
steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface as an administrator, and
   then click the **Admin** tab.
#. Click the **Bulk file management** link.
#. At the bottom of the webpage, click **Export data**.
#. In the **From** field, select a beginning date for the information in
   the export file. The export file will contain all selected
   information from the current date to midnight of the beginning date
   that you select.

   .. note::  

      You cannot select dates more than 31 days in the past.

#. In the **Data Exports** section, select one or more of the following
   check boxes to determine which information to export:

   -  **Person** - Visitors that have been uniquely identified with
      first-party cookies, their email addresses, or some other
      identifier.
   -  **Touch** - A series of contiguous events (such as content views)
      with a duration between events of no more than 30 minutes.
   -  **Event** - Discrete visitor actions, such as a content view of an
      article or a click-through on a subscription offer.
   -  **Rankings** - Links to the Person, Touch, and Event tables
      separated by metadata classifications. For example, the
      person_ranking table can track how many times a person has
      accessed a webpage by platform.
   -  **Matched Segment** - A list of the events and segments that are
      associated with each segment, linking the Segments table to the
      Event table.
   -  **Segment** - A list of the segments defined in the
      |acquia-product:cha| service, synchronized with the configuration
      database.

#. In the **Identifier Types** section, select one or more of the
   following check boxes to limit the export file's results to display
   information from only visitors with the selected identity properties:

   -  **Purged** - Displays results for visitors with an associated
      tracking ID that has been purged from the database.
   -  **Email Address** - Displays results for visitors with an
      associated email address.
   -  **Tracking ID** - Displays results for visitors with an associated
      tracking cookie ID.
   -  **Account ID** - Displays results for visitors with an associated
      account ID, which can be an identifier from another tracking
      system.
   -  **Facebook ID** - Displays results for visitors with an associated
      Facebook username.
   -  **Twitter ID** - Displays results for visitors with an associated
      Twitter username.
   -  **Name** - Displays results for visitors with an entered name,
      including first, middle, last, or any combination of these.

   .. note::  

      The Identifier Types section also includes any `custom identifier
      types </lift/profile-mgr/admin/customer>`__ that you have added to
      the customer.

#. Click **OK**.

|acquia-product:lpm| begins to export your requested information.
Depending on your selections in the **Data Exports** section, the
|acquia-product:cha| service will create a file for each export option,
with filenames that include the selected option.

The Bulk File Management webpage will update the list of files with each
of the new **Pending** export files. The export file creation process
can take some time to complete.

To refresh the list of files and their statuses, click **Find** on the
webpage.

.. note::  

   Entering values in the fields at the top of the page can limit the
   displayed file results. If your export file is not displayed on this
   page after clicking **Find**, clear the filter fields at the top of the
   webpage, and then click **Find** again.

After the |acquia-product:cha| service completes an export file, it
changes the file's status to **Complete**, and you can download the
file.


Retrieving your export file
---------------------------

|acquia-product:lpm| saves completed export files to an Amazon S3
directory that is associated with your account. To download your export
file, complete the file retrieval steps described in `Amazon S3 file
management with |acquia-product:lpm| </lift/profile-mgr/amazons3>`__.

.. _examine:

Examining the export file
-------------------------

To ensure that other applications are able to read the export file's
data correctly, |acquia-product:lpm| adds escape characters ( ``\`` ) to
the export file. For more information, see `Amazon S3 file 
management </lift/profile-mgr/amazons3>`__ with |acquia-product:lpm|.
