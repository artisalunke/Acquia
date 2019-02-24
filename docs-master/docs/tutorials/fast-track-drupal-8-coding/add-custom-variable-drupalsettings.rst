.. include:: /common/global.rst

Add a custom variable to Drupal.Settings
==========================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ 

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Define a custom template for module output
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/define-custom-template-module-output


Lesson Goal
-----------

.. container:: message-status

   Passing configuration values from PHP to a JavaScript library.

In Drupal, you can pass values to your JavaScript using the Drupal
Settings class. The name of the class and how you pass this settings in
Drupal 8 have changed some from Drupal 7.

The following items are new in Drupal 8:

-  A different class in JS (drupalSettings)
-  You have to declare a dependency to core/drupalSettings in your
   library definition.

+--------------------------------------+--------------------------------------+
| Drupal Version                       | Method                               |
+======================================+======================================+
| Drupal 7                             | -  Use drupal\_add\_js() or          |
|                                      |    #attached                         |
|                                      | -  Use Drupal.settings in JS         |
+--------------------------------------+--------------------------------------+
| Drupal 8                             | -  Declare a dependency on           |
|                                      |    DrupalSettings                    |
|                                      | -  Use drupalSettings in JS          |
+--------------------------------------+--------------------------------------+

Drupal 7 method
---------------

In the ``lotus.module`` file:

.. code-block:: PHP

    function lotus_preprocess_html(&amp;$variables) {
      $lotus_height = ‘300px’;
      //Add a JS library
      drupal_add_js(drupal_get_path('module', 'lotus') . '/js/lotus.js');
      drupal_add_js(array('lotus' => array('lotus_height' => $lotus_height)), 'setting');
    }

In the ``lotus.js`` file:

.. code-block:: JavaScript

    (function ($, Drupal) {
    Drupal.behaviors.LotusBehavior = {
      attach: function (context, settings) {
        // can access setting from 'settings' or 'Drupal.settings';
        var lotusHeight = Drupal.settings.lotus.lotus_height;
        $('lotusElement').css('height', lotusHeight);
      }
    };
    })(jQuery, Drupal);

Drupal 8 method
---------------

In the ``lotus.services.yml`` file you have to declare a dependency to
drupalSettings:

.. code-block:: yaml

    lotus-js:
      version: 1.x
      js:
        js/lotus.js: {}
      dependencies:
        - core/jquery
        - core/drupalSettings

In the ``lotus.module`` file:

.. code-block:: PHP

    function lotus_preprocess_html(&amp;$variables) {
      $lotus_height = ‘300px’;
      //Add a JS library
      $variables['#attached']['library'][] = 'lotus/lotus-js';
    $variables['#attached']['drupalSettings']['lotus']['lotusJS']['lotus_height'] = $lotus_height;
    }

In the ``lotus.js`` file:

.. code-block:: JavaScript

    (function ($, Drupal, drupalSettings) {
    Drupal.behaviors.LotusBehavior = {
      attach: function (context, settings) {
        // can access setting from 'drupalSettings';
        var lotusHeight = drupalSettings.lotus.lotusJS.lotus_height;
        $('lotusElement').css('height', lotusHeight);
      }
    };
    })(jQuery, Drupal, drupalSettings);

Gist Link
---------

https://gist.github.com/camoa/dba6280f3f1f1f8bd418f7ed9d5362e6

Resources
---------

https://www.drupal.org/node/2274843
