.. include:: /common/global.rst

Define a custom template for module output
============================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Pre-process output provided by other modules
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/pre-process-output-provided-other-modules

.. |Next lesson| replace:: Add a custom variable to Drupal.Settings
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/add-custom-variable-drupalsettings


Lesson Goal
-----------

.. container:: message-status

   Provide a custom template/hook for your custom module.

Implementation Method
---------------------

In Drupal 7 and Drupal 8, we use ``hook_theme`` to register a template.
In Drupal 8 the default is a template, and in Drupal 7 you need to
specify that you are defining a template. The ``theme()`` function is
deprecated in Drupal 8.

+------------------+-------------------------------------------------------------+
| Drupal Version   | Method                                                      |
+==================+=============================================================+
| Drupal 7         | hook\_theme() To register the template/hook                 |
|                  | theme() to call the template and render it or               |
|                  | Render Array as a preferable alternative.                   |
+------------------+-------------------------------------------------------------+
| Drupal 8         | hook\_theme() To register the template                      |
|                  | Returning a render Array from a controller content method   |
+------------------+-------------------------------------------------------------+

Drupal 7 method
---------------

In the ``lotus.module`` file:

.. code-block:: php

    /**
    * Implements hook_theme() to add the template definition. 
    **/
    function lotus_theme($existing, $type, $theme, $path) {
      $theme = array();
      $theme['lotus_template'] = array(
        'template' => 'lotus-template',
        'variables' => Array('test_var' => NULL),
      );
      return $theme;
    }
    // In the callback function
    function lotus_callback() {
      $output = theme('lotus_template', array('test_var' => t(‘Test Value’)));
      return $output;
    }

In the templates folder, create the file ``lotus-template.tpl.php``:

``<p> This is the lotus template with a value of <? print $test_var; ?> </p>``

Drupal 8 method
---------------

In the ``lotus.module`` file:

.. code-block:: php

    /**
    * Implements hook_theme() to add the template definition. 
    **/
    function lotus_theme($existing, $type, $theme, $path) {
      return array(
        'lotus_template' => array(
          'variables' => array('test_var' => NULL),
        ),
      );
    }

In the ``LotusController.php`` file:

.. code-block:: php

    //Calling from the Controller
    /**
    * @file
    * Contains \Drupal\lotus\Controller\LotusController.php
    */
    namespace Drupal\lotus\Controller;

    use Drupal\Core\Controller\ControllerBase;

    class LotusController extends ControllerBase {
      public function content() {

        return array(
          '#theme' => 'lotus_template',
          '#test_var' => $this->t('Test Value'),
        );

      }
    }

In the template folder create the ``lotus-template.html.twig`` file:

``<p> This is the lotus template with a value of {{ test_var }} </p>``


Gist Link
---------

https://gist.github.com/camoa/4561530b69243738da6dafa8ad0ddfe5

Resources
---------

-  https://www.drupal.org/docs/8/theming/twig/create-custom-twig-templates-from-custom-module
-  https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Render%21theme.api.php/group/theme_render/8.5.x
-  https://www.drupal.org/docs/8/theming/twig/comparison-of-phptemplate-and-twig-theming-paradigms
