.. include:: /common/global.rst

Pre-process output provided by other modules
============================================

.. container:: message-status

   Fast Track to Drupal 8 Coding – |Back to intro|_ |br| 
   Previous lesson - |Previous lesson|_ |br| 
   Next lesson – |Next lesson|_

.. |Back to intro| replace:: Back to intro
.. _Back to intro: /tutorials/fast-track-drupal-8-coding

.. |Previous lesson| replace:: Update an existing custom schema
.. _Previous lesson: /tutorials/fast-track-drupal-8-coding/update-existing-custom-schema

.. |Next lesson| replace:: Define a custom template for module output
.. _Next lesson: /tutorials/fast-track-drupal-8-coding/define-custom-template-module-output

Lesson Goal
-----------

.. container:: message-status

   Use a preprocess function to change template variables.

Implementation Method
---------------------

Although there are no major changes in how to define preprocess
functions in your custom theme or module, there are some changes in how
you create the variables and with some best practices.

+----------------------------+----------------------------+
| Drupal Version             | Method                     |
+============================+============================+
| Drupal 7                   | Drupal 8                   |
+----------------------------+----------------------------+
| hook\_preprocess\_HOOK()   | hook\_preprocess\_HOOK()   |
+----------------------------+----------------------------+

Drupal 7 method
---------------

.. code-block:: php

    /**
    * Implements hook_preprocess_page()
    * $variables contains all variables used for the template.
    * $hook should be ‘page’ in this case. 
    **/
    function lotus_preprocess_page(&amp;$variables, $hook) {
      // Rendering a table inside the template
      // Using theme for this example. You can create a Render Array and pass it using drupal_render()
      $variables['table'] = theme('table', array('header' => $header, 'rows' => $rows));

      // Pass a text to the template using t() for multilingual an url to create a link
    $variables['create_content'] = t('To create some content <a href="@create-content">click here</a>.', array('@create-content' => url('admin/structure/types/add')));
      //Add a class to the page
      $variables[‘classes_array’][] = ‘new-class’;
      
      // Add a new suggestion for a page template
      // This allows us to use a template name page--lotus.tpl.php
      $variables['theme_hook_suggestions'][] =  'page__lotus';

      //Add a JS library
      drupal_add_js(drupal_get_path('module', 'lotus') . '/js/lotus.js');

    }

Template file page – ``lotus.tpl.php``

Use the $classes variable, which is the flattened output of the
``$classes_array``.

.. code-block:: none

    <div class=‘<? print $classes; ?>’>
      // Print the table variable
      <div class=’table’>
        <? Print $table; ?>
      </div>
      //Print the text and link to create new content
      <p> <? Print $create_content; ?> </p>
    </div>

Drupal 8 method
---------------

In the ``lotus.module`` file:

.. code-block:: php

    /**
    * Implements hook_preprocess_page()
    * $variables contains all variables used for the template.
    * $hook should be ‘page’ in this case. 
    **/
    function lotus_preprocess_page(&amp;$variables, $hook) {
      // Rendering a table inside the template
      // Using a render array is the best practice here - Twigg will render it correctly.
      $variables['table'] = array(
        '#theme' => 'table',
        '#header' => $header,
        '#rows' => $rows,
      );
      //Add a JS library
      $variables['#attached']['library'][] = 'lotus/lotus-js';
    }

    * Implements hook_theme_suggestions_page_alter()
    * $variables contains all variables used for the template.
    * $suggestions will contain the current suggestions for the hook 
    * ‘page’ in this case. 
    **/

    function lotus_theme_suggestions_page_alter(array &amp;$suggestions, array $variables) {
      // Add a new suggestion for a page template
      // This allows us to use a template name page--lotus.tpl.php
      $suggestions[] =  'page__lotus';
    }

In the ``lotus.libraries.yml`` file:

.. code-block:: yaml

    lotus-js:
      version: 1.x
      js:
        js/lotus.js: {}
      dependencies:
        - core/jquery

In the page – ``lotus.html.twig`` file:

.. code-block:: none

    // Add classes in templates is a preferred way in Drupal 8
    {%
      set classes = [
        'new-class',
      ]
    %}
    <div{{ attributes.addClass(classes) }}>
      // Print the table variable
      <div class=’table’>
        {{ table }}
      </div>
      //Print the text and link to create new content
      <p>{{ 'To create some content <a href="@create-content">click here</a>.'|t({'@create-content': url('admin/structure/types/add')}) }}</p>
    </div>

Gist Link
---------

https://gist.github.com/camoa/7686e80ae494f19b3c3cfde1e087ca7b

Resources
---------

-  https://www.drupal.org/docs/8/theming
-  https://api.drupal.org/api/drupal/8.5.x/search/preprocess
