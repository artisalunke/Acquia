.. include:: /common/global.rst

Release notes - Acquia DAM
==========================

Looking for the latest and greatest new features and changes to
|acquia-product:dam|? Read on and check back regularly to see what else we’ve
done.

.. _20180531:

Acquia DAM - May 31, 2018 release
----------------------------------
*Thu, 31 May 2018*

This release of the |acquia-product:dam| product and its components includes the following
updates:

Changes
~~~~~~~

- *Workstream* |--| Calendar now displays an increased number of tasks
- When converting ``EPS`` files, |acquia-product:dam| now uses your configured presets

Fixed issues
~~~~~~~~~~~~

- A dynamic template is no longer displayed once it has expired
- An asset expiration email was not always delivered to the recipient
- A permissions issue affecting the `cropping tool </dam/content/asset/edit>`__ was resolved
- The video asset count was not always accurate
- An issue navigating to `brand portal </dam/brand-connect/homepage>`__ from the
  main UI was fixed

.. _20180503:

Acquia DAM - May 3, 2018 release
------------------------------------------
*Thu, 3 May 2018*

This release of the Acquia DAM product and its components includes the following
updates:

Changes
~~~~~~~

-  The IPTC headline field now displays additional characters in the
   headline.
-  The cropping tool now additionally supports ``.tif`` and ``.tiff``
   files.
-  The following improvements have been made:

   -  Behavioral consistency triggering a download
   -  Password reset functionality

Fixed issues
~~~~~~~~~~~~

-  In some situations, image previews overlapped.
-  An issue was resolved downloading ``.ppt`` files.
-  A ``.png`` file was offered in the CMYK colorspace, when that format
   does not support CMYK.
-  When downloading a video preset using Google Chrome, an error
   condition occurred if the filename included both a space and a comma.
-  Color rendering did not always work with Google Chrome and Microsoft
   Internet Explorer.
-  When entering ``return`` in a field, the cursor would move to the
   beginning of the entry field.
-  Resolved discrepancies with the launch date between user roles.
-  When tagging a user in a comment through the guest asset viewer,
   Acquia DAM displayed an error message.
-  *Workstream* - Resolved duplicate in-application notifications to
   task requester.

.. _20180426:

Acquia DAM - April 26, 2018 release
---------------------------------------------
*Thu, 26 Apr 2018*

This release of the Acquia DAM product and its components includes the following updates:

Changes
~~~~~~~

-  The dynamic templates folder can now be renamed and moved in the
   folder hierarchy.
-  `Brand portal </dam/brand-connect/homepage>`__ search is improved.
-  The Acquia DAM interface was improved to make it easier to avoid
   implementation issues.
-  *Workstream* - Request Form settings now includes auto-notification
   and auto-assignee options.

Fixed issues
~~~~~~~~~~~~

-  Users could not sort audit logs at the folder level.
-  When generating reports, the start and end dates were not always
   working.
-  Approval paths did not work consistently with email addresses.
-  The following general issues were resolved:

   -  Downloading versioned assets that lack a preview image
   -  Saving metadata for large batches of assets

-  *Workstream-related fixed issues*

   -  Intermittent comment tagging behavior
   -  Project list UX

.. _20180417:

Acquia DAM Connector - 8.x-1.31 release
-------------------------------------------------
*Tue, 17 Apr 2018*

This release of the Acquia DAM Drupal Connector
(`download <https://www.drupal.org/project/media_acquiadam/releases/8.x-1.31>`__)
contains several changes and fixes, including support for Drupal 8.5.1.

For information about its specific changes, including Drupal.org issue
numbers, see the `connector release
notes <https://www.drupal.org/project/media_acquiadam/releases/8.x-1.31>`__.

.. _20180405:

Acquia DAM - April 5, 2018 release
--------------------------------------------
*Thu, 5 Apr 2018*

This release of the Acquia DAM product and its components includes the following updates:

Changes
~~~~~~~

-  A new configuration setting is included in the `user
   profile </dam/admin/users>`__: **Allow support to access your account
   for troubleshooting purposes**
-  The publishing interface now displays a *mixed* switch for a portal,
   if folders nested in a parent folder have a mixture of published and
   unpublished statuses.
