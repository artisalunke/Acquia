.. include:: /common/global.rst

Alter an existing simple form
=============================

| **Fast Track to Drupal 8 Coding** – *`Back to
  Intro </tutorials/fast-track-drupal-8-coding>`__*
| *Previous lesson – `Create a custom
  block </tutorials/fast-track-drupal-8-coding/create-custom-block>`__*  |  *Next
  lesson – `Build a new
  form </tutorials/fast-track-drupal-8-coding/build-new-form>`__*

Lesson Goal
-----------

Change the label of a comment form button to **Add Comment**.

Implementation Method
---------------------

Drupal Version

Method

Drupal 7

Use
`hook_form_alter <https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_form_alter/7.x>`__

Drupal 8

Use
`hook_form_alter <https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Form%21form.api.php/function/hook_form_alter/8.5.x>`__

Drupal 7 method
---------------

Add the following code to the ``lotus.module`` file:

````

Drupal 8 method
---------------

Add the following code to the ``lotus.module`` file:

````

Gist Link
---------

https://gist.github.com/gauravgoyal/809b13e2901ef4a4c9bb8472ca60a385
