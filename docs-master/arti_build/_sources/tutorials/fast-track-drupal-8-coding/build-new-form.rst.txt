.. include:: /common/global.rst

Build a new form
===================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Alter an existing simple form
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/alter-existing-simple-form

.. |Next lesson| replace:: Add a field to an existing form
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/add-field-existing-form


Lesson Goal
-----------

.. container:: message-status

   Build a new form that validates entries (in this example, the title must 
   be at least 15 characters in length) and also provides a submission 
   function.

Implementation Method
---------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Drupal Version
     - Method
   * - Drupal 7 
     - Use hook_menu_ and drupal_get_form_
   * - Drupal 8
     - Use |routingyml|_ and FormBase_ class

.. _hook_menu: https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_menu/7.x
.. _drupal_get_form: https://api.drupal.org/api/drupal/includes%21form.inc/function/drupal_get_form/7.x
.. _FormBase: https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Form%21FormBase.php/class/FormBase/8.5.x

.. |routingyml| replace:: routing.yml
.. _routingyml: https://www.drupal.org/docs/8/api/routing-system/introductory-drupal-8-routes-and-controllers-example


Drupal 7 method
---------------

Create a ``lotus.info`` file to register your module, with the following
contents:

.. code-block:: none

   name = Lotus
   description = Build a simple form.
   package = Custom
   core = 7.x

Register a menu link using ``hook_menu``. To this, add the following
code in the ``lotus.module`` file:

.. code-block:: php

    /**
    * Implements hook_menu().
    */
    function lotus_menu() {
      $items['simple-form'] = array(
        'title' => 'Simple Form',
        'description' => 'Build a simple form',
        'page callback' => 'drupal_get_form',
        'page arguments' => array('lotus_simple_form'),
        'access arguments' => array('access content'),
      );
      return $items;

    }

Create a form by calling ``drupal_get_form`` and using Form API. To
build the form, add the following code to the ``lotus.module`` file:

.. code-block:: php
   :linenos:

    /**
    * Creates a simple form. Page callback.
    */
    function lotus_simple_form($form, &amp;$form_state) {
      $form['title'] = array(
        '#type' => 'textfield',
        '#title' => t('Title'),
        '#description' => t('Title must be at least 15 characters in length.'),
        '#required' => TRUE,
      );
      // Group submit handlers in an actions element with a key of "actions" so
      // that it gets styled correctly, and so that other modules may add actions
      // to the form. This is not required, but is convention.
      $form['actions'] = [
        '#type' => 'actions',
      ];

      // Add a submit button that handles the submission of the form.
      $form['actions']['submit'] = [
        '#type' => 'submit',
        '#value' => t('Submit'),
      ];

      return $form;
    }

    /**
    * Validation for title. Title must be at least 15 characters in length.
    */
    function lotus_simple_form_validate($form, &amp;$form_state) {
      $title = $form_state['values']['title'];
      if (strlen($title) < 15) {
        // Set an error for the form element with a key of "title".
        form_set_error('title', t('The title must be at least 15 characters long.'));
      }
    }

    /**
    * Display a message after successful form submit.
    */
    function lotus_simple_form_submit($form, &amp;$form_state) {
      $title = $form_state['values']['title'];
      drupal_set_message(t('You specified a title of %title.', ['%title' => $title]));
    }

Drupal 8 method
---------------

#. Create a ``lotus.info.yml`` file with the following contents:

   .. code-block:: yaml

      name: Lotus
      description: Build a basic form.
      type: module
      core: 8.x

#. Register a route by adding the following code to the
   ``lotus.routing.yml`` file:

   .. code-block:: yaml

      lotus.simple_form:
        path: '/simple-form'
        defaults:
          _form:  '\Drupal\lotus\Form\SimpleForm'
          _title: 'Simple Form Example'
        requirements:
          _permission: 'access content'

#. Create a form class extending FormBase to build your form. To do
   this, add the following code to the ``lotus/src/Form/SimpleForm.php``
   file:

   .. code-block:: php
      :linenos:

      <?php
      namespace Drupal\lotus\Form;

      use Drupal\Core\Form\FormBase;
      use Drupal\Core\Form\FormStateInterface;

      /**
      * Implements a simple form.
      */
      class SimpleForm extends FormBase {

        /**
        * Build the simple form.
        *
        * @param array $form
        *   Default form array structure.
        * @param FormStateInterface $form_state
        *   Object containing current form state.
        */
        public function buildForm(array $form, FormStateInterface $form_state) {

          $form['title'] = [
            '#type' => 'textfield',
            '#title' => $this->t('Title'),
            '#description' => $this->t('Title must be at least 15 characters in length.'),
            '#required' => TRUE,
          ];

          // Group submit handlers in an actions element with a key of "actions" so
          // that it gets styled correctly, and so that other modules may add actions
          // to the form. This is not required, but is convention.
          $form['actions'] = [
            '#type' => 'actions',
          ];

          // Add a submit button that handles the submission of the form.
          $form['actions']['submit'] = [
            '#type' => 'submit',
            '#value' => $this->t('Submit'),
          ];

          return $form;
        }

        /**
        * Getter method for Form ID.
        *
        * The form ID is used in implementations of hook_form_alter() to allow other
        * modules to alter the render array built by this form controller.  it must
        * be unique site wide. It normally starts with the providing module's name.
        *
        * @return string
        *   The unique ID of the form defined by this class.
        */
        public function getFormId() {
          return 'lotus_simple_form';
        }

        /**
        * Implements form validation.
        *
        * The validateForm method is the default method called to validate input on
        * a form.
        *
        * @param array $form
        *   The render array of the currently built form.
        * @param FormStateInterface $form_state
        *   Object describing the current state of the form.
        */
        public function validateForm(array &amp;$form, FormStateInterface $form_state) {
          $title = $form_state->getValue('title');
          if (strlen($title) < 15) {
            // Set an error for the form element with a key of "title".
            $form_state->setErrorByName('title', $this->t('The title must be at least 15 characters long.'));
          }
        }

        /**
        * Implements a form submit handler.
        *
        * The submitForm method is the default method called for any submit elements.
        *
        * @param array $form
        *   The render array of the currently built form.
        * @param FormStateInterface $form_state
        *   Object describing the current state of the form.
        */
        public function submitForm(array &amp;$form, FormStateInterface $form_state) {
          /*
          * This would normally be replaced by code that actually does something
          * with the title.
          */
          $title = $form_state->getValue('title');
          drupal_set_message($this->t('You specified a title of %title.', ['%title' => $title]));
        }

      }

Gist Link
---------

https://gist.github.com/gauravgoyal/fa10d45a7512d76a5554ee534b67650c

Resources
---------

-  `Introduction to Form
   API <https://www.drupal.org/docs/8/api/form-api/introduction-to-form-api>`__
-  `Form API in Drupal
   8 <https://api.drupal.org/api/drupal/elements/8.5.x>`__