-  Project names are now included in task notification emails.
-  *Workstream-related changes*

   -  Request forms now use the term *Activate* instead of *Publish*. An
      activated form is available for use.
   -  The email that Acquia DAM sends whenever tasks have been received
      now includes the information submitted by a user in the Workstream
      request form.

Fixed issues
~~~~~~~~~~~~

-  In some instances, Acquia DAM displayed the settings menu several
   times.
-  The **Uploaded by** metadata field was not being displayed.
-  Several issues regarding publishing were resolved.
-  Occasionally when using proofing, Acquia DAM displayed a HTTP Status
   500 error.
-  In certain situations, multiple approvals were displayed for an
   asset.
-  *Brand Connect* - Occasionally, `faceted
   search </dam/brand-connect/search#facets>`__ did not work.
-  *Workstream* - An issue with translations was resolved.

.. _20180308:

Acquia DAM - March 8, 2018 release
--------------------------------------------
*Thu, 8 Mar 2018*

This release of the Acquia DAM product and its components includes the
following updates:

Changes
~~~~~~~

-  Improved user experience when publishing subsections of a brand
   guideline.
-  Added native support for M4A audio files.
-  Improved performance for `Brand Connect </dam/brand-connect>`__
   portals with over 100,000 published assets.
-  Workstream

   -  `Approvals </dam/admin/approve>`__ now support an optional default
      path
   -  Approval warnings may have a custom time frame
   -  The API now offers high resolution RAW URLs
   -  Easier selection of future dates in the calendar
   -  Comments within `tasks </dam/workstream/tasks>`__ can now tag
      other users using ``@`` and the username

Fixed issues
~~~~~~~~~~~~

-  The user was not notified when publishing a subsection inside of an
   unpublished parent section.
-  When approving an asset, comments were not correctly submitted.
-  A guest user was unable to view the approval palette without
   authorization to view comments.
-  The user was not notified when an asset was being processed.
-  When viewing an asset's details, its approval status did not update
   correctly.
-  Rendering issues in Firefox and Internet Explorer were resolved.
-  When getting a direct download link for an audio asset, the links
   were incorrect.
-  Several display issues were fixed:

   -  Task lists displayed an incorrect time zone
   -  Address book entries without a full name displayed as ``()``
   -  Incorrect icons displayed for ``.ppt`` and ``.pptx`` embedded
      files
   -  Searching without any criteria displayed an "undefined" pill in
      the search filters

-  Large folders of assets did not load in certain situations.
-  Some video assets were not being processed.

.. _20180215:

Acquia DAM - February 15, 2018 release
------------------------------------------------
*Thu, 15 Feb 2018*

This release of the Acquia DAM product and its components includes the
following updates:

Changes
~~~~~~~

-  Performance and stability improvements in Acquia DAM, Brand Connect,
   and Workstream.
-  Workstream now displays in-app notifications.

Fixed issues
~~~~~~~~~~~~

-  In some cases, the Asset Expiration `API </dam/api>`__ replied with
   an incorrect response.
-  `Simple approval requests </dam/admin/approve>`__ created from the
   **Asset Details Action** bar failed to send.
-  Downloaded ``.TIFF``, ``.JPEG``, or ``.EPS`` files using the CMYK
   color scheme, were incorrectly converted to the RGB color scheme.
-  Previewing ``.PSD`` images using the aRGB colorspace failed.
-  An issue displaying some videos in Internet Explorer 11 was fixed.
-  FTP downloads of assets for a lightbox failed in some cases.
-  *Brand Connect* - An issue toggling visibility of
   `facets </dam/brand-connect/search>`__ was resolved.
-  When using large files with the `Box
   integration </dam/integrate/box>`__, an issue transferring files was
   fixed.
-  Redirects generated for `lightboxes from a Brand
   Portal </dam/brand-connect/homepage#lightbox>`__ were not always
   correct.

.. _20180208:

Acquia DAM - February 8, 2018 release
-----------------------------------------------
*Thu, 8 Feb 2018*

This release of the Acquia DAM product and its components includes the
following updates:

Changes
~~~~~~~

-  Admins can now batch download metadata for assets.
-  Brand Connect now displays more metadata fields by default.
-  Contributors can download inactive assets in Workstream.
-  Animated GIFs now display correctly when embedded with the Embed
   Links feature.
