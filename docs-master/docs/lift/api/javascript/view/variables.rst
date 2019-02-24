.. include:: /common/global.rst

Capturable variables for JavaScript API
=======================================

The various capture methods used by |acquia-product:cha| can be modified
based on your website's needs by replacing the following variables:

-  ``<category>`` - The event descriptor that you want to associate with the page
   view. For more information about creating categories for your use,
   see `Creating and managing
   events </lift/profile-mgr/event/category>`__.
-  ``<parameter>`` - An information type that collects additional custom data about
   an event, such as the length of a video that was viewed. Commonly
   used parameters include the following:

   -  ``author`` - Author of a piece of content a visitor viewed
   -  ``content_keywords`` - Maps to a Drupal keyword taxonomy when the
      |acquia-product:cha| Drupal module is used
   -  ``content_type`` - Content-type to which a piece of visitor-viewed
      content belongs
   -  ``content_title`` - Title of a piece of content a visitor viewed
   -  ``content_section`` - Section or category associated with a piece
      of content (for example, ``technology``)
   -  ``site_id`` - Your websites that use |acquia-product:cha| (for
      more information, see `Customer
      sites </lift/profile-mgr/customer-sites>`__)
   -  ``engagement_score`` - Number that you have chosen to signify the
      importance of a visitor's interest in this event (for example,
      viewing a webpage might have an engagement score of 1, and viewing
      a webinar might have an engagement score of 20)
   -  ``page_type`` - Category of page the visitor viewed (examples
      include ``article page``, ``tag page``, and ``home page``)
   -  ``persona`` - User-defined category into which a visitor fits,
      based on their viewing of particular content
   -  ``post_id`` - Unique identifier for a piece of content (for
      example, ``10000324``)
   -  ``published_date`` - Date and time that a piece of content was
      published

   Although each parameter can have only a single value, you can include
   multiple parameters to provide additional values, separating each
   parameter and value pair by commas.

   You can also enter parameters that are based on the following
   user-defined fields that are made available by |acquia-product:cha|
   (where ``<i>`` is the user-defined field you want to use, such as
   ``touch_udf3``):

   -  ``person_udf`` - User-defined field for a person, with up to 50
      fields for values
   -  ``touch_udf`` - User-defined field for a touch, with up to 20
      fields for values
   -  ``event_udf`` - User-defined field for an event, with up to 50
      fields for values

   .. note::  

      |acquia-product:cha| also includes an additional method called
      ``identity`` that also accepts parameters. Using this method allows
      you to send additional information about the website visitor along
      with the page view to |acquia-product:cha|. For information about
      using the ``identity`` method, see `Capturing visitor identity
      information </lift/javascript/identity>`__.

-  ``<value>`` - The value that you want to assign to a parameter.

For more information about parameters, see the Field Layouts section of
the `|acquia-product:ldb| </lift/omni>`__ documentation.
