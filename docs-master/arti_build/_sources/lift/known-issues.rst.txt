.. include:: /common/global.rst

Known Issues in |acquia-product:cha|
====================================

This page describes known issues for |acquia-product:cha|. For a listing
of known issues for each component of |acquia-product:cha|, select from
the following list:

-  |issues-ch|_
-  |issues-leb|_
-  |issues-lpm|_


.. |issues-ch| replace:: Known issues in  \ |acquia-product:ch|\ 
.. _issues-ch: #hub

.. |issues-leb| replace:: Known issues in  \ |acquia-product:leb|\ 
.. _issues-leb: #expbuilder

.. |issues-lpm| replace:: Known issues in  \ |acquia-product:lpm|\ 
.. _issues-lpm: #profile

Applicable client versions for issues can be identified using the following icons:

-  |D8| – Applies to Drupal 8
-  |D7| – Applies to Drupal 7

.. _hub:

Known issues in |acquia-product:ch|
-----------------------------------

See also the list of `supported and unsupported modules </content-hub/modules>`__  for |acquia-product:ch|.

-  |D7| |D8| **No operability between Drupal 7 and Drupal 8 websites** |br|
   All websites in a |acquia-product:ch| installation must be on the same major version of Drupal.
-  |D8| **Content Hub client for Drupal 8 requires Drupal 8.4 or greater** |br|
   The |acquia-product:ch| client for Drupal 8 requires Drupal 8.4 or greater, and is not compatible with previous Drupal versions.
-  |D8| **The discovery page does not currently have a select-all option** |br|
   You must select one item of content at a time.
-  |D8| **Administrative users must ensure that they do not override the REST configuration entity types created by Content Hub** |br|
   Overriding these entities can remove saved |acquia-product:ch| filters.
-  |D8| **Webhook registration sometimes fails when saving** |br|
   *Workaround:* If this occurs, retry and it should eventually save.
-  |D8| **Websites using Content Hub must be fully HTTP or HTTPS** |br|
   Mixed-mode websites will experience difficulties when using any version of |acquia-product:ch|.
-  |D8| **Acquia Cloud Site Factory customers who clone content may encounter problems when attempting to publish the cloned content to Acquia Lift** |br|
-  |D7| |D8| **Password protection using .htaccess** |br|
   Websites using |acquia-product:ch| in development or staging environments that protect those environments using ``.htaccess`` password protection may have difficulties synchronizing content. To prevent issues, Acquia recommends that you whitelist both your webhook URL and the path. The path is based on your installed version of Drupal:

   -  *Drupal 8* - ``/acquia-contenthub/*``
   -  *Drupal 7* - ``content-hub/*``

   For information about using |acquia-product:ch| with the 
   `Shield <https://www.drupal.org/project/shield>`__ module, see 
   `Modules to use </content-hub/modules>`__ with |acquia-product:ch|.
-  | |D7| |D8| **Autosynchronization fails when entities in field collections have translations** |br|
   | Synchronization of content does not work properly when Field
     collections are enabled on publisher and subscriber
     |acquia-product:ch| websites, and where Entity translations are
     only in use on the publisher website. Field collections are not
     translatable `in all use cases. <http://cgit.drupalcode.org/field_collection/tree/README.txt#n30>`__

       The common use case is to leave the field collection field
       untranslatable and set the necessary fields inside it to
       translatable. There is currently a known issue where a host can
       not be translated unless it has at least one other field that is
       translatable, even if some fields inside one of its field
       collections are translatable.

   *Workaround:* Errors are partially handled in |acquia-product:ch|
   `release 1.11.0 </node/24386>`__, and |acquia-product:ch| indicates
   in the user interface that this configuration is not supported. Users
   may continue to experience problems when using translation and Field
   collections.

-  |D7| **Issue when editing filters for websites with large numbers of tags** |br|
   If you have a very large number of tags (800 or more), the filter
   controls may stop working when you save a filter.
   *Workaround:* Reload the content discovery page.
-  |D7| |D8| **Error when editing Views filters** |br|
   When you edit a saved filter in the |acquia-product:ch|, the filter
   controls may stop working. You may receive AJAX errors when using
   exposed filters.
   *Workaround:* Upgrade the `Views <https://www.drupal.org/project/views>`__ module to 7.x-3.13
   or greater. If you must continue to use Views version 7.x-3.11 with
   your website, apply the `patch <https://www.drupal.org/files/issues/views_with_exposed-1809958-28.patch>`__
   described in `issue 1809958 <https://www.drupal.org/node/1809958>`__
   on `drupal.org <https://www.drupal.org>`__.
-  |D7| |D8| **Valid webhooks fail to register** |br|
   If the server that is hosting the publishing or subscribing website
   is not keeping correct time, webhook registration can fail with the
   following error message:
   ``There was a problem trying to register Webhook URL [URL]. Error Code = 4005: The provided URL did not respond with a valid authorization.``

.. _expbuilder:

Known issues in |acquia-product:leb|
------------------------------------

At this time, no known issues with |acquia-product:leb| are available for reporting. If you encounter any difficulties with your |acquia-product:leb| subscription, `contact Acquia Support </support#contact>`__ for assistance.

.. _profile:

Known issues in |acquia-product:lpm|
------------------------------------

At this time, no known issues with |acquia-product:lpm| are available for reporting. If you encounter any difficulties with your |acquia-product:leb| subscription, `contact Acquia Support </support#contact>`__ for assistance.

.. |D8| image:: https://cdn3.webdamdb.com/1280_k33N7wQmFpp3.png?-62169955200
   :class: no-sb
   :width: 22px
.. |D7| image:: https://cdn2.webdamdb.com/1280_oqVDdWhUqFm0.png?-62169955200
   :class: no-sb
   :width: 22px