-  Sharing assets through the `Box </dam/integrate/box>`__ integration
   has been improved.

Fixed issues
~~~~~~~~~~~~

-  The following features received fixes in this release due to
   discovered issues:

   -  Authentication - Issues with `Shutterstock
      Premier </dam/integrate/shutterstock>`__ users
   -  Downloads By Time report

-  When following a direct link, previously signed in users were
   required to sign in again.
-  *Brand Connect issues*

   -  Asset counts displayed in a
      `lightbox </dam/brand-connect/lightbox>`__ did not reflect recent
      changes made in Acquia DAM.
   -  Rendering in Internet Explorer was sluggish in Brand Connect and
      Workstream.

-  *Workstream* - Rendering in Internet Explorer was sluggish

.. _20180125:

Acquia DAM - January 25, 2018 release
-----------------------------------------------
*Thu, 25 Jan 2018*

This release of the Acquia DAM product and its components includes the
following updates:

Changes
~~~~~~~

-  Multiple improvements to the publishing experience:

   -  Publish assets to your brand portal with a single click.
   -  Publishing and unpublishing can be done anywhere within the folder
      hierarchy.
   -  Improved visibility into the publication status of assets.

.. _20180110:

Acquia DAM Drupal 8.4 Connector - 8.x-1.2 release
-----------------------------------------------------------
*Wed, 10 Jan 2018*

This release of the Acquia DAM Drupal 8.4 Connector includes the
following updates:

Fixed issues
~~~~~~~~~~~~

-  When searching for assets, both inactive assets and folders that
   contained assets that met the search criteria were displayed
   alongside active assets.
-  Updates made to an asset in Acquia DAM were not synced to the Drupal
   instance.
-  Making updates to the Connector configuration would fail unless a new
   password and secret key were entered.
-  Cron updates did not always complete successfully.
-  Attempting to use an asset other than an image failed with an error
   message.
-  Configuring the Entity browser media type would fails and display an
   error message.

.. _20171207:

Acquia DAM - December 7, 2017 release
-----------------------------------------------
*Thu, 7 Dec 2017*

This release of the Acquia DAM product and its components includes the
following updates:

Changes
~~~~~~~

-  When using the bulk metadata tool, Acquia DAM now displays warnings
   regarding missing required fields.
-  *Workstream changes*

   -  Workstream's dialog boxes now use material design.
   -  The responsiveness of the `new task
      page </dam/workstream/tasks>`__ is improved.
   -  Error messages related to proofing account creation have been
      improved.
   -  On the Task Details page, Workstream no longer displays *due*
      information on the left of the page.
   -  Rendering is improved for Internet Explorer users.
   -  When adding approvers, Workstream sends a notification to the
      update API call.
   -  The performance of the **Manage > Preferences** page has been
      improved when using a large number of statuses.

Fixed issues
~~~~~~~~~~~~

-  The following features received fixes in this release due to
   discovered issues:

   -  Metadata templates - Issues with multi-select values
   -  `Box integration </dam/integrate/box>`__ - Data transfer issue
   -  `Watch </dam/access/alerts>`__ feature
   -  `Lightbox </dam/content/lightbox>`__
   -  Email customization
   -  Custom Downloads API

-  Compatibility issues with PHP 5.3 and PHP 5.6 were resolved
-  *Brand Connect issues*

   -  When clicking on an invalid link in an email, the user is
      redirected to the brand guidelines section page.
   -  The Cover image feature received fixes in this release due to
      discovered issues.

-  *Workstream* - When using the Approval Details page, items in the
   upper left corner now function properly.

.. _20171115:

Acquia DAM - November 15, 2017 release
------------------------------------------------
*Wed, 15 Nov 2017*

This release of the Acquia DAM product and its components includes the
following updates:

Changes
~~~~~~~

-  Rendering is improved for users of Microsoft Internet Explorer 11.
-  When `sharing a link to an asset </dam/content/asset/share>`__ as a
   signed out user, the asset path used is now shortener.

Fixed issues
~~~~~~~~~~~~

-  The link for resetting passwords did not work for some visitors.
-  *Workstream* - When using an `approval
   preview </dam/workstream/approval>`__, the correct versions of assets
   were not viewable.

