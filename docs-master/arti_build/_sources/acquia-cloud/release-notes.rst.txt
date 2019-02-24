.. include:: /common/global.rst

Release notes - |acquia-product:ac|
===================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/release-notes/*

Looking for the latest and greatest new `features and changes to <https://www.acquia.com/products-services/acquia-cloud>`__
|acquia-product:ac|?
Read on and check back regularly to see what else we’ve done.

.. _20180607:

Acquia Cloud updates - June 7, 2018
---------------------------------------------
*Thursday, 7 June 2018* 

|acquia-product:ac| includes the following updates:

Changes
~~~~~~~
-  The |acquia-product:ac| pipelines feature enables synchronizing of databases
   from other environments to |acquia-product:ccd| environments.
-  The |acquia-product:ac| pipelines feature paginates the branch display.
-  Pushing a tag in the |acquia-product:ac| pipelines feature triggers a build.
-  XML can not be uploaded into support tickets. Place the XML in a ``.zip`` 
   file and attach that file to the ticket.

Fixed issues
~~~~~~~~~~~~
-  |acquia-product:ac| pipelines branches sometimes looped due to a webhook issue.

.. _20180518:

Acquia Cloud 1.108
-----------------------------------
*Friday, 18 May 2018*

|acquia-product:ac| includes the following updates:

**Release Schedule**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Platform
     - Release date
   * - |acquia-product:acs|
     - Wednesday, May 30, 2018
   * - |acquia-product:ace|
     - Wednesday, June 6, 2018
   * - |acquia-product:edg|
     - Wednesday, June 15, 2018

Although no subscriber actions are required for this release, you may notice momentary website traffic interruptions as PHP restarts.

Changes
~~~~~~~

-  The following `included software </acquia-cloud/arch/tech-platform>`__ was updated:
   
   -  PHP versions were updated to 7.1.17 and 7.2.5

-  Timeouts for websites behind balancers have been increased.
-  Cloned web servers will have identical volume sizes.
-  PHP 7.2 is now selectable for |acquia-product:acs| and |acquia-product:ace| 
   subscriptions. `Learn more </acquia-cloud/manage/php>`__. For information 
   about upgrading to PHP 7.2, see `Upgrading to PHP 7.2 
   </article/php-56-retirement-faq>`__.
    
   .. important::
    
      To use PHP 7.2, Acquia recommends Drupal 8.5 or greater.

Fixed issues
~~~~~~~~~~~~

-  Stack Metrics graphs for Varnish requests correctly show data.


.. _20180430:

Acquia Cloud updates - week of April 22, 2018
---------------------------------------------
*Mon, 30 Apr 2018* 

The |acquia-product:ac| platform includes the following update for the week of 
April 22, 2018 through April 28, 2018:

Change
~~~~~~

-  The |acquia-product:ac| pipelines feature now uses encrypted volumes for all of its functions.

.. _20180430:

Acquia Cloud updates - week of April 15, 2018
---------------------------------------------
*Mon, 23 Apr 2018* 

The |acquia-product:ac| platform includes the following updates for the week of 
April 15, 2018 through April 21, 2018:

Changes
~~~~~~~

-  The **Minimal installation profile** is again available in the 
   |acquia-product:ui| for your use.
-  The |acquia-product:ac| pipelines feature includes changes which will not affect users'
   experience with the product.

Acquia Cloud 1.107
-----------------------------------
*Monday, 16 April 2018*

|acquia-product:ac| includes the following updates:

**Release Schedule**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Platform
     - Release date
   * - |acquia-product:acs|
     - Thursday, April 26, 2018
   * - |acquia-product:ace|
     - Wednesday, May 2, 2018
   * - |acquia-product:edg|
     - Wednesday, May 9, 2018

Although no subscriber actions are required for this release, you may notice momentary website traffic interruptions as PHP restarts.

Change
~~~~~~~

-  The following `included software </acquia-cloud/arch/tech-platform>`__ was 
   updated:
   
   -  PHP versions were updated to 7.1.15 and 5.6.34

.. _20180416:

Acquia Cloud updates - week of April 8, 2018
---------------------------------------------
*Mon, 16 Apr 2018* 

The |acquia-product:ac| platform includes the following updates for the week of 
April 8, 2018 through April 14, 2018:

Change
~~~~~~~

-  The |acquia-product:ac| pipelines feature includes changes which will not affect users'
   experience with the product.

.. _20180402:

Acquia Cloud updates - week of March 18, 2018
---------------------------------------------
*Mon, 2 Apr 2018* 

The |acquia-product:ac| platform includes the following updates for the week of 
March 18, 2018 through March 31, 2018:

Changes
~~~~~~~

-  The Activity Stream indicator will not indicate busy status as frequently.
-  Users with the Administrator or Owner roles can view the |acquia-product:ui|
   `last login date </acquia-cloud/teams/members>`__ for a team member on the 
   organizational details page.
-  Environment cards now display which tag or branch is deployed to that environment.
-  Acquia's HMAC implementation no longer supports PHP 5.5.
-  The |acquia-product:ac| pipelines feature includes changes which will not 
   affect users' experience with the product.

Fixed issues
~~~~~~~~~~~~

-  The |acquia-product:ac| pipelines API sends more useful error messages when 
   encountering 500 errors due to missing user information.


Acquia Cloud 1.106
-----------------------------------
*Monday, 12 Mar 2018*

|acquia-product:ac| includes the following updates:

**Release Schedule**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Platform
     - Release date
   * - |acquia-product:acs|
     - Wednesday, March 21, 2018
   * - |acquia-product:ace|
     - Wednesday, March 28, 2018
   * - |acquia-product:edg|
     - Wednesday, March 4, 2018

Although no subscriber actions are required for this release, you may notice 
momentary website traffic interruptions as PHP restarts.

Change
~~~~~~~

-  The following `included software </acquia-cloud/arch/tech-platform>`__ was 
   updated:
   
   -  PHP versions were updated to 7.1.1 and 5.6.33

.. _20180402:

Acquia Cloud updates - week of February 25, 2018
-----------------------------------------------------
*Mon, 5 Mar 2018* 

The |acquia-product:ac| platform includes the following updates for the week of 
February 25, 2018 through March 3, 2018:

Change
~~~~~~

-  ClamAV was updated to version 0.99.3.

Acquia Cloud updates - week of February 18, 2018
-----------------------------------------------------
*Mon, 26 Mar 2018* 

The |acquia-product:ac| platform includes the following updates for the week of 
February 18, 2018 through March 24, 2018:

Change
~~~~~~

-  The |acquia-product:ac| pipelines feature removed support for the PHP s
   ``sha1_file`` function for security purposes.

Acquia Cloud 1.105
-----------------------------------
*Monday, 21 Feb 2018*

|acquia-product:ac| includes the following updates:

**Release Schedule**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Platform
     - Release date
   * - |acquia-product:acs|
     - Wednesday, February 28, 2018
   * - |acquia-product:ace|
     - Thursday, March 1, 2018
   * - |acquia-product:edg|
     - Wednesday, March 7, 2018

Although no subscriber actions are required for this release, you may notice 
momentary website traffic interruptions as PHP and Apache restart.

Changes
~~~~~~~

-  The following included software was updated:

   -  PHP versions were updated to 7.1.13 and 5.6.33
   -  New Relic was updated to 7.7.0.203
-  Node.js applications will experience less downtime during server reboots.
-  The Git origin will be pruned before fetching during code deployments.
-  Deletion of Acquia Cloud CD environments is more reliable.
-  The Apache version will no longer be displayed on 4XX errors.
-  Deployed Git branches or tags can no longer be deleted.
-  The Drush launcher now uses the application's site Drush version.
-  MySQL dump restores should be faster.

Acquia Cloud updates - week of February 11, 2018
------------------------------------------------
*Tue, 20 Feb 2018* 

The |acquia-product:ac| platform includes the following updates for the week of 
February 11, 2018 through February, 2018:

Changes
~~~~~~~

-  |acquia-product:ace| customers can now change their application's PHP memory 
   limits from the |acquia-product:ui|. 
   `Learn more </acquia-cloud/manage/php#php-mem>`__
-  The |acquia-product:ac| pipelines feature includes changes which will not 
   affect users' experience with the product.

Acquia Cloud updates - week of January 28, 2018
------------------------------------------------
*Mon, 5 Feb 2018* 

The |acquia-product:ac| platform includes the following updates for the week of 
January 28, 2018 through February 3, 2018:

Changes
~~~~~~~

-  Branches that are deployed to an environment can no longer be deleted.
-  The |acquia-product:ac| pipelines feature includes changes which will not 
   affect users' experience with the product.

Acquia Cloud updates - week of January 21, 2018
------------------------------------------------
*Mon, January 29, 2018*

The  |acquia-product:ac| product includes the following updates for the week of 
January 21, 2018 through January 27, 2018:

Changes
~~~~~~~

-  Stack Metrics graphs now display results more quickly.
-  Administrative usernames that contain the strings ``admin``, ``root``, and 
   ``administrator`` are required to have a minimum username length of 15 
   characters.

Fixed issue
~~~~~~~~~~~

-  The pipelines feature did not build properly from a forked Bitbucket 
   repository.

Acquia Cloud updates - week of January 14, 2018
-----------------------------------------------
*Tue, 16 Jan 2018*

Fixed issue
~~~~~~~~~~~

-  The pipelines feature did not build properly from a forked Bitbucket 
   repository.

Acquia Cloud updates - week of January 1, 2018
----------------------------------------------
*Mon 8 Jan, 2018*

The |acquia-product:ac| product includes the following updates for the week of 
January 1, 2018 through January 7, 2018:

Changes
~~~~~~~  
-  The |acquia-product:ac| pipelines feature can now trigger jobs from forked 
   BitBucket repositories.

Fixed issue
~~~~~~~~~~~

-  When switching environments in Acquia Insight, the displayed environment did
   not change.
