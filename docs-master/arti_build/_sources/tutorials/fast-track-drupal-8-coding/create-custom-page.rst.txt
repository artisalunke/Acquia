.. include:: /common/global.rst

Create a custom page
====================

| **Fast Track to Drupal 8 Coding** – *`Back to
  Intro </tutorials/fast-track-drupal-8-coding>`__*
| *Next lesson – `Create a custom page with
  arguments </tutorials/fast-track-drupal-8-coding/create-custom-page-arguments>`__*

Lesson Goal
-----------

Create a custom page at ``/hello`` that displays a title of 'Hello
Drupal!' and the following content: 'Welcome to my website!'

Drupal 7 method
---------------

Add the following code to the ``lotus.module`` file:

``/** * Implements hook_menu() **/  function lotus_menu() {     $items['hello'] = array(       'title' => 'Hello Drupal!',       'description' => 'Landing Page for Lotus Module',       'page callback' => 'lotus_hello_view',       'access arguments' => array('access content')     );     return $items;   }  /**  * Page callback function **/    function lotus_hello_view() {     return 'Welcome to my website!';   }``

Drupal 8 method
---------------

#. Add the following code to the ``lotus.routing.yml`` file:

   ``lotus.content:   path: '/hello'   defaults:     _controller: '\Drupal\lotus\Controller\HelloController::content'     _title: 'Hello Drupal!'   requirements:     _permission: 'access content'``

#. Add the following code to the
   ``lotus/src/Controller/HelloController.php`` file:

   ``namespace Drupal\lotus\Controller;  use Drupal\Core\Controller\ControllerBase;  class HelloController extends ControllerBase {   public function content() {     return array(         '#type' => 'markup',         '#markup' => $this->t('Welcome to my website!'),     );   } }``

Gist Link
---------

https://gist.github.com/prasadshir/be232c55197c5011b074ea4efa1f416d

Resources
---------

`Routing system
overview <https://www.drupal.org/docs/8/api/routing-system/routing-system-overview>`__
