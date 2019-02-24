.. include:: /common/global.rst

Add a field to an existing form
========================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Build a new form
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/build-new-form

.. |Next lesson| replace:: Create users programmatically
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/create-users-programmatically


Lesson Goal
-----------

.. container:: message-status

   Add an **Accept Terms** check box to the User Registration Form.

Implementation Method
---------------------

You can complete this lesson by using either
`hook\_form\_alter <https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_form_alter/7.x>`__
OR ``hook_form_FORM_ID_alter``. Because we need to do a form-specific
changes, we will use the ``hook_form_FORM_ID_alter``.

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Drupal Version
     - Method
   * - Drupal 7
     - Use `hook_form_FORM_ID_alter() <https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_form_FORM_ID_alter/7.x>`__
   * - Drupal 8
     - Use `hook_form_FORM_ID_alter() <https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Form%21form.api.php/function/hook_form_FORM_ID_alter/8.5.x>`__



Drupal 7 method
---------------

Add the following code to the ``lotus.module`` file:

.. code-block:: php

    <?php
    /**
    * @file
    * Add a field to an existing form.
    */
    /**
    * Implements hook_form_FORM_ID_alter().
    */
    function lotus_form_user_register_form_alter(&amp;$form, &amp;$form_state, $form_id) {
      // Add a checkbox to registration form for terms.
      $form['terms'] = array(
        '#type' => 'checkbox',
        '#title' => t("I accept the website's terms."),
        '#required' => TRUE,
      );
    }

Drupal 8 method
---------------

Add the following code to the ``lotus.module`` file:

.. code-block:: php

    <?php
    /**
    * @file
    * Add a field to an existing form.
    */
    use \Drupal\Core\Form\FormStateInterface;

    /**
    * Implements hook_form_FORM_ID_alter().
    */
    function lotus_form_user_register_form_alter(&amp;$form, FormStateInterface $form_state, $form_id) {
      // Add a checkbox to registration form for terms.
      $form['terms'] = array(
        '#type' => 'checkbox',
        '#title' => t("I accept the website's terms."),
        '#required' => TRUE,
      );
    }

Gist Link
---------

https://gist.github.com/vyasamit2007/d9310fda83c79002e6af6032bc89e4e5
