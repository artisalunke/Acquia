.. include:: /common/global.rst

Create users programmatically
===================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: CAdd a field to an existing form
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/add-field-existing-form

.. |Next lesson| replace:: Update users programmatically
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/update-users-programmatically


Lesson Goal
-----------

.. container:: message-status

   Create a code snippet that can be used as a base to create new users programatically.

Implementation Method
---------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Drupal Version
     - Method
   * - Drupal 7
     - ``user_save()``
   * - Drupal 8
     - |usercreate|_

.. |usercreate| replace:: User::create()
.. _usercreate: https://api.drupal.org/api/drupal/core%21modules%21user%21src%21Plugin%21views%21argument_default%21User.php/function/User%3A%3Acreate/8.5.x



Drupal 7 method
---------------

Add the following function to the ``lotus.module`` file, being sure to
replace ````, ````, and ```` with the appopriate values for the user
account you want to create:

.. code-block:: php

    /**
    * Helper function to create a new user.
    */
    function create_new_user(){
      $newUser = array(
        'name' => '<username>', 
        'pass' => '<password>',  // note: do not md5 the password
        'mail' => '<email>', 
        'status' => 1, 
        'init' => '<email>',
      );
      // The first parameter is sent blank so a new user is created.
      $user = user_save(null, $newUser);

      drupal_set_message("User with uid " . $user->uid . " saved!\n");
    }

Drupal 8 method
---------------

Add the following function to the ``lotus.module`` file, being sure to
replace ``<username>``, ``<password>``, and ``<email>`` with the appopriate values for the user
account you want to create:

.. code-block:: php

    use Drupal\user\Entity\User;
    /**
    * Helper function to create a new user.
    */
    function create_new_user(){
      $user = User::create();

      //Mandatory settings
      $user->setPassword('<password>');
      $user->enforceIsNew();
      $user->setEmail('<email>');

      //This username must be unique and accept only a-Z,0-9, - _ @ .
      $user->setUsername('<username>');

      //Optional settings
      $language = 'en';
      $user->set("init", 'email');
      $user->set("langcode", $language);
      $user->set("preferred_langcode", $language);
      $user->set("preferred_admin_langcode", $language);
      $user->activate();

      //Save user
      $user->save();
      drupal_set_message("User with uid " . $user->id() . " saved!\n");
    }

Gist Link
---------

https://gist.github.com/gargsuchi/2c26c1464e5f7f69c82a59980c0a1da0

Resources
---------

`User::create <https://api.drupal.org/api/drupal/core%21modules%21user%21src%21Plugin%21views%21argument_default%21User.php/function/User%3A%3Acreate/8.5.x>`__
